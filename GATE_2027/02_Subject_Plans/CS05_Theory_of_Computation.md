# CS05: Theory of Computation — GATE 2027 CSE Study Plan

## Overview

| Metric | Detail |
|--------|--------|
| **Expected Marks** | 5–7 (1–2 MCQs + 1–2 NAT/MSQ) |
| **Difficulty** | Hard |
| **Scoring Potential** | Medium — conceptual, requires careful study |
| **Time Estimate** | 30–35 hours total |
| **Priority** | Medium-High |

---

## GATE 2027 Syllabus

### Formal Languages & Automata
1. **Regular Languages** — Regular expressions (RE), equivalence of RE and FA, closure properties
2. **Finite Automata** — DFA, NFA, NFA to DFA minimization, equivalence, Myhill-Nerode theorem
3. **Context-Free Languages** — Context-Free Grammars (CFG), parse trees, ambiguity, Chomsky Normal Form (CNF), Greibach Normal Form (GNF)
4. **Pushdown Automata** — PDA for CFLs, deterministic PDA, equivalence of PDA and CFL
5. **Pumping Lemma** — For regular languages, for CFLs

### Computability
6. **Turing Machines** — Definition, variants, Church-Turing thesis
7. **Decidability** — Decidable and undecidable languages, Halting problem
8. **Reducibility** — Mapping reducibility, problems reducible to Halting problem
9. **Complexity Classes** — P, NP, NP-complete, NP-hard (basic understanding)

---

## PYQ Weightage Analysis (2017–2026)

| Topic | Avg. Questions/Year | Avg. Marks/Year | Trend |
|-------|---------------------|-----------------|-------|
| Regular Languages (RE ↔ FA) | 1–2 | 2–3 | Stable, **most common** |
| Context-Free Languages (CFG, CFL) | 1–2 | 2–3 | Stable |
| Pumping Lemma | 0–1 | 1–2 | Moderate |
| Turing Machines & Decidability | 1 | 1–2 | Stable |
| DFA Construction | 1 | 1–2 | Increasing |

**Most Common PYQ Patterns:**
- Regular expression ↔ DFA/NFA conversion
- CFG construction for given language
- Pumping lemma proof (regular or CFL)
- Language closure properties (union, intersection, complement)
- Decidability questions (which is decidable/undecidable)
- CFL closure properties

---

## Topic-Wise Priority

| Topic | Priority | Why |
|-------|----------|-----|
| Regular Expressions ↔ Finite Automata | **HIGHEST** | Most frequently tested, formulaic |
| Context-Free Languages (CFG, CNF) | **HIGH** | High frequency, conceptual |
| Pumping Lemma (Regular + CFL) | **HIGH** | Frequently tested, requires practice |
| Decidability & Turing Machines | **MEDIUM** | Moderate frequency, tricky |
| PDA Construction | **LOW** | Rarely tested directly |

---

## Recommended Resources

### Free YouTube
| Resource | Topics |
|----------|--------|
| **Knowledge Gate (Sanchit Jain)** — TOC | Best for GATE — exhaustive coverage |
| **Neso Academy** — TOC | Good theory explanations |
| **Gate Smashers** — TOC | Quick revision |
| **Ravindrababu Ravula** — TOC | Short conceptual videos |

### Books
| Book | Use |
|------|-----|
| **Hopcroft, Motwani, Ullman — Intro to Automata Theory** | Gold standard |
| **Peter Linz — Introduction to Automata and Formal Languages** | Easier to read |
| **Sipser — Introduction to the Theory of Computation** | More advanced, good for NP |

---

## Week-by-Week Study Plan (3.5 Weeks)

### Week 1: Regular Languages + Finite Automata (10 hours)

| Day | Topic | Hours | Tasks |
|-----|-------|-------|-------|
| Day 1 | Regular Expressions | 2.5 | Learn RE syntax, closure properties, solve 15 RE problems |
| Day 2 | DFA Construction | 3 | Build DFAs for given languages, minimize DFA |
| Day 3 | NFA ↔ DFA Conversion | 2.5 | Subset construction, epsilon-closure, NFA to DFA |
| Day 4 | Myhill-Nerode + Pumping Lemma (Regular) | 2 | Equivalence classes, prove non-regular languages |

### Week 2: Context-Free Languages + PDA (10 hours)

