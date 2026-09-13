# CS08: Databases — GATE 2027 CSE Study Plan

## Overview

| Metric | Detail |
|--------|--------|
| **Expected Marks** | 7–9 (2–3 MCQs + 1–2 NAT/MSQ) |
| **Difficulty** | Moderate |
| **Scoring Potential** | **Very High** — formulaic with practice |
| **Time Estimate** | 35–40 hours total |
| **Priority** | **HIGH** |

---

## GATE 2027 Syllabus

### Data Models & Design
1. **ER Model** — Entities, attributes, relationships (1:1, 1:N, M:N), weak entities, ISA hierarchy, ER to relational mapping
2. **Relational Model** — Relations, tuples, attributes, domains, keys (primary, foreign, candidate, super), integrity constraints (domain, key, referential, NOT NULL)

### Query Languages
3. **Relational Algebra** — Selection, projection, cartesian product, union, set difference, rename, natural join, theta join, division
4. **Tuple Relational Calculus** — Existential (∃) and universal (∀) quantifiers, safe expressions
5. **SQL** — DDL (CREATE, ALTER, DROP), DML (SELECT, INSERT, UPDATE, DELETE), JOINs, subqueries, GROUP BY, HAVING, aggregate functions (COUNT, SUM, AVG, MIN, MAX), set operations (UNION, INTERSECT, EXCEPT), views, triggers

### Normalization
6. **Functional Dependencies** — Definition, Armstrong's axioms (reflexivity, augmentation, transitivity), closure, canonical cover
7. **Normalization** — 1NF, 2NF, 3NF, BCNF, decomposition (lossless join, dependency preserving)
8. **Multi-valued Dependencies** — 4NF

### Storage & Indexing
9. **File Organization** — Heap, sorted, hashing, cluster
10. **Indexing** — Dense/sparse index, primary/secondary index, B-tree, B+ tree

### Transactions
11. **Transaction Concepts** — ACID properties, transaction states
12. **Concurrency Control** — Serializability (conflict, view), lock-based protocols (2PL, strict 2PL), timestamp ordering, deadlock handling
13. **Recovery** — Log-based recovery, checkpointing, ARIES algorithm basics

---

## PYQ Weightage Analysis (2017–2026)

| Topic | Avg. Questions/Year | Avg. Marks/Year | Trend |
|-------|---------------------|-----------------|-------|
| Normalization (FD, 2NF, 3NF, BCNF) | 2–3 | 3–4 | Stable, **most common** |
| SQL Queries | 1–2 | 2–3 | Stable, high value |
| ER Model | 1 | 1–2 | Moderate |
| Relational Algebra | 1 | 1–2 | Stable |
| Transactions & Concurrency | 1 | 1–2 | Stable |
| Indexing (B/B+ Tree) | 0–1 | 0–1 | Moderate |

**Most Common PYQ Patterns:**
- Normalization (find key, determine 2NF/3NF/BCNF, decompose)
- SQL query output prediction
- Relational algebra expression evaluation
- ER to relational mapping
- Functional dependency closure
- Serializability (precedence graph)
- B+ tree insertion/deletion

---

## Topic-Wise Priority

| Topic | Priority | Why |
|-------|----------|-----|
| Normalization (FD, 2NF/3NF/BCNF) | **HIGHEST** | 3–4 marks guaranteed, formulaic |
| SQL Queries | **HIGHEST** | Always tested, 2–3 marks |
| Relational Algebra | **HIGH** | Frequent, formulaic |
| ER Model | **HIGH** | Moderate frequency, conceptual |
| Transactions & Concurrency | **MEDIUM** | Moderate frequency |
| Indexing (B/B+ Tree) | **LOW** | Rarely tested directly |

---

## Recommended Resources

### Free YouTube
| Resource | Topics |
|----------|--------|
| **Gate Smashers** — DBMS | Best for GATE — exhaustive, popular |
| **Knowledge Gate (Sanchit Jain)** — DBMS | Detailed theory |
| **Neso Academy** — DBMS | Good for fundamentals |

### Books
| Book | Use |
|------|-----|
| **Korth, Silberschatz — Database System Concepts** | Gold standard |
| **Navathe — Fundamentals of Database Systems** | Good for normalization |
| **Ramakrishnan — Database Management Systems** | More advanced |

---

## Week-by-Week Study Plan (4 Weeks)

### Week 1: ER Model + Relational Model + Algebra (10 hours)

