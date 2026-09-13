# CS06: Compiler Design — GATE 2027 CSE Study Plan

## Overview

| Metric | Detail |
|--------|--------|
| **Expected Marks** | 3–5 (1–2 MCQs + 1 NAT) |
| **Difficulty** | Moderate |
| **Scoring Potential** | High — formula-based with practice |
| **Time Estimate** | 25–30 hours total |
| **Priority** | Medium |

---

## GATE 2027 Syllabus

### Front End
1. **Lexical Analysis** — Regular expressions for tokens, finite automata for scanner, symbol table basics
2. **Parsing** — CFG, parse trees, ambiguity, top-down (recursive descent, LL(1)), bottom-up (SLR(1), LR(1), LALR(1)), first and follow sets
3. **Syntax-Directed Translation** — Syntax-directed definitions (SDD), syntax-directed translation schemes (SDT), inherited and synthesized attributes, L-attributed definitions

### Back End
4. **Runtime Environments** — Stack allocation, heap allocation, activation records, parameter passing (call by value, reference, name, copy-restore)
5. **Intermediate Code** — Three-address code, quadruples, triples, inheritance
6. **Code Optimization** — Local optimization (common subexpression elimination, constant propagation), loop optimization (strength reduction, loop invariant code motion)
7. **Code Generation** — Basic block, flow graph, instruction selection, register allocation

---

## PYQ Weightage Analysis (2017–2026)

| Topic | Avg. Questions/Year | Avg. Marks/Year | Trend |
|-------|---------------------|-----------------|-------|
| Parsing (First/Follow, LL/LR) | 1–2 | 2–3 | Stable, **most common** |
| Syntax-Directed Translation | 1 | 1–2 | Moderate |
| Lexical Analysis | 0–1 | 0–1 | Stable |
| Runtime Environments | 0–1 | 0–1 | Moderate |
| Code Optimization | 0–1 | 0–1 | Stable |

**Most Common PYQ Patterns:**
- First and Follow set computation
- LL(1) parsing table construction
- LR(0) / SLR(1) item set construction
- Syntax-directed translation for arithmetic expressions
- SDT evaluation order (S-attributed vs L-attributed)
- Three-address code generation

---

## Topic-Wise Priority

| Topic | Priority | Why |
|-------|----------|-----|
| Parsing (First/Follow, LL/LR) | **HIGHEST** | 2–3 marks guaranteed, formulaic |
| Syntax-Directed Translation | **HIGH** | Frequently tested, moderate difficulty |
| Lexical Analysis (RE → FA) | **MEDIUM** | Moderate frequency, overlaps with TOC |
| Runtime Environments | **MEDIUM** | Occasionally tested |
| Code Optimization | **LOW** | Rarely tested directly |
| Code Generation | **LOW** | Rarely tested |

---

## Recommended Resources

### Free YouTube
| Resource | Topics |
|----------|--------|
| **Knowledge Gate (Sanchit Jain)** — Compiler Design | Best for GATE — exhaustive |
| **Neso Academy** — Compiler Design | Good theory explanations |
| **Gate Smashers** — Compiler Design | Quick revision |

### Books
| Book | Use |
|------|-----|
| **Aho, Sethi, Ullman — Compilers: Principles, Techniques, and Tools** | Dragon Book — gold standard |
| **Louden — Compiler Construction** | Easier to read |
| **Tennent — Programming Language Concepts** | Supplementary |

---

## Week-by-Week Study Plan (3 Weeks)

### Week 1: Lexical Analysis + Parsing (10 hours)

| Day | Topic | Hours | Tasks |
|-----|-------|-------|-------|
| Day 1 | Lexical Analysis | 2 | RE → DFA, scanner implementation basics |
| Day 2 | CFG + First/Follow | 3 | Compute First and Follow sets, solve 10 problems |
| Day 3 | LL(1) Parsing | 2.5 | Parsing table construction, predictive parser |
| Day 4 | LR Parsing (LR(0), SLR(1)) | 2.5 | Item sets, goto/action tables, solve 5 problems |

