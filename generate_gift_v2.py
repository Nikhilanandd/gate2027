#!/usr/bin/env python3
"""GIFT generator v2 — real GATE CSE PYQs (2012-2025) with real answers from GO mapping.
Event-stream parser: handles interleaved/scrambled option layouts via backward assignment."""
import json, re, sys, os
from collections import Counter, defaultdict

TEXT_DIR = '/tmp/gate_text'
MAP_FILE = '/tmp/answers_topics.json'
OUT_FILE = '/home/nikhil/Documents/GATE/GATE_2027/06_PYQ_Papers/GATE_CSE_PYQ.gift'

MAP = json.load(open(MAP_FILE))

BLACKLIST = {(2013, 1, 16), (2014, 1, 45), (2014, 2, 6), (2022, 1, 39)}

PAPERS = [
    ('2012_CS.txt',    2012, 1, 'cont',   0),
    ('2013_CS.txt',    2013, 1, 'cont',   0),
    ('2014_CS.txt',    2014, 1, 'cont',   0),
    ('2014_CS.txt',    2014, 2, 'cont',   0),
    ('2014_CS.txt',    2014, 3, 'cont',   0),
    ('2016_CS.txt',    2016, 1, 'restart', 0),
    ('2016_CS.txt',    2016, 2, 'restart', 0),
    ('2018_CS.txt',    2018, 1, 'restart', 0),
    ('2022_CS.txt',    2022, 1, 'cont',  10),
    ('2023_CS.txt',    2023, 1, 'cont',  10),
    ('2024_CS1.txt',   2024, 1, 'cont',  10),
    ('2024_CS2.txt',   2024, 2, 'cont',  10),
    ('2025_CS1.txt',   2025, 1, 'cont',  10),
    ('2025_CS2.txt',   2025, 2, 'cont',  10),
    ('2026_CS1.txt',   2026, 1, 'cont',  10),
    ('2026_CS2.txt',   2026, 2, 'cont',  10),
]

SET14 = {1: (320, 1668), 2: (2259, 3599), 3: (4237, 5623)}

NOISE_RES = [
    r'^Page \d+ of \d+$', r'^\d+/\d+$', r'^CS-?[A-D]$', r'^GA$', r'^CS$',
    r'^GATE 20\d\d$', r'^COMPUTER SCIENCE.*$', r'^COMPUTER – CS$',
    r'^General Aptitude.*$', r'^Q\.\d+\s*[–-]\s*Q\.\d+.*$',
    r'^Organiz.*ing Institute.*$', r'^Organising Institute.*$',
    r'^Computer Science and Information Technology.*$', r'^IIT .*$', r'^IISc .*$',
    r'^SESSION.*$', r'^Notations.*$', r'^Question Paper Name.*$',
    r'^Number of Questions.*$', r'^Total Marks.*$', r'^Wrong answer.*$',
    r'^END OF THE QUESTION PAPER$', r'^Answer Key.*$', r'^Key / Range$', r'^Marks$',
    r'^Graduate Aptitude Test in Engineering.*$', r'^Home$', r'^Information Brochure$',
    r'^Pre Examination$', r'^Important Dates$', r'^FAQs$', r'^Contact Us$',
    r'^GA - General Aptitude$', r'^CS: Computer Sc.*$', r'^CS: COMPUTER SCIENCE.*$',
    r'^\(\s*\)$', r'^Q\.No\.? \d+$',
    r'^\*+$', r'^-+$',
]
NOISE = [re.compile(p) for p in NOISE_RES]
WM = [re.compile(p) for p in [r'^\(G$', r'^AT$', r'^E$', r'^\)$', r'^20$', r'^14$', r'^4\)$']]

def is_noise(line, watermark=False):
    t = line.strip()
    if not t:
        return True
    for rx in NOISE:
        if rx.match(t):
            return True
    if watermark:
        for rx in WM:
            if rx.match(t):
                return True
    return False