| Day | Topic | Hours | Tasks |
|-----|-------|-------|-------|
| Day 1 | ER Model | 2.5 | Entities, relationships, weak entities, ISA — solve 5 ER problems |
| Day 2 | ER to Relational Mapping | 2 | Convert ER diagrams to tables, practice 5 problems |
| Day 3 | Relational Algebra | 3 | All operations, practice 15 algebra expression problems |
| Day 4 | Tuple Relational Calculus | 2.5 | Existential/universal quantifiers, practice 10 problems |

### Week 2: SQL + Normalization (10 hours)

| Day | Topic | Hours | Tasks |
|-----|-------|-------|-------|
| Day 1 | SQL Basics (DDL + DML) | 2.5 | CREATE, INSERT, SELECT, UPDATE, DELETE |
| Day 2 | SQL Advanced (JOINs, Subqueries, GROUP BY) | 3 | Practice 10 SQL query problems |
| Day 3 | Functional Dependencies | 2.5 | Armstrong's axioms, closure computation, canonical cover |
| Day 4 | Normalization (1NF → BCNF) | 2 | All normal forms, decomposition techniques |

### Week 3: Normalization Practice + Transactions (10 hours)

| Day | Topic | Hours | Tasks |
|-----|-------|-------|-------|
| Day 1 | Normalization Deep Dive | 3 | Solve 20 normalization PYQs |
| Day 2 | Decomposition (Lossless + Dependency Preserving) | 2.5 | Algorithms and practice |
| Day 3 | Transaction Concepts | 2 | ACID, states, schedules |
| Day 4 | Concurrency Control | 2.5 | Serializability, 2PL, deadlock handling |

### Week 4: Indexing + Full Revision (10 hours)

| Day | Topic | Hours | Tasks |
|-----|-------|-------|-------|
| Day 1 | File Organization + Indexing | 2.5 | B-tree, B+ tree basics |
| Day 2 | PYQ Marathon — Full Subject | 3 | Solve 50 mixed DB PYQs |
| Day 3 | Weak Areas + SQL Practice | 2.5 | Focus on weakest areas |
| Day 4 | Final Revision | 2 | Revisit all formulas |

---

## Key Concepts and Formulas to Master

### Relational Algebra
```
Selection: σ_condition(R) — select rows
Projection: π_attributes(R) — select columns
Cartesian Product: R × S — all combinations
Union: R ∪ S — all tuples in R or S (same schema)
Set Difference: R - S — tuples in R but not S
Rename: ρ_new_name(R) — rename relation/attributes

Natural Join: R ⋈ S = π(R × S) where common attributes equal
Theta Join: R ⋈_condition S = σ_condition(R × S)
Left Outer Join: R ⟕ S = (R ⋈ S) ∪ (R - π_R(R ⋈ S)) × (nulls)
Division: R ÷ S = {t | ∀s ∈ S: (t, s) ∈ R}
  (tuples in R that match ALL tuples in S on S's attributes)
```

### Functional Dependencies
```
Armstrong's Axioms:
  Reflexivity: If Y ⊆ X, then X → Y
  Augmentation: If X → Y, then XZ → YZ
  Transitivity: If X → Y and Y → Z, then X → Z

Derived Rules:
  Union: X → Y and X → Z → X → YZ
  Decomposition: X → YZ → X → Y and X → Z
  Pseudo-transitivity: X → Y and WY → Z → WX → Z

Closure of FD set F⁺: all FDs derivable from F
Closure of attribute set X⁺: all attributes determined by X under F

Candidate Key: minimal set of attributes whose closure = all attributes
```

### Normalization
```
1NF: All attributes are atomic (no composite/multi-valued attributes)

2NF: 1NF + No partial dependency
  (No non-prime attribute depends on part of any candidate key)

3NF: 2NF + No transitive dependency
  (No non-prime attribute transitively depends on any candidate key)
  Alternative: For every FD X → A, either X is superkey OR A is prime

BCNF: For every non-trivial FD X → A, X is a superkey
  (Stronger than 3NF — every determinant is a candidate key)

Decomposition:
  Lossless Join: R = R₁ ∪ R₂, R₁ ∩ R₂ → R₁ or R₁ ∩ R₂ → R₂
  Dependency Preserving: Union of projected FDs = original FD set
```

### SQL Patterns
```sql
-- Correlated Subquery
SELECT * FROM E e WHERE salary > (SELECT AVG(salary) FROM E WHERE dept = e.dept);

-- GROUP BY with HAVING
SELECT dept, COUNT(*) FROM E GROUP BY dept HAVING COUNT(*) > 5;

-- EXISTS
SELECT * FROM E e WHERE EXISTS (SELECT 1 FROM D d WHERE d.dept = e.dept);

-- Set Operations
(SELECT name FROM E) UNION (SELECT name FROM S);
(SELECT name FROM E) INTERSECT (SELECT name FROM S);
(SELECT name FROM E) EXCEPT (SELECT name FROM S);

-- VIEW
CREATE VIEW HighSalary AS SELECT * FROM E WHERE salary > 50000;

-- Aggregate Functions
SELECT dept, MAX(salary), AVG(salary) FROM E GROUP BY dept;
```

