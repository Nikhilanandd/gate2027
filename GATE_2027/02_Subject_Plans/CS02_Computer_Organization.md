# CS02: Computer Organization & Architecture — GATE 2027 CSE Study Plan

## Overview

| Metric | Detail |
|--------|--------|
| **Expected Marks** | 4–6 (1–2 MCQs + 1–2 NAT/MSQ) |
| **Difficulty** | Hard |
| **Scoring Potential** | Medium — conceptual, requires practice |
| **Time Estimate** | 35–40 hours total |
| **Priority** | Medium-High |

---

## GATE 2027 Syllabus

1. **Instruction Set Architecture** — Instruction formats, addressing modes (immediate, direct, indirect, register, register indirect, indexed, auto-increment/decrement)
2. **Arithmetic** — Integer arithmetic (addition, subtraction, multiplication, division), ALU design (ripple carry, carry look-ahead, carry select adders, booth's multiplier)
3. **Control Unit** — Hardwired control unit, Microprogrammed control unit (control memory, microinstructions, sequencing)
4. **Memory Hierarchy** — Cache (direct, associative, set-associative mapping), cache coherence, replacement policies, write policies
5. **Pipelining** — Instruction pipeline, pipeline hazards (data, control, structural), hazard resolution techniques
6. **I/O Organization** - Interrupts (Vectored, Non-vectored), DMA, I/O mapped vs memory mapped I/O

> **GATE 2027 Update:** Hardwired vs microprogrammed control is now explicitly in scope. Cache memory mapping techniques are explicitly listed.

---

## PYQ Weightage Analysis (2017–2026)

| Topic | Avg. Questions/Year | Avg. Marks/Year | Trend |
|-------|---------------------|-----------------|-------|
| Instruction Set & Addressing | 1 | 1–2 | Stable |
| ALU & Arithmetic | 1 | 1–2 | Moderate |
| Control Unit | 0–1 | 0–2 | **Increasing (2027)** |
| Cache Memory | 1–2 | 2–3 | Stable, high value |
| Pipelining | 1 | 1–2 | Stable |
| I/O Organization | 0–1 | 0–1 | Declining |

**Most Common PYQ Patterns:**
- Cache hit/miss calculation (direct/associative mapping)
- Pipeline timing diagrams and speedup calculation
- Addressing mode identification from assembly code
- Cache performance with access time and hit ratio

---

## Topic-Wise Priority

| Topic | Priority | Why |
|-------|----------|-----|
| Cache Memory Hierarchy | **HIGH** | Highest frequency, formula-based |
| Pipelining (Hazards, Speedup) | **HIGH** | Frequently tested, moderate difficulty |
| Addressing Modes | **HIGH** | Easy to score, frequently in MCQs |
| ALU Design (Adders) | **MEDIUM** | Moderate frequency |
| Control Unit (Hardwired/Microprogrammed) | **MEDIUM** | **NEW in 2027** — expect questions |
| Booth's Multiplier | **LOW** | Rarely tested, complex |

---

## Recommended Resources

### Free YouTube
| Resource | Topics |
|----------|--------|
| **Neso Academy** — COA | Full syllabus — best for theory |
| **GO Classes** — COA | GATE-focused, PYQ solutions |
| **Gate Smashers** — COA | Quick revision |

### Books
| Book | Use |
|------|-----|
| **William Stallings — Computer Organization & Architecture** | Primary reference |
| **Morris Mano — Computer System Architecture** | Classic, good for ALU and control |
| **Hamacher — Computer Organization** | Indian university standard |

---

## Week-by-Week Study Plan (4 Weeks)

### Week 1: Instruction Set + Addressing Modes + ALU (10 hours)

| Day | Topic | Hours | Tasks |
|-----|-------|-------|-------|
| Day 1 | Instruction Formats | 2 | Read Stallings Ch. 8, practice instruction decoding |
| Day 2 | Addressing Modes | 2.5 | All modes with examples, solve 15 PYQs |
| Day 3 | Adders (Ripple Carry, CLA) | 3 | Watch Neso Academy, derive CLA equations |
| Day 4 | Booth's Multiplier + ALU | 2.5 | Learn algorithm, solve 5 numerical problems |

### Week 2: Cache Memory (10 hours)

| Day | Topic | Hours | Tasks |
|-----|-------|-------|-------|
| Day 1 | Cache Basics + Direct Mapping | 2.5 | Block size, tag/index/offset calculation |
| Day 2 | Associative Mapping | 2.5 | Fully associative, set-associative |
| Day 3 | Cache Performance | 2.5 | AMAT calculation, multi-level cache |
| Day 4 | Cache Practice | 2.5 | Solve 20 PYQs on cache mapping |

### Week 3: Pipelining + Control Unit (10 hours)

| Day | Topic | Hours | Tasks |
|-----|-------|-------|-------|
| Day 1 | Instruction Pipeline | 2.5 | Pipeline stages, speedup, efficiency |
| Day 2 | Pipeline Hazards | 3 | Data hazards (forwarding), control hazards (branch prediction) |
| Day 3 | Hardwired Control | 2 | Control signals, sequencing, timing |
| Day 4 | Microprogrammed Control | 2.5 | Control memory, microinstruction format, sequencing |

### Week 4: I/O + Revision (10 hours)

| Day | Topic | Hours | Tasks |
|-----|-------|-------|-------|
| Day 1 | Interrupts & DMA | 2 | Vectored vs non-vectored, DMA transfer |
| Day 2 | PYQ Marathon — Full Subject | 3 | Solve 40 mixed COA PYQs |
| Day 3 | Weak Area Revision | 2.5 | Focus on weakest 2 topics |
| Day 4 | Final Revision + Formula Review | 2.5 | Revise all formulas, re-solve error log |

---

## Key Formulas and Concepts to Master

### Cache Memory
```
Address = [Tag | Index | Block Offset]

Direct Mapping:
  Index = (Block Address) mod (Number of Cache Blocks)
  Tag = Block Address / Number of Cache Blocks

Set-Associative:
  Set Index = (Block Address) mod (Number of Sets)
  Tag = Block Address / Number of Sets

AMAT = Hit Time + Miss Rate × Miss Penalty
Multi-level AMAT = Hit Time₁ + MR₁ × (Hit Time₂ + MR₂ × Miss Penalty₂)

Cache Size = Number of Sets × Associativity × Block Size
```

### Pipelining
```
Speedup = Non-pipelined time / Pipelined time
Speedup (ideal) = Number of stages (k)
Actual Speedup = k / (1 + stall cycles per instruction)
Pipeline Efficiency = Speedup / k × 100%
CPI = 1 + (Pipeline stall cycles per instruction)

Number of cycles = (k + n - 1) × clock_cycle  (for n instructions, k stages)
```

### Adders
```
Ripple Carry Adder: Delay = O(n) — n full adders in series
Carry Look-Ahead: 
  Generate (G) = A AND B
  Propagate (P) = A XOR B
  C_i = G_i + P_i·C_{i-1}
  Delay = O(1) — constant time carry computation
```

### Booth's Algorithm
```
For multiplying A (multiplicand) × Q (multiplier):
  Q₋₁ = 0 (extra bit)
  
  If Q₀Q₋₁ = 01 → A = A + M (add multiplicand)
  If Q₀Q₋₁ = 10 → A = A - M (subtract multiplicand)
  If Q₀Q₋₁ = 00 or 11 → No operation
  
  Then arithmetic right shift {A, Q, Q₋₁}
  Repeat for n iterations (n = number of bits)
```

### Control Unit
```
Hardwired:
  - Uses combinational logic gates
  - Faster but inflexible
  - Changes require hardware modification

Microprogrammed:
  - Uses control memory (microcode)
  - Slower but flexible
  - Changes require microcode update
  - Microinstruction format: [Routine addr | Micro-op | Next addr | Conditions]
```

---

## Common Mistake Patterns

| Mistake | How to Avoid |
|---------|--------------|
| Wrong tag/index/offset bit calculation | Always verify: tag + index + offset = address bits |
| Confusing set-associative with fully associative | Set-associative: sets > 1, blocks per set = associativity |
| Pipeline hazard type misidentification | Data: RAW/WAR/WAW | Control: branch | Structural: resource conflict |
| Forgetting pipeline stall penalty | stalls = branch penalty × branch frequency |
| Booth's algorithm sign extension | Always extend A and M to n+1 bits before starting |
| Wrong addressing mode in assembly | Trace the effective address computation step by step |
| Cache replacement policy errors | LRU tracks access history; FIFO uses queue; Random uses counter |

---

## PYQ Practice Strategy

### Phase 1: Topic-wise
- Cache problems first (highest ROI)
- Then pipelining + addressing modes
- Then ALU and control unit

### Phase 2: Mixed Practice
- Solve 40 mixed COA PYQs in 60 minutes
- Focus on numerical problems (NATs)

### Phase 3: Revision
- Focus on cache and pipeline numericals
- Revise addressing mode definitions

### Key PYQ Problem Types
1. Cache hit/miss rate calculation
2. AMAT computation for multi-level cache
3. Pipeline timing diagram with stalls
4. Speedup calculation for pipeline vs non-pipeline
5. Addressing mode identification from code
6. Number of clock cycles for instruction execution

---

## Topic-Wise Time Estimates

| Topic | Study Time | Practice Time | Total |
|-------|------------|---------------|-------|
| Instruction Set & Addressing | 4 hrs | 3 hrs | 7 hrs |
| ALU & Arithmetic | 4 hrs | 3 hrs | 7 hrs |
| Cache Memory | 6 hrs | 5 hrs | 11 hrs |
| Pipelining | 5 hrs | 4 hrs | 9 hrs |
| Control Unit | 4 hrs | 2 hrs | 6 hrs |
| I/O Organization | 2 hrs | 1.5 hrs | 3.5 hrs |
| **Total** | **25 hrs** | **18.5 hrs** | **43.5 hrs** |

---

## Quick Revision Checklist

- [ ] All addressing modes with examples
- [ ] Direct/associative/set-associative cache mapping
- [ ] AMAT formula for single and multi-level cache
- [ ] Pipeline speedup and efficiency formulas
- [ ] Data hazards and forwarding solution
- [ ] Control hazards and branch prediction
- [ ] Hardwired vs microprogrammed control differences
- [ ] Booth's algorithm steps
- [ ] Ripple carry vs carry look-ahead adder
- [ ] DMA vs interrupt-driven I/O