CTRL = re.compile(r'[\x00-\x08\x0b\x0c\x0e-\x1f]')

NUM = re.compile(r'^-?\d+(\.\d+)?$')

def nat_gift(ans):
    a = str(ans).strip().lower().replace('to', ':').replace(' ', '')
    if a in ('n/a', 'x', 'na', 'none', ''):
        return None
    if ':' in a:
        parts = a.split(':')
        if len(parts) == 2:
            lo, hi = parts
            if lo and NUM.match(lo) and hi and NUM.match(hi):
                return f'{{#{lo}}}' if lo == hi else f'{{#{lo}..{hi}}}'
            if lo and NUM.match(lo) and not hi:
                try:
                    v = float(lo)
                    tol = max(abs(v) * 0.03, 0.01)
                    dec = len(lo.split('.')[-1]) if '.' in lo else 0
                    tol = round(tol, dec)
                    return f'{{#{lo}:{tol}}}'
                except ValueError:
                    return None
        return None
    if NUM.match(a):
        return f'{{#{a}}}'
    return None

def esc(s):
    s = s.replace('\\', '\\\\')
    for ch in '~ = # { } :'.split():
        s = s.replace(ch, '\\' + ch)
    return s

def squeeze(s):
    return re.sub(r'\s+', ' ', s).strip()

BLANK1 = re.compile(r'=\s*\.')
BLANK2 = re.compile(r'\s\.\s')

SYMBOL_FONT = {
    0x28: '(', 0x29: ')', 0x2B: '+', 0x2D: '−', 0x2F: '/', 0x3D: '=', 0x5B: '[', 0x5D: ']',
    0x7B: '{', 0x7D: '}', 0x7C: '|',
    0x22: '∀', 0x24: '∃', 0x27: '∋', 0x2A: '∗', 0x40: '≅',
    0x41: 'Α', 0x42: 'Β', 0x43: 'Χ', 0x44: 'Δ', 0x45: 'Ε', 0x46: 'Φ', 0x47: 'Γ', 0x48: 'Η',
    0x49: 'Ι', 0x4A: 'ϑ', 0x4B: 'Κ', 0x4C: 'Λ', 0x4D: 'Μ', 0x4E: 'Ν', 0x4F: 'Ο', 0x50: 'Π',
    0x51: 'Θ', 0x52: 'Ρ', 0x53: 'Σ', 0x54: 'Τ', 0x55: 'Υ', 0x56: 'ς', 0x57: 'Ω', 0x58: 'Ξ',
    0x59: 'Ψ', 0x5A: 'Ζ', 0x5C: '∴', 0x5E: '⊥',
    0x61: 'α', 0x62: 'β', 0x63: 'χ', 0x64: 'δ', 0x65: 'ε', 0x66: 'φ', 0x67: 'γ', 0x68: 'η',
    0x69: 'ι', 0x6A: 'ϕ', 0x6B: 'κ', 0x6C: 'λ', 0x6D: 'μ', 0x6E: 'ν', 0x6F: 'ο', 0x70: 'π',
    0x71: 'θ', 0x72: 'ρ', 0x73: 'σ', 0x74: 'τ', 0x75: 'υ', 0x76: 'ϖ', 0x77: 'ω', 0x78: 'ξ',
    0x79: 'ψ', 0x7A: 'ζ',
    0xA2: '′', 0xA3: '≤', 0xA5: '∞', 0xB0: '°', 0xB1: '±', 0xB3: '≥', 0xB4: '×', 0xB6: '∂',
    0xB9: '≠', 0xBA: '≡', 0xBB: '≈', 0xC6: '∅', 0xC7: '∩', 0xC8: '∪', 0xCC: '⊂', 0xCD: '⊆',
    0xCE: '∈', 0xCF: '∉', 0xD6: '√', 0xD7: '⋅', 0xE5: 'Σ', 0xF2: '∫',
}
GLYPH_MAP = {chr(0xF000 + k): v for k, v in SYMBOL_FONT.items()}

