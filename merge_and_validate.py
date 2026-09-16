#!/usr/bin/env python3
"""Merge the real PYQ GIFT file with the curated supplement to produce exactly
1000 questions, then validate the GIFT syntax of the result.

Inputs:
  GATE_2027/06_PYQ_Papers/GATE_CSE_PYQ.gift      (real PYQs, ~707)
  GATE_2027/06_PYQ_Papers/GATE_CSE_CURATED.gift  (curated supplement, ~294)
Output:
  GATE_2027/06_PYQ_Papers/GATE_CSE_1000_Questions.gift
"""
import re
import sys
from collections import Counter

BASE = '/home/nikhil/Documents/GATE/GATE_2027/06_PYQ_Papers/'
PYQ = BASE + 'GATE_CSE_PYQ.gift'
CUR = BASE + 'GATE_CSE_CURATED.gift'
OUT = BASE + 'GATE_CSE_1000_Questions.gift'
TARGET = 1000


def split_questions(content):
    """Split GIFT content into question blocks (each starts with a ::title:: line)."""
    blocks, cur = [], None
    for ln in content.split('\n'):
        if ln.startswith('::'):
            if cur is not None:
                blocks.append('\n'.join(cur))
            cur = [ln]
        elif cur is not None:
            cur.append(ln)
    if cur is not None:
        blocks.append('\n'.join(cur))
    return blocks


def split_answer(block):
    """Return (head_without_answer, answer_body) or (None, None) on failure."""
    src_i = block.find('####Source')
    head = block[:src_i] if src_i != -1 else block
    head = head.rstrip()
    if not head.endswith('}'):
        return None, None
    depth = 0
    for i in range(len(head) - 1, -1, -1):
        c = head[i]
        prev = head[i - 1] if i > 0 else ''
        if c == '}' and prev != '\\':
            depth += 1
        elif c == '{' and prev != '\\':
            depth -= 1
            if depth == 0:
                return head[:i], head[i + 1:-1]
    return None, None


def validate(blocks):
    errors = []
    stats = Counter()
    for bi, block in enumerate(blocks):
        title_m = re.match(r'^::([^:]+)::', block)
        if not title_m:
            errors.append(f'block {bi}: missing/invalid title')
            continue
        title = title_m.group(1)
        if '####Source' not in block:
            errors.append(f'{title}: missing ####Source')
        head, body = split_answer(block)
        if body is None:
            errors.append(f'{title}: missing or malformed answer block')
            continue
        if body.startswith('#'):
            qtype = 'nat'
            if not re.match(r'^#(-?\d+(\.\d+)?(\.\.-?\d+(\.\d+)?|:-?\d+(\.\d+)?)?)(\s|$)', body):
                errors.append(f'{title}: malformed NAT answer: {body[:40]}')
        else:
            marks = re.findall(r'(?<!\\)([=~])', body)
            if '=' in marks:
                qtype = 'mcq'
                if marks.count('=') != 1:
                    errors.append(f'{title}: MCQ has {marks.count("=")} correct options')
                if marks.count('~') < 1:
                    errors.append(f'{title}: MCQ has no distractors')
            else:
                qtype = 'msq'
                if not re.search(r'~%\d', body):
                    errors.append(f'{title}: MSQ missing percentage weights')
                if marks.count('~') < 2:
                    errors.append(f'{title}: MSQ has too few options')
        stats[qtype] += 1
        stats['total'] += 1
    return errors, stats


def main():
    pyq = open(PYQ, encoding='utf-8').read()
    cur = open(CUR, encoding='utf-8').read()
    pyq_blocks = split_questions(pyq)
    cur_blocks = split_questions(cur)
    print(f'PYQ questions:     {len(pyq_blocks)}')
    print(f'Curated questions: {len(cur_blocks)}')

    need = TARGET - len(pyq_blocks)
    if need < 0:
        print(f'ERROR: PYQ file already exceeds {TARGET}', file=sys.stderr)
        sys.exit(1)
    if need != len(cur_blocks):
        print(f'ERROR: curated count mismatch ({need} needed, {len(cur_blocks)} available)', file=sys.stderr)
        sys.exit(1)

    merged = pyq.rstrip() + '\n\n' + cur.rstrip() + '\n'
    with open(OUT, 'w', encoding='utf-8') as f:
        f.write(merged)

    blocks = split_questions(merged)
    errors, stats = validate(blocks)
    print(f'\nMerged file: {OUT}')
    print(f'Total questions: {len(blocks)}')
    print(f'By type: {dict(stats)}')
    if errors:
        print(f'\nVALIDATION ERRORS ({len(errors)}):')
        for e in errors[:40]:
            print('  -', e)
        sys.exit(1)
    print('\nGIFT syntax validation: PASSED')

    cats = Counter(re.findall(r'^\$CATEGORY:\s*(.+)$', merged, re.M))
    print(f'\nCategories ({len(cats)}):')
    for c, n in sorted(cats.items()):
        print(f'  {c}: {n} blocks')


if __name__ == '__main__':
    main()