### B+ Tree
```
Properties:
  - All data in leaf nodes
  - Leaf nodes linked (for range queries)
  - Internal nodes: keys + child pointers
  - Every node has at least ⌈m/2⌉ children (except root)
  - Every node has at most m children
  - Every internal node has at most m-1 keys

Insertion: Split node if full
Deletion: Merge/borrow from siblings if underflow

Order m B+ tree:
  Max keys per node: m-1
  Min keys per node: ⌈m/2⌉ - 1 (except root)
  Max children: m
  Min children: ⌈m/2⌉ (except root)
```

### Transactions
```
ACID:
  Atomicity: all or nothing
  Consistency: valid state transitions
  Isolation: concurrent execution = serial
  Durability: committed changes persist

Schedule Properties:
  Conflict Serializability: precedence graph has no cycle
  View Serializability: same read/write sets as some serial schedule

2PL (Two-Phase Locking):
  Growing phase: acquire locks, no release
  Shrinking phase: release locks, no acquire
  Strict 2PL: release all locks at commit/abort (prevents cascading abort)
```

---

## Common Mistake Patterns

| Mistake | How to Avoid |
|---------|--------------|
| Wrong candidate key computation | Compute closure of all attribute subsets, find minimal ones |
| Partial dependency in 2NF | Check if non-prime attribute depends on PART of composite key |
| BCNF vs 3NF confusion | BCNF: every determinant is superkey; 3NF allows non-superkey determinants if prime |
| SQL GROUP BY errors | Non-aggregated columns must be in GROUP BY |
| Relational algebra division confusion | Division = "for all" — tuples matching ALL in S |
| ER to relational mapping errors | M:N relationships need separate table; 1:N can merge |
| Serializability graph errors | Draw edges for conflicting operations only (R-W, W-R, W-W on same data) |
| B+ tree insertion order matters | Always insert in given order, split as needed |
| Lossless decomposition verification | Check: intersection determines one of the decomposed relations |
| Aggregate function without GROUP BY | COUNT(*) without GROUP BY returns single row |

---

## PYQ Practice Strategy

### Phase 1: Normalization (Week 1–2)
- Solve 30 normalization PYQs
- Focus on finding keys, computing closures, checking normal forms

### Phase 2: SQL + Relational Algebra (Week 2–3)
- Solve 20 SQL query problems
- Solve 15 relational algebra problems

### Phase 3: Mixed Practice (Week 3–4)
- Solve 50 mixed DB PYQs in 70 minutes
- Focus on speed and accuracy

### Key PYQ Problem Types
1. Normalization — find keys, check 2NF/3NF/BCNF
2. SQL query output prediction
3. Relational algebra expression evaluation
4. ER diagram construction
5. Functional dependency closure
6. Serializability — conflict serializable or not?
7. B+ tree insertion/deletion

---

## Topic-Wise Time Estimates

| Topic | Study Time | Practice Time | Total |
|-------|------------|---------------|-------|
| ER Model | 3 hrs | 2 hrs | 5 hrs |
| Relational Algebra | 4 hrs | 3 hrs | 7 hrs |
| SQL | 4 hrs | 4 hrs | 8 hrs |
| Functional Dependencies | 3 hrs | 3 hrs | 6 hrs |
| Normalization | 5 hrs | 5 hrs | 10 hrs |
| Transactions & Concurrency | 4 hrs | 3 hrs | 7 hrs |
| Indexing & File Organization | 2 hrs | 1.5 hrs | 3.5 hrs |
| **Total** | **25 hrs** | **21.5 hrs** | **46.5 hrs** |

---

## Quick Revision Checklist

- [ ] Armstrong's axioms and derived rules
- [ ] Closure computation (attribute set and FD set)
- [ ] Candidate key identification
- [ ] 1NF → 2NF → 3NF → BCNF conditions
- [ ] Lossless join and dependency preserving decomposition
- [ ] All relational algebra operations
- [ ] SQL JOINs, subqueries, GROUP BY, HAVING
- [ ] B+ tree properties (order m)
- [ ] ACID properties
- [ ] Conflict serializability — precedence graph construction
- [ ] 2PL and Strict 2PL differences