NOISE_GLOBAL = [
    r'Page\s*\d+\s*of\s*\d+',
    r'Organizing Institute:?\s*[^.]{0,40}',
    r'Computer Science\s*&\s*Information Technology\s*\(CS\d?\)',
    r'Computer Science and Information Technology\s*\(CS\d?\)',
    r'Computer Science & Information Technology',
    r'GA\s*-\s*General Aptitude',
    r'Q\.No\.?\s*\d+',
]
NOISE_TAIL = [
    r'GATE\s*20\d\d',
    r'CS\s*\(Set\s*[-A-Za-z\d]+\)',
    r'CS:\s*Computer Science[^.]*',
    r'CS\d?\)',
]


def clean_text(s):
    for g, r in GLYPH_MAP.items():
        s = s.replace(g, r)
    for pat in NOISE_GLOBAL:
        s = re.sub(pat, ' ', s, flags=re.I)
    changed = True
    while changed:
        changed = False
        for pat in NOISE_TAIL:
            new = re.sub(r'[\s,;:]*' + pat + r'\s*$', '', s, flags=re.I)
            if new != s:
                s = new
                changed = True
    return re.sub(r'\s+', ' ', s).strip()


def dedup_text(t):
    probe = t[:40]
    if len(probe) < 40:
        return t
    second = t.find(probe, 10)
    if second > 0 and t[second:].startswith(t[:second].strip()):
        return t[:second].strip()
    return t


def ensure_blank(text):
    if '____' in text:
        return text
    if BLANK1.search(text):
        return BLANK1.sub('= ________.', text, count=1)
    if BLANK2.search(text):
        return BLANK2.sub(' ________. ', text, count=1)
    return text + ' ________.'

# ---------------- answer lookup ----------------
def answer_key(year, setn, qnum, is_ga):
    if is_ga:
        for fmt in (f'GA{qnum:02d}', f'GA-{qnum:02d}', f'GA-{qnum}', f'GA{qnum}'):
            k = f'{year}|{setn}|{fmt}'
            if k in MAP:
                return MAP[k]
        return None
    for c in (qnum, f'{qnum:02d}'):
        k = f'{year}|{setn}|{c}'
        if k in MAP:
            return MAP[k]
    return None

# ---------------- event-stream parser ----------------
QMARK = re.compile(r'^Q\s*\.?\s*(?:No\.?\s*)?(\d{1,2})(?![\d.])\s*$|^Q\s*\.?\s*(?:No\.?\s*)?(\d{1,2})(?![\d.])\s+(.+)$')
OPT = re.compile(r'^\(?([A-E])\)?\s*$|^\(([A-E])\)\s*(.+)$|^\(([A-E])\)\s*$')

def build_events(lines, watermark=False):
    """Yield events: ('Q', qnum, text_rest) or ('O', letter, chunk_text)."""
    events = []
    pending_text = []
    for ln in lines:
        t = CTRL.sub(' ', ln.strip())
        if not t or is_noise(t, watermark):
            continue
        mq = QMARK.match(t)
        mo = re.match(r'^\(([A-E])\)\s*(.*)$', t)
        if mq:
            qnum = int(mq.group(1) or mq.group(2))
            rest = (mq.group(3) or '').strip()
            if pending_text:
                events.append(('T', ' '.join(pending_text)))
                pending_text = []
            events.append(('Q', qnum, rest))
            if rest:
                pending_text.append(rest)
            continue
        if mo:
            if pending_text:
                events.append(('T', ' '.join(pending_text)))
                pending_text = []
            letter, rest = mo.group(1), mo.group(2).strip()
            events.append(('O', letter, rest))
            continue
        pending_text.append(t)
    if pending_text:
        events.append(('T', ' '.join(pending_text)))
    return events

