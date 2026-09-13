# CS01: Digital Logic — GATE 2027 CSE Study Plan

## Overview

| Metric | Detail |
|--------|--------|
| **Expected Marks** | 3–5 (1–2 MCQs + 1–2 NAT/MSQ) |
| **Difficulty** | Moderate |
| **Scoring Potential** | High — deterministic, formula-based |
| **Time Estimate** | 25–30 hours total |
| **Priority** | Medium |

---

## GATE 2027 Syllabus

1. **Boolean Algebra** — Basic theorems, properties of Boolean algebra
2. **Minimization** — Karnaugh map (up to 5 variables), Tabular method (Quine-McCluskey)
3. **Combinational Circuits** — Multiplexers, decoders, adders, subtractors, code converters, parity generators
4. **Sequential Circuits** — Latches, flip-flops (SR, JK, D, T), counters (synchronous, asynchronous), shift registers, state diagrams, state tables
5. **Number Representation** — Fixed point (signed magnitude, 1's complement, 2's complement), floating point (IEEE 754 single precision), arithmetic operations
6. **Logic Gates** — AND, OR, NOT, NAND, NOR, XOR, XNOR — realization using universal gates

---

## PYQ Weightage Analysis (2017–2026)

| Topic | Avg. Questions/Year | Avg. Marks/Year | Trend |
|-------|---------------------|-----------------|-------|
| Boolean Algebra & Minimization | 1–2 | 1–2 | Stable |
| Combinational Circuits | 1 | 1–2 | Stable |
| Sequential Circuits | 1–2 | 2–3 | Increasing |
| Number Representation & Arithmetic | 0–1 | 1–2 | Stable |
| Logic Gate Realization | 0–1 | 0–1 | Declining |

**Most Common PYQ Patterns:**
- K-map with don't-care conditions (5+ marks problems)
- Flip-flop timing analysis and state machine design
- IEEE 754 floating point representation and conversion
- Counter design with specific sequences

---

## Topic-Wise Priority