| Day | Topic | Hours | Tasks |
|-----|-------|-------|-------|
| Day 1 | CFG Fundamentals | 2.5 | Parse trees, ambiguity, leftmost/rightmost derivations |
| Day 2 | CNF and GNF | 2.5 | Convert grammar to CNF, solve 10 problems |
| Day 3 | Pumping Lemma for CFL | 3 | Prove languages are not CFL, solve 10 problems |
| Day 4 | CFL Properties | 2 | Closure properties, deterministic CFL vs CFL |

### Week 3: Turing Machines + Decidability (10 hours)

| Day | Topic | Hours | Tasks |
|-----|-------|-------|-------|
| Day 1 | Turing Machines | 2.5 | Basic TM definition, variants, Church-Turing thesis |
| Day 2 | Decidability | 3 | Decidable vs undecidable, Halting problem |
| Day 3 | Reducibility & NP | 2.5 | Mapping reducibility, P vs NP basics |
| Day 4 | PYQ Marathon | 2 | Solve 30 mixed TOC PYQs |

### Week 3.5: Revision (5 hours)

| Day | Topic | Hours | Tasks |
|-----|-------|-------|-------|
| Day 1 | Regular + CFL Revision | 2.5 | Re-solve key problems, revise closure properties |
| Day 2 | Final Revision | 2.5 | TM, decidability, error log review |

---

## Key Concepts and Formulas to Master

### Finite Automata
```
DFA: Exactly one transition per symbol from each state
NFA: Zero or more transitions per symbol, can have ε-transitions
ε-NFA: NFA with epsilon transitions

Subset Construction (NFA → DFA):
  DFA states = power set of NFA states
  Start state = ε-closure of NFA start state
  For each DFA state {q₁, q₂, ...} and symbol a:
    DFA transition = ε-closure of union of NFA transitions from q₁, q₂, ... on a

DFA Minimization:
  1. Remove unreachable states
  2. Partition states into accepting and non-accepting
  3. Refine partitions until no further splitting possible
  4. Each partition becomes one state in minimized DFA

Myhill-Nerode Theorem:
  Number of states in minimized DFA = number of equivalence classes of ≋_L
```

### Regular Expressions
```
Base: ∅, ε, a (single symbol)
Union: R₁ + R₂
Concatenation: R₁ · R₂ (or R₁R₂)
Kleene Star: R₁*

Equivalences:
  a* = ε + a + aa + aaa + ...
  (a+b)* = all strings over {a,b}
  (a+b)*abb = strings ending with "abb"
  
Conversion: RE → ε-NFA (Thompson's construction)
           FA → RE (State elimination)
```

### Context-Free Grammars
```
G = (V, Σ, P, S)
  V: variables (non-terminals)
  Σ: terminals
  P: productions (V → (V ∪ Σ)*)
  S: start variable

Derivation:
  Leftmost: always expand leftmost variable
  Rightmost: always expand rightmost variable
  Parse tree: graphical representation of derivation

Ambiguity: grammar with two different leftmost derivations for same string
  → ambiguous grammar → may need unambiguous grammar

Chomsky Normal Form (CNF):
  All productions: A → BC or A → a or S → ε
  (B, C ≠ S; a ∈ Σ)
  Every CFG can be converted to CNF

Greibach Normal Form (GNF):
  All productions: A → aα where a ∈ Σ, α ∈ V*
```

### Pumping Lemma
```
Regular Language Pumping Lemma:
  If L is regular, ∃ p (pumping length) such that ∀ w ∈ L with |w| ≥ p:
    w = xyz where:
    1. |xy| ≤ p
    2. |y| ≥ 1
    3. ∀ i ≥ 0: xy^iz ∈ L

CFL Pumping Lemma:
  If L is CFL, ∃ p such that ∀ w ∈ L with |w| ≥ p:
    w = uvxyz where:
    1. |vy| ≥ 1
    2. |vxy| ≤ p
    3. ∀ i ≥ 0: uv^ixy^iz ∈ L

Usage: To prove language is NOT regular/CFL
  1. Assume L is regular/CFL
  2. Take w = a^p b^p (or appropriate string)
  3. Apply pumping lemma
  4. Show pumped string ∉ L — contradiction
```

### Turing Machines
```
TM = (Q, Σ, Γ, δ, q₀, q_accept, q_reject)
  Q: finite set of states
  Σ: input alphabet
  Γ: tape alphabet (Σ ⊂ Γ, ⊔ ∈ Γ for blank)
  δ: Q × Γ → Q × Γ × {L, R} (transition function)
  q₀: start state
  q_accept, q_reject: halting states

Church-Turing Thesis:
  Anything computable by an algorithm is computable by a TM

Variants: multi-tape, non-deterministic, etc. — all equivalent in power
```

