# CS04: Algorithms — GATE 2027 CSE Study Plan

## Overview

| Metric | Detail |
|--------|--------|
| **Expected Marks** | 7–9 (2–3 MCQs + 1–2 NAT/MSQ) |
| **Difficulty** | Moderate-Hard |
| **Scoring Potential** | High — formulaic with practice |
| **Time Estimate** | 40–45 hours total |
| **Priority** | **HIGH** |

---

## GATE 2027 Syllabus

### Analysis of Algorithms
1. **Asymptotic Complexity** — Big-O, Big-Ω, Big-Θ, Little-o, Little-ω
2. **Recurrences** — Substitution method, Master theorem, Recursion tree
3. **Amortized Analysis** — Aggregate, accounting, potential methods

### Algorithm Design Techniques
4. **Greedy Algorithms** — Activity selection, Huffman coding, Kruskal's, Prim's, Dijkstra's
5. **Divide and Conquer** — Merge sort, quick sort, binary search, Strassen's matrix multiplication
6. **Dynamic Programming** — Optimal substructure, overlapping subproblems, memoization, tabulation
7. **Backtracking** — N-Queens, subset sum, graph coloring
8. **Branch and Bound** — Travelling salesman, assignment problem

### Graph Algorithms
9. **Graph Traversals** — BFS, DFS, applications (topological sort, connected components, cycle detection)
10. **Minimum Spanning Tree** — Kruskal's, Prim's (with priority queue)
11. **Shortest Paths** — Dijkstra's, Bellman-Ford, Floyd-Warshall
12. **Network Flow** — Ford-Fulkerson, Max-flow min-cut theorem

### Sorting & Searching
13. **Comparison Sorts** — Merge sort, quick sort, heap sort, insertion sort, bubble sort, selection sort
14. **Linear Time Sorts** — Counting sort, radix sort, bucket sort
15. **Searching** — Binary search, linear search, interpolation search

### Hashing
16. **Hash Functions** — Division method, multiplication method
17. **Collision Resolution** — Chaining, open addressing (linear probing, quadratic probing, double hashing)
18. **Universal Hashing**

---

## PYQ Weightage Analysis (2017–2026)

| Topic | Avg. Questions/Year | Avg. Marks/Year | Trend |
|-------|---------------------|-----------------|-------|
| Asymptotic Complexity | 1–2 | 2–3 | Stable |
| Dynamic Programming | 1–2 | 2–3 | Increasing |
| Graph Algorithms | 1–2 | 2–3 | Stable |
| Sorting Algorithms | 1 | 1–2 | Stable |
| Recurrences | 0–1 | 1–2 | Stable |
| Greedy Algorithms | 1 | 1–2 | Moderate |
| Hashing | 0–1 | 0–1 | Declining |

**Most Common PYQ Patterns:**
- Asymptotic complexity comparison (which is larger/smaller)
- Recurrence relation solving (Master theorem)
- DP problem identification and recurrence
- Dijkstra's / Bellman-Ford shortest path numerical
- Sorting algorithm comparison (stability, time, space)
- MST construction numerical

---

## Topic-Wise Priority

| Topic | Priority | Why |
|-------|----------|-----|
| Asymptotic Complexity & Recurrences | **HIGHEST** | 2–3 marks guaranteed, formula-based |
| Dynamic Programming | **HIGH** | High frequency, moderate difficulty |
| Graph Algorithms (BFS/DFS/Dijkstra/Bellman-Ford) | **HIGH** | Always tested, numerical |
| Sorting Algorithms | **HIGH** | Frequently tested, comparison-based |
| Greedy Algorithms | **MEDIUM** | Moderate frequency, tricky to prove |
| Hashing | **MEDIUM** | Occasionally tested |
| Network Flow | **LOW** | Rarely tested |
| Backtracking / Branch & Bound | **LOW** | Rarely tested |

---

## Recommended Resources

### Free YouTube
| Resource | Topics |
|----------|--------|
| **Abdul Bari** — Algorithms | Full syllabus — absolute legend for GATE |
| **MIT OCW 6.006** | Deep theory, good for understanding |
| **Gate Smashers** — Algorithms | Quick revision |

### Books
| Book | Use |
|------|-----|
| **CLRS — Introduction to Algorithms** | Gold standard reference |
| **Kleinberg & Tardos — Algorithm Design** | Best for design paradigm intuition |
| **Cormen (Indian Edition)** | More affordable CLRS |

### Practice
- Abdul Bari's problems (watch and solve along)
- GeeksforGeeks Algorithms section
- LeetCode Medium problems (Algorithm category)
- PYQ compilations on GO portal

---

## Week-by-Week Study Plan (4 Weeks)

### Week 1: Complexity Analysis + Recurrences + Sorting (10 hours)