| Topic | Priority | Why |
|-------|----------|-----|
| K-map Minimization | **HIGH** | Most frequently tested, easy to score |
| Sequential Circuits (Flip-flops, Counters) | **HIGH** | High weightage, moderate difficulty |
| Number Representation (2's complement, IEEE 754) | **HIGH** | Frequently appears in MCQs and NATs |
| Combinational Circuits | **MEDIUM** | Moderate frequency, conceptual |
| Boolean Algebra Theorems | **MEDIUM** | Foundation, tested indirectly |
| Logic Gate Realization | **LOW** | Simple, rarely tested directly |

---

## Recommended Resources

### Free YouTube
| Resource | Topics | Link |
|----------|--------|------|
| **Neso Academy** — Digital Logic | Full syllabus, best for theory | youtube.com/nesoacademy |
| **Gate Smashers** — Digital Logic | Quick revision, PYQ solving | youtube.com/gatesmashers |
| **Jenny's Lectures** — Digital Logic | Alternate explanations | youtube.com/jennyslectures |

### Books
| Book | Use |
|------|-----|
| **Morris Mano — Digital Design** | Primary reference, best for concepts |
| **Anand Kumar — Digital Design** | Indian author, more examples |

### Practice
- PYQ Topic-wise: Subject practice on GO portal or standard question banks
- GeeksforGeeks Digital Logic section for quick MCQs

---

## Week-by-Week Study Plan (3 Weeks)

### Week 1: Boolean Algebra + Minimization + Combinational Circuits (10 hours)

| Day | Topic | Hours | Tasks |
|-----|-------|-------|-------|
| Day 1 | Boolean Algebra | 2 | Read Mano Ch. 2, solve 20 problems |
| Day 2 | K-map (2, 3, 4 variable) | 3 | Watch Neso Academy lectures, solve 15 K-map problems |
| Day 3 | K-map (5 variable) + Don't cares | 2.5 | Practice 10 advanced K-map problems |
| Day 4 | Tabular Method | 2.5 | Learn Quine-McCluskey, solve 5 problems |

### Week 2: Combinational + Sequential Circuits (10 hours)

| Day | Topic | Hours | Tasks |
|-----|-------|-------|-------|
| Day 1 | Combinational Circuits | 2.5 | MUX, decoder, adder — watch Neso Academy |
| Day 2 | Combinational Practice | 2 | Solve 15 PYQ problems on combinational |
| Day 3 | Flip-flops (SR, JK, D, T) | 2.5 | Characteristic equations, excitation tables |
| Day 4 | Counters & Shift Registers | 3 | Synchronous/asynchronous counter design |

### Week 3: Number Representation + Revision (10 hours)

| Day | Topic | Hours | Tasks |
|-----|-------|-------|-------|
| Day 1 | Number Systems | 2.5 | Signed magnitude, 1's, 2's complement |
| Day 2 | IEEE 754 Floating Point | 3 | Single precision format, conversions, practice 10 problems |
| Day 3 | Sequential Circuit Design | 2.5 | State diagram → state table → flip-flop design |
| Day 4 | Full Revision + PYQ Marathon | 2 | Solve 30 mixed PYQs, identify weak areas |

---

## Key Formulas and Concepts to Master

### Boolean Algebra
```
A + A·B = A (Absorption)
A·(A + B) = A (Absorption)
De Morgan's: (A·B)' = A' + B'  |  (A+B)' = A'·B'
A ⊕ B = A'B + AB'
A ⊙ B = AB + A'B
```

### K-map
```
Adjacent cells differ by exactly 1 variable
Group sizes: 1, 2, 4, 8, 16 (powers of 2)
Don't cares (X) can be 0 or 1 — use to maximize group size
Essential prime implicants: must include for some minterm
```

### Number Representation
```
2's complement of X = 1's complement of X + 1
Range (n bits): -2^(n-1) to 2^(n-1) - 1
IEEE 754 Single: (-1)^S × 1.M × 2^(E-127)
  S: 1 bit, Exponent: 8 bits (biased 127), Mantissa: 23 bits
```

### Flip-flop Excitation Tables
```
SR:  Q(t)→Q(t+1) | S | R
     0→0          | 0 | X
     0→1          | 1 | 0
     1→0          | 0 | 1
     1→1          | X | 0

JK:  Q(t)→Q(t+1) | J | K
     0→0          | 0 | X
     0→1          | 1 | X
     1→0          | X | 1
     1→1          | X | 0

D:   Q(t)→Q(t+1) | D
     0→0          | 0
     0→1          | 1
     1→0          | 0
     1→1          | 1
```

---

## Common Mistake Patterns

| Mistake | How to Avoid |
|---------|--------------|
| Forgetting don't cares in K-map | Always check if don't cares can extend groups |
| Wrong grouping in K-map (diagonal/odd sizes) | Only adjacent cells, sizes must be powers of 2 |
| Confusing 1's complement and 2's complement range | 2's complement has one extra negative number |
| IEEE 754 biased exponent error | Bias is 127 for single, 1023 for double |
| Counter MOD calculation error | MOD = number of unique states, not FF count |
| Asynchronous counter timing issues | Output of one FF clocks the next — ripple effect |
| State diagram conversion mistakes | Always verify every input combination for each state |

---

## PYQ Practice Strategy

### Phase 1: Topic-wise (Week 1–2)
- Solve 2017–2026 PYQs topic by topic
- Focus: K-map → Number Representation → Sequential Circuits
- Maintain error log for recurring mistakes

### Phase 2: Mixed Practice (Week 3)
- Solve 50 mixed Digital Logic PYQs in 60 minutes
- Track accuracy by topic
- Time per question target: ~70 seconds

### Phase 3: Revision (Before exam)
- Revise formulas from cheat sheet
- Re-solve all questions from error log
- Take 2 mini-mocks (10 questions each, 15 minutes)

### Key PYQ Problem Types to Master
1. K-map minimization with 4–5 variables
2. Number of gates for specific expression
3. IEEE 754 conversion (decimal ↔ floating point)
4. Counter design for specific sequence
5. State machine design from word problem
6. Flip-flop excitation table derivation

---

## Topic-Wise Time Estimates

| Topic | Study Time | Practice Time | Total |
|-------|------------|---------------|-------|
| Boolean Algebra | 3 hrs | 2 hrs | 5 hrs |
| K-map Minimization | 4 hrs | 3 hrs | 7 hrs |
| Tabular Method | 2 hrs | 1.5 hrs | 3.5 hrs |
| Combinational Circuits | 3 hrs | 2 hrs | 5 hrs |
| Sequential Circuits | 5 hrs | 3 hrs | 8 hrs |
| Number Representation | 3 hrs | 2 hrs | 5 hrs |
| IEEE 754 | 2 hrs | 2 hrs | 4 hrs |
| **Total** | **22 hrs** | **15.5 hrs** | **37.5 hrs** |

---

## Quick Revision Checklist

- [ ] Boolean algebra theorems (absorption, De Morgan's, consensus)
- [ ] K-map: 2-variable through 5-variable
- [ ] Quine-McCluskey tabular method steps
- [ ] All flip-flop characteristic and excitation tables
- [ ] Synchronous counter design procedure
- [ ] 2's complement arithmetic
- [ ] IEEE 754 single precision format
- [ ] Parity generator/checker circuits
- [ ] MUX implementation of Boolean functions
- [ ] MOD-N counter calculations