def parse_region(lines, watermark=False):
    """Single-pass event-stream assignment.
    Returns dict qnum -> {'text': list[str], 'letters': {letter: text_str}}"""
    events = build_events(lines, watermark)
    questions = {}
    order = []
    cur = None          # current question qnum (from Q events)
    pending_opt = None  # (qnum, letter) — option being filled by continuation text

    def find_target(letter, cur_qnum):
        """Forward then backward assignment for option letter."""
        if cur_qnum is not None and letter not in questions[cur_qnum]['letters']:
            return cur_qnum
        for qn in reversed(order):
            q = questions[qn]
            if q['letters'] and letter not in q['letters']:
                return qn
        return None

    for ev in events:
        if ev[0] == 'Q':
            qnum = ev[1]
            pending_opt = None
            if qnum in questions:
                cur = None  # duplicate region
                continue
            questions[qnum] = {'text': [], 'letters': {}}
            order.append(qnum)
            cur = qnum
            if ev[2]:
                questions[qnum]['text'].append(ev[2])
            continue
        if ev[0] == 'O':
            letter, rest = ev[1], ev[2]
            pending_opt = None
            target = find_target(letter, cur)
            if target is None:
                continue
            questions[target]['letters'][letter] = rest
            pending_opt = (target, letter)
            continue
        if ev[0] == 'T':
            text = ev[1]
            if pending_opt is not None:
                tn, ln = pending_opt
                if ln in questions[tn]['letters']:
                    questions[tn]['letters'][ln] = (questions[tn]['letters'][ln] + ' ' + text).strip()
            elif cur is not None:
                questions[cur]['text'].append(text)
            continue
    return questions

CORRUPT_PHRASES = ('Consider the following', 'Consider a ', 'Which of the following', 'Which one of the following',
                   'Does a given program', 'answer in integer', 'Computer Science', 'GATE 20', 'CS(Set')
BROKEN_MATH = re.compile(r'Θ\s*\(\s*[) +]*\)|\(\s*\)')
PRIV = re.compile(r'[\ue000-\uf8ff]')


def option_corrupt(o, limit):
    if PRIV.search(o):
        return True
    if any(p in o for p in CORRUPT_PHRASES):
        return True
    if len(o) > limit:
        return True
    if BROKEN_MATH.search(o):
        return True
    return False


def parse_paper(fname, year, setn, kind, shift):
    lines, watermark = load_lines(fname, year, setn)
    qs = parse_region(lines, watermark)
    out = []
    for qnum in sorted(qs):
        if (year, setn, qnum) in BLACKLIST:
            continue
        q = qs[qnum]
        text = dedup_text(clean_text(squeeze(' '.join(q['text']))))
        opts = {c: clean_text(squeeze(v)) for c, v in q['letters'].items() if squeeze(v)}
        if not text:
            continue
        if kind == 'restart':
            is_ga = qnum <= 10
            cs_q = qnum if qnum > 10 else None
        else:
            is_ga = (qnum <= 10 and year in (2012, 2014, 2016, 2018, 2026))
            cs_q = qnum - shift if shift else qnum
        ans = answer_key(year, setn, qnum, True) if is_ga else answer_key(year, setn, cs_q, False)
        if not ans:
            continue
        goans = str(ans['ans']).strip()
        subject, topic = ans['subject'], ans['topic']
        if opts and len(opts) >= 2:
            if re.fullmatch(r'[A-D][;,][A-D]([;,][A-D])?', goans):
                qtype = 'msq' if all(c in opts for c in re.findall(r'[A-D]', goans)) else None
            elif re.fullmatch(r'[A-D]', goans) and goans in opts:
                qtype = 'mcq'
            else:
                qtype = None
        else:
            qtype = 'nat' if nat_gift(goans) else None
        if qtype is None:
            continue
        if qtype in ('mcq', 'msq'):
            limit = 150 if qtype == 'mcq' else 350
            if any(option_corrupt(o, limit) for o in opts.values()):
                continue
        if PRIV.search(text):
            continue
        if len(text) < 12:
            continue
        if any(bad in text for bad in ('Question Paper Name', 'Number of Questions', 'Total Marks', 'Wrong answer', 'Answer Key', 'END OF THE QUESTION')):
            continue
        if qtype == 'nat':
            text = ensure_blank(text)
        out.append(dict(year=year, set=setn, qnum=qnum, qtype=qtype, text=text,
                        opts=opts, ans=goans, subject=subject, topic=topic,
                        gift_nat=nat_gift(goans) if qtype == 'nat' else None))
    return out