| Day | Topic | Hours | Tasks |
|-----|-------|-------|-------|
| Day 1 | Asymptotic Notations | 2.5 | Big-O, Ω, Θ definitions, practice 20 comparison problems |
| Day 2 | Recurrences | 3 | Master theorem, substitution, recursion tree — solve 15 problems |
| Day 3 | Comparison Sorts | 2.5 | Merge sort, quick sort, heap sort — analyze all complexities |
| Day 4 | Linear Sorts + Sorting Practice | 2 | Counting, radix, bucket sort; solve 15 sorting PYQs |

### Week 2: Greedy + Dynamic Programming (10 hours)

| Day | Topic | Hours | Tasks |
|-----|-------|-------|-------|
| Day 1 | Greedy Algorithms | 2.5 | Activity selection, Huffman, fractional knapsack |
| Day 2 | DP Fundamentals | 3 | Optimal substructure, overlapping subproblems, 0/1 knapsack |
| Day 3 | DP on Strings | 2.5 | LCS, edit distance — solve 10 problems |
| Day 4 | DP on Graphs + Trees | 2 | Matrix chain multiplication, tree DP |

### Week 3: Graph Algorithms (10 hours)

| Day | Topic | Hours | Tasks |
|-----|-------|-------|-------|
| Day 1 | BFS + DFS | 2.5 | Traversals, applications (topological sort, cycle detection) |
| Day 2 | MST (Kruskal + Prim) | 2.5 | Both algorithms, union-find |
| Day 3 | Shortest Paths (Dijkstra + Bellman-Ford) | 3 | Both algorithms with numerical problems |
| Day 4 | Floyd-Warshall + Graph Practice | 2 | All-pairs shortest path, solve 15 graph PYQs |

### Week 4: Hashing + Revision (10 hours)

| Day | Topic | Hours | Tasks |
|-----|-------|-------|-------|
| Day 1 | Hashing | 2.5 | Hash functions, collision resolution, expected time |
| Day 2 | PYQ Marathon — Full Subject | 3 | Solve 40 mixed Algorithms PYQs |
| Day 3 | Weak Areas Revision | 2.5 | Focus on weakest 2 topics |
| Day 4 | Final Revision | 2 | Revisit formulas, re-solve error log problems |

---

## Key Formulas and Concepts to Master

### Asymptotic Complexity
```
Big-O:   f(n) = O(g(n)) iff ∃ c, n₀: f(n) ≤ c·g(n) for all n ≥ n₀
Big-Ω:   f(n) = Ω(g(n)) iff ∃ c, n₀: f(n) ≥ c·g(n) for all n ≥ n₀
Big-Θ:   f(n) = Θ(g(n)) iff f(n) = O(g(n)) AND f(n) = Ω(g(n))

Common complexities: O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(n³) < O(2ⁿ) < O(n!)

Rules:
- Drop constants: O(2n) = O(n)
- Drop lower order: O(n² + n) = O(n²)
- Multiplication: O(f(n)) × O(g(n)) = O(f(n) × g(n))
- Log properties: log_a(n) = Θ(log_b(n)) for any a, b > 1
```

### Master Theorem
```
T(n) = aT(n/b) + Θ(n^d)

Compare log_b(a) with d:
  Case 1: d < log_b(a)  → T(n) = Θ(n^{log_b(a)})
  Case 2: d = log_b(a)  → T(n) = Θ(n^d × log n)
  Case 3: d > log_b(a)  → T(n) = Θ(n^d)

Examples:
  Merge sort: T(n) = 2T(n/2) + Θ(n) → a=2, b=2, d=1
    log₂(2) = 1 = d → Case 2 → Θ(n log n)

  Binary search: T(n) = T(n/2) + Θ(1) → a=1, b=2, d=0
    log₂(1) = 0 = d → Case 2 → Θ(log n)
```

### Sorting Algorithm Comparison
```
Algorithm    | Best    | Average    | Worst    | Space  | Stable
-------------|---------|------------|----------|--------|-------
Merge Sort   | n log n | n log n    | n log n  | O(n)   | Yes
Quick Sort   | n log n | n log n    | n²       | O(log n)| No
Heap Sort    | n log n | n log n    | n log n  | O(1)   | No
Insertion    | n       | n²         | n²       | O(1)   | Yes
Bubble       | n       | n²         | n²       | O(1)   | Yes
Selection    | n²      | n²         | n²       | O(1)   | No
Counting     | n+k     | n+k        | n+k      | O(k)   | Yes
Radix        | dn+k    | dn+k       | dn+k     | O(n+k) | Yes

d = number of digits, k = range of input
```