### Decidability
```
Decidable (Recursive): TM always halts and gives yes/no answer
Semi-decidable (Recursively Enumerable): TM halts on yes, may loop on no

Key Decidable Problems:
  - DFA acceptance, emptiness, equivalence
  - CFL emptiness, finiteness
  - Regular expression equivalence

Key Undecidable Problems:
  - Halting problem (does TM halt on input?)
  - DFA equivalence (is L(M₁) = L(M₂)?) — wait, this IS decidable
  - CFG membership (given G, w: is w ∈ L(G)?) — undecidable
  - Post Correspondence Problem
  - Rice's Theorem: any non-trivial property of RE languages is undecidable
```

### Closure Properties
```
Regular Languages:
  ✓ Union, intersection, complement, concatenation, star
  ✓ Reverse, homomorphism, inverse homomorphism
  ✓ Difference, symmetric difference

CFL:
  ✓ Union, concatenation, star, reverse
  ✓ Homomorphism, inverse homomorphism
  ✗ Intersection (NOT closed)
  ✗ Complement (NOT closed)
  Note: CFL ∩ Regular = CFL (intersection with regular is fine)

RE:
  ✓ Union, intersection, concatenation, star, complement
  ✓ (Closed under all operations)
```

---

## Common Mistake Patterns

| Mistake | How to Avoid |
|---------|--------------|
| Confusing NFA and DFA | DFA: exactly one transition per symbol; NFA: zero or more |
| Wrong pumping lemma string choice | Choose w that forces |y| to contain specific structure |
| Ambiguous grammar identification | Check if two different parse trees exist for same string |
| CFL closure property errors | CFL is NOT closed under intersection or complement |
| Decidability classification error | Use Rice's theorem for RE language properties |
| Wrong CNF conversion | Eliminate unit productions, empty productions, and long productions in order |
| DFA minimization partition error | Re-check partition refinement until stable |
| TM state diagram mistakes | Each transition: read, write, move (L/R) must be defined |
| Confusing RE with CFL | RE = Regular expressions; CFL = CFG-generated |
| Pumping lemma conclusion error | Lemma proves "if L regular then pumped string in L" — contrapositive proves non-regular |

---

## PYQ Practice Strategy

### Phase 1: Regular Languages (Week 1)
- Solve 25 PYQs on RE ↔ DFA, closure properties
- Practice DFA construction from description

### Phase 2: CFL + Pumping Lemma (Week 2)
- Solve 20 PYQs on CFG, CNF, pumping lemma proofs
- Practice proving languages are not CFL

### Phase 3: Decidability + Mixed (Week 3)
- Solve 15 PYQs on decidability and TM
- Mixed practice: 30 questions in 45 minutes

### Key PYQ Problem Types
1. RE ↔ DFA/NFA conversion
2. DFA minimization
3. Language closure properties (given operations, what class is result?)
4. Pumping lemma proofs
5. CFG construction for given language
6. CNF conversion
7. Decidable/undecidable classification
8. Language class identification (Regular? CFL? RE?)

---

## Topic-Wise Time Estimates

| Topic | Study Time | Practice Time | Total |
|-------|------------|---------------|-------|
| Regular Expressions | 3 hrs | 2.5 hrs | 5.5 hrs |
| Finite Automata (DFA/NFA) | 5 hrs | 4 hrs | 9 hrs |
| Pumping Lemma | 3 hrs | 3 hrs | 6 hrs |
| CFG & CNF | 4 hrs | 3 hrs | 7 hrs |
| CFL Properties | 2 hrs | 1.5 hrs | 3.5 hrs |
| Turing Machines | 3 hrs | 2 hrs | 5 hrs |
| Decidability | 3 hrs | 2.5 hrs | 5.5 hrs |
| **Total** | **23 hrs** | **18.5 hrs** | **41.5 hrs** |

---

## Quick Revision Checklist

- [ ] DFA construction from RE
- [ ] NFA to DFA subset construction algorithm
- [ ] DFA minimization procedure
- [ ] Pumping lemma template for regular languages
- [ ] Pumping lemma template for CFLs
- [ ] CFL closure properties (which operations work)
- [ ] CNF conversion steps
- [ ] Decidable vs undecidable problems (key examples)
- [ ] Rice's theorem application
- [ ] Church-Turing thesis statement