def load_lines(fname, year, setn):
    lines = open(os.path.join(TEXT_DIR, fname), errors='ignore').read().splitlines()
    watermark = (year == 2014)
    if year == 2014:
        s, e = SET14[setn]
        lines = lines[s:e]
        for i, ln in enumerate(lines):
            if 'Answer Keys for CS' in ln:
                lines = lines[:i]
                break
    if year == 2016:
        if setn == 1:
            stop = next((i for i, ln in enumerate(lines) if 'GA Set-6' in ln), len(lines))
            lines = lines[:stop]
        else:
            start = next((i for i, ln in enumerate(lines) if 'GA Set-6' in ln), 0)
            lines = lines[start:]
    return lines, watermark

def build_gift(qs):
    qs = sorted(qs, key=lambda q: (q['subject'], q['year'], q['set'], q['qnum']))
    parts, curcat = [], None
    for q in qs:
        cat = f'GATE CSE PYQ/{q["subject"]}'
        if cat != curcat:
            parts.append(f'$CATEGORY: {cat}\n')
            curcat = cat
        setlab = f'Set {q["set"]}' if q['year'] in (2014, 2016, 2024, 2025, 2026) else ''
        title = f'GATE {q["year"]}' + (f' {setlab}' if setlab else '') + f' Q{q["qnum"]}'
        tesc = esc(q['text'])
        if q['qtype'] == 'mcq':
            letter = q['ans'].strip()
            items = []
            for c in 'ABCDE':
                if c not in q['opts']:
                    continue
                mark = '=' if c == letter else '~'
                items.append(f'{mark}{esc(q["opts"][c])}')
            body = '{' + ' '.join(items) + '}'
        elif q['qtype'] == 'msq':
            letters = re.findall(r'[A-D]', q['ans'])
            k = len(letters)
            w = round(100 / k, 2)
            items = []
            for c in 'ABCDE':
                if c not in q['opts']:
                    continue
                mark = f'~%{w}%' if c in letters else '~%-100%'
                items.append(f'{mark}{esc(q["opts"][c])}')
            body = '{' + ' '.join(items) + '}'
        else:
            body = q['gift_nat']
        src = f'GATE {q["year"]}' + (f' {setlab}' if setlab else '') + f', Q{q["qnum"]}'
        parts.append(f'::{title}::[plain]{tesc} {body}\n####Source: {src}\n')
    return '\n'.join(parts)

def main():
    allq = []
    for fname, year, setn, kind, shift in PAPERS:
        qs = parse_paper(fname, year, setn, kind, shift)
        print(f'{year} set {setn}: {len(qs)}', file=sys.stderr)
        allq.extend(qs)
    seen, uniq = set(), []
    for q in allq:
        k = (q['year'], q['set'], q['qnum'])
        if k in seen:
            continue
        seen.add(k)
        uniq.append(q)
    print(f'TOTAL: {len(uniq)}', file=sys.stderr)
    print('types:', dict(Counter(q['qtype'] for q in uniq)), file=sys.stderr)
    print('subjects:', dict(Counter(q['subject'] for q in uniq)), file=sys.stderr)
    print('years:', dict(Counter(q['year'] for q in uniq)), file=sys.stderr)
    with open(OUT_FILE, 'w', encoding='utf-8') as f:
        f.write(build_gift(uniq))
    print(f'wrote {OUT_FILE} ({os.path.getsize(OUT_FILE)} bytes)', file=sys.stderr)

if __name__ == '__main__':
    main()