### Graph Algorithms
```
BFS: O(V + E) — uses queue, finds shortest path in unweighted graph
DFS: O(V + E) — uses stack/recursion, finds connected components, topological sort

Dijkstra's: O((V + E) log V) with min-heap — no negative weights
Bellman-Ford: O(V × E) — handles negative weights, detects negative cycles
Floyd-Warshall: O(V³) — all-pairs shortest path

Kruskal's MST: O(E log E) — uses union-find
Prim's MST: O((V + E) log V) with min-heap — starts from a vertex

Topological Sort: O(V + E) — DAG only, using DFS or Kahn's (BFS) algorithm
```

### Dynamic Programming
```
Steps to solve DP:
1. Identify optimal substructure
2. Define state (what does dp[i] or dp[i][j] represent?)
3. Write recurrence relation
4. Determine base cases
5. Determine computation order (bottom-up)
6. Extract solution if needed

Common DP patterns:
- Linear DP: dp[i] depends on dp[i-1], dp[i-2]
- 2D DP: dp[i][j] depends on dp[i-1][j], dp[i][j-1], dp[i-1][j-1]
- Knapsack: dp[i][w] = max(dp[i-1][w], dp[i-1][w-wt[i]] + val[i])
- LIS: dp[i] = length of LIS ending at index i
- LCS: dp[i][j] = LCS of s1[0..i-1] and s2[0..j-1]
```

### Hashing
```
Hash Function: h(k) = k mod m (division method)
h(k) = ⌊m × (kA mod 1)⌋ (multiplication, A ≈ (√5-1)/2)

Collision Resolution:
  Chaining: Expected O(1 + α) where α = n/m (load factor)
  Linear Probing: Expected O(1/(1-α)) for α < 1
  Quadratic Probing: Better distribution than linear
  Double Hashing: h₁(k) + i·h₂(k) mod m

Success factor = 1/(1-α) for successful search (open addressing)
```

---

## Common Mistake Patterns

| Mistake | How to Avoid |
|---------|--------------|
| Wrong Master theorem case identification | Compare d with log_b(a) carefully |
| Confusing stable and unstable sorts | Merge/Insertion/Bubble = stable; Quick/Heap/Selection = unstable |
| Forgetting Dijkstra doesn't work with negative weights | Use Bellman-Ford for negative weights |
| Wrong DP state definition | State must capture all necessary information |
| DFS vs BFS application confusion | BFS for shortest path in unweighted; DFS for topological sort |
| MST edge weight miscalculation | Re-check Kruskal's sorted order and Prim's priority queue |
| Incorrect amortized analysis | Account for all operations, not just worst-case individual |
| Hash function distribution error | Choose m as prime, avoid clustering patterns |
| Recurrence base case omission | Always verify base case and its value |
| Confusing O(n) with Θ(n) | O is upper bound, Θ is tight bound |

---

## PYQ Practice Strategy

### Phase 1: Complexity Analysis (Week 1)
- Solve 30 asymptotic complexity PYQs
- Practice recurrence solving with Master theorem

### Phase 2: Algorithm Design (Week 2–3)
- Solve PYQs topic-wise: Greedy → DP → Graphs
- Focus on identifying which paradigm to apply

### Phase 3: Mixed Practice (Week 4)
- Solve 40 mixed Algorithms PYQs in 60 minutes
- Focus on speed + accuracy

### Key PYQ Problem Types
1. Asymptotic complexity comparison
2. Recurrence solving
3. Sorting algorithm identification (given properties)
4. Dijkstra's/Bellman-Ford numerical
5. MST construction
6. DP problem formulation
7. BFS/DFS traversal output

---

## Topic-Wise Time Estimates

| Topic | Study Time | Practice Time | Total |
|-------|------------|---------------|-------|
| Asymptotic Complexity | 3 hrs | 3 hrs | 6 hrs |
| Recurrences | 3 hrs | 3 hrs | 6 hrs |
| Sorting Algorithms | 4 hrs | 3 hrs | 7 hrs |
| Greedy Algorithms | 3 hrs | 3 hrs | 6 hrs |
| Dynamic Programming | 6 hrs | 5 hrs | 11 hrs |
| Graph Algorithms | 6 hrs | 5 hrs | 11 hrs |
| Hashing | 2 hrs | 1.5 hrs | 3.5 hrs |
| **Total** | **27 hrs** | **23.5 hrs** | **50.5 hrs** |

---

## Quick Revision Checklist

- [ ] Master theorem — all three cases with examples
- [ ] Sorting algorithms — time, space, stability for all
- [ ] Dijkstra's algorithm steps and complexity
- [ ] Bellman-Ford — when to use, negative cycle detection
- [ ] Kruskal's and Prim's — both MST algorithms
- [ ] BFS and DFS — applications and differences
- [ ] DP steps: state → recurrence → base case → computation
- [ ] Common DP patterns (knapsack, LIS, LCS, MCM)
- [ ] Hash function properties and collision resolution
- [ ] Topological sort — both DFS and Kahn's approaches