### Week 2: SDT + Runtime + Intermediate Code (10 hours)

| Day | Topic | Hours | Tasks |
|-----|-------|-------|-------|
| Day 1 | Syntax-Directed Definitions | 2.5 | S-attributed, L-attributed, inherited vs synthesized |
| Day 2 | SDT Translation Schemes | 2.5 | Postfix translation, type checking, solve 10 problems |
| Day 3 | Runtime Environments | 2 | Stack frames, activation records, parameter passing |
| Day 4 | Intermediate Code | 1.5 | Three-address code, quadruples |
| Day 5 | Code Optimization | 1.5 | Basic block optimization, loop optimization |

### Week 3: PYQ Marathon + Revision (10 hours)

| Day | Topic | Hours | Tasks |
|-----|-------|-------|-------|
| Day 1 | LL/LR Parsing Practice | 3 | Solve 20 parsing PYQs |
| Day 2 | SDT PYQ Practice | 2.5 | Solve 15 SDT PYQs |
| Day 3 | Mixed PYQ Marathon | 2.5 | Solve 30 mixed Compiler Design PYQs |
| Day 4 | Final Revision | 2 | Revise formulas, re-solve error log |

---

## Key Concepts and Formulas to Master

### First and Follow Sets
```
FIRST(X):
  If X is terminal: FIRST(X) = {X}
  If X → ε: add ε to FIRST(X)
  If X → Y₁Y₂...Yₙ:
    Add FIRST(Y₁)\{ε} to FIRST(X)
    If ε ∈ FIRST(Y₁): add FIRST(Y₂)\{ε} to FIRST(X)
    Continue until no ε or end of production

FOLLOW(A):
  Add $ to FOLLOW(start symbol)
  If A → αBβ: add FIRST(β)\{ε} to FOLLOW(B)
  If A → αB or A → αBβ where ε ∈ FIRST(β): add FOLLOW(A) to FOLLOW(B)
```

### LL(1) Parsing
```
Parse table construction:
  For each production A → α:
    For each terminal a in FIRST(α): add A → α to M[A, a]
    If ε ∈ FIRST(α): for each b in FOLLOW(A): add A → ε to M[A, b]
    If ε ∈ FIRST(α) and $ ∈ FOLLOW(A): add A → ε to M[A, $]

LL(1) condition:
  For every non-terminal A:
    For every pair of productions A → α and A → β:
      FIRST(α) ∩ FIRST(β) = ∅
      If ε ∈ FIRST(α): FIRST(β) ∩ FOLLOW(A) = ∅
      If ε ∈ FIRST(β): FIRST(α) ∩ FOLLOW(A) = ∅
```

### LR Parsing
```
LR(0) Item: [A → α·β] (dot indicates progress)
Closure(I):
  Add all items in I
  If [A → α·Bβ] is in closure and B → γ is a production:
    Add [B → ·γ] to closure

GOTO(I, X):
  If [A → α·Xβ] is in I: add [A → αX·β] to goto result

SLR(1): Use FOLLOW sets to resolve conflicts
  Shift: if [A → α·aβ] and a is terminal → shift a
  Reduce: if [A → α·] and a ∈ FOLLOW(A) → reduce by A → α
  
LR(1) items: [A → α·β, a] where a is lookahead
LALR(1): Merge LR(1) items with same core (same state, different lookahead)
```

### Syntax-Directed Translation
```
Synthesized Attribute: computed from children (bottom-up)
Inherited Attribute: computed from parent/siblings (top-down)

S-attributed: only synthesized attributes (can evaluate bottom-up)
L-attributed: attributes computed left-to-right (can evaluate with SDT)

Common Translation Schemes:
  E → E₁ + T    { E.val = E₁.val + T.val }
  E → T          { E.val = T.val }
  T → id         { T.val = lookup(id.entry).val }

Type Checking:
  E → E₁ + E₂   { E.type = if E₁.type == E₂.type then E₁.type else error }
```

### Runtime Environments
```
Activation Record:
  ┌──────────────┐
  │ Return value  │
  │ Parameters    │
  │ Control link  │ (pointer to caller's AR)
  │ Access link   │ (for nested scopes)
  │ Saved machine status │
  │ Local variables │
  │ Temporaries    │
  └──────────────┘

Parameter Passing:
  Call by Value: copy of actual parameter
  Call by Reference: alias (address of actual parameter)
  Call by Name: substitute text, evaluate when accessed
  Call by Copy-Restore: copy-in, copy-out
```

### Three-Address Code
```
x = y op z      (binary operation)
x = op y        (unary operation)
x = y           (assignment)
goto L          (unconditional jump)
if x relop y goto L  (conditional jump)
param x         (parameter passing)
call p          (function call)
x = call p      (function call with return value)
return x        (return value)

Example:
  a = b + c * d
  → t1 = c * d
  → t2 = b + t1
  → a = t2
```

---

## Common Mistake Patterns

| Mistake | How to Avoid |
|---------|--------------|
| First/Follow computation errors | Follow start symbol always contains $; follow production A → αBβ adds FIRST(β) to FOLLOW(B) |
| LL(1) table conflicts | If M[A,a] has two entries → grammar is not LL(1) |
| LR(0) item set errors | Closure adds items for non-terminals after dot; GOTO moves dot past symbol |
| SLR(1) vs LR(1) confusion | SLR uses FOLLOW for reduce; LR uses lookahead from item |
| Inherited vs synthesized confusion | Inherited comes from parent/siblings; synthesized from children |
| SDT evaluation order errors | S-attributed: right-to-left; L-attributed: left-to-right |
| Runtime environment stack errors | Always allocate activation record on call, deallocate on return |
| Three-address code mistakes | Break complex expressions into single operations |
| Confusing LL and LR | LL: top-down, uses stack, predicts; LR: bottom-up, uses stack, reduces |
| Lexical analysis vs parsing scope | Lexical: token recognition; Parsing: syntax structure |

---

## PYQ Practice Strategy

### Phase 1: Parsing (Week 1)
- Solve 20 PYQs on First/Follow, LL(1), LR parsing
- Focus on item set construction

### Phase 2: SDT (Week 2)
- Solve 15 PYQs on syntax-directed translation
- Practice attribute evaluation

### Phase 3: Mixed (Week 3)
- Solve 30 mixed Compiler Design PYQs in 45 minutes
- Focus on parsing and SDT

### Key PYQ Problem Types
1. First and Follow set computation
2. LL(1) parsing table construction
3. LR(0) / SLR(1) item set and parsing table
4. SDT for arithmetic expressions
5. Three-address code generation
6. Grammar classification (LL(1)? SLR(1)? LR(1)?)
7. Activation record layout

---

## Topic-Wise Time Estimates

| Topic | Study Time | Practice Time | Total |
|-------|------------|---------------|-------|
| Lexical Analysis | 2 hrs | 1.5 hrs | 3.5 hrs |
| First/Follow Sets | 3 hrs | 3 hrs | 6 hrs |
| LL(1) Parsing | 3 hrs | 3 hrs | 6 hrs |
| LR Parsing | 4 hrs | 3 hrs | 7 hrs |
| Syntax-Directed Translation | 4 hrs | 3 hrs | 7 hrs |
| Runtime Environments | 2 hrs | 1.5 hrs | 3.5 hrs |
| Intermediate Code + Optimization | 2 hrs | 1 hr | 3 hrs |
| **Total** | **20 hrs** | **16 hrs** | **36 hrs** |

---

## Quick Revision Checklist

- [ ] First and Follow computation algorithm
- [ ] LL(1) parsing table construction
- [ ] LR(0) item set construction (closure and goto)
- [ ] SLR(1) vs LR(1) vs LALR(1) differences
- [ ] S-attributed vs L-attributed definitions
- [ ] Common translation schemes (expression, type checking)
- [ ] Activation record structure
- [ ] Parameter passing methods
- [ ] Three-address code format
- [ ] Grammar classification hierarchy (regular ⊂ LL ⊂ LR ⊂ CFG)
