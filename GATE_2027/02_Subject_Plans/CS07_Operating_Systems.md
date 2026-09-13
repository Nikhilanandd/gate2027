# CS07: Operating Systems — GATE 2027 CSE Study Plan

## Overview

| Metric | Detail |
|--------|--------|
| **Expected Marks** | 8–10 (2–3 MCQs + 2–3 NAT/MSQ) |
| **Difficulty** | Moderate |
| **Scoring Potential** | **Very High** — second highest weightage subject |
| **Time Estimate** | 40–45 hours total |
| **Priority** | **HIGHEST** — must master this subject |

---

## GATE 2027 Syllabus

### Process Management
1. **System Calls** — Types, fork(), exec(), wait(), process creation
2. **Processes** — Process states, process control block (PCB), process scheduling (FCFS, SJF, SRTF, Round Robin, Priority, Multilevel Queue), scheduling criteria
3. **Threads** — User-level vs kernel-level threads, multithreading models
4. **Interprocess Communication (IPC)** — Shared memory, message passing, pipes, semaphores
5. **Concurrency** — Race conditions, critical section, mutex locks, semaphores (binary, counting), monitors, peterson's solution, deadlock (prevention, avoidance, detection, recovery)
6. **Synchronization** — Producer-consumer, readers-writers, dining philosophers

### Memory Management
7. **Memory Management** — Contiguous allocation, fixed/partitioning, variable partitioning, fragmentation (internal/external), paging, segmentation, page table
8. **Virtual Memory** — Demand paging, page replacement algorithms (FIFO, LRU, Optimal, LFU), page fault handling, thrashing, working set model

### Storage Management
9. **I/O Systems** — I/O hardware, programmed I/O, interrupt-driven I/O, DMA
10. **File Systems** — File organization, directory structure, allocation methods (contiguous, linked, indexed), free space management, disk scheduling (FCFS, SSTF, SCAN, C-SCAN, LOOK, C-LOOK)

---

## PYQ Weightage Analysis (2017–2026)

| Topic | Avg. Questions/Year | Avg. Marks/Year | Trend |
|-------|---------------------|-----------------|-------|
| Process Scheduling | 1–2 | 2–3 | Stable, **very common** |
| Deadlock | 1–2 | 2–3 | Stable |
| Memory Management (Paging) | 1–2 | 2–3 | Stable, **very common** |
| Virtual Memory (Page Replacement) | 1–2 | 2–3 | Stable |
| Synchronization (Semaphores) | 1 | 1–2 | Increasing |
| File Systems / Disk Scheduling | 0–1 | 0–1 | Moderate |

**Most Common PYQ Patterns:**
- CPU scheduling Gantt chart and average waiting/turnaround time
- Page replacement algorithm trace (FIFO, LRU, Optimal)
- Address translation with paging (page number, offset)
- Deadlock detection (resource allocation graph)
- Semaphore-based synchronization output
- Effective access time calculation
- Belady's anomaly identification

---

## Topic-Wise Priority

| Topic | Priority | Why |
|-------|----------|-----|
| Process Scheduling | **HIGHEST** | 2–3 marks guaranteed, numerical |
| Virtual Memory (Page Replacement) | **HIGHEST** | Always tested, numerical |
| Paging & Address Translation | **HIGH** | Very frequent, formula-based |
| Deadlock | **HIGH** | High frequency, conceptual |
| Synchronization (Semaphores) | **HIGH** | Increasing frequency |
| File Systems / Disk Scheduling | **MEDIUM** | Moderate frequency |
| Threads / IPC | **LOW** | Rarely tested directly |

---

## Recommended Resources

### Free YouTube
| Resource | Topics |
|----------|--------|
| **Knowledge Gate (Sanchit Jain)** — OS | Best for GATE — exhaustive |
| **Neso Academy** — OS | Good theory explanations |
| **Gate Smashers** — OS | Quick revision |
| ** Jenny's Lectures** — OS | Alternate explanations |

### Books
| Book | Use |
|------|-----|
| **Silberschatz, Galvin, Gagne — Operating System Concepts** | Gold standard (Dinosaur book) |
| **Stallings — Operating Systems** | Good for numerical problems |
| **Galvin — Operating System Concepts (Indian Edition)** | More affordable |

---

## Week-by-Week Study Plan (4.5 Weeks)

### Week 1: Process Management + Scheduling (10 hours)

| Day | Topic | Hours | Tasks |
|-----|-------|-------|-------|
| Day 1 | Processes + System Calls | 2.5 | Process states, fork/exec/wait, PCB |
| Day 2 | CPU Scheduling Algorithms | 3 | FCFS, SJF, SRTF, RR, Priority — trace all |
| Day 3 | Scheduling Numericals | 2.5 | Calculate avg waiting time, turnaround time — solve 15 problems |
| Day 4 | Threads + IPC | 2 | User vs kernel threads, shared memory, message passing |

### Week 2: Concurrency + Deadlock (10 hours)

| Day | Topic | Hours | Tasks |
|-----|-------|-------|-------|
| Day 1 | Critical Section + Mutex | 2.5 | Peterson's solution, mutex locks |
| Day 2 | Semaphores | 3 | Binary/counting semaphores, solve 10 synchronization problems |
| Day 3 | Deadlock (Conditions + Prevention) | 2.5 | 4 conditions, prevention strategies |
| Day 4 | Deadlock (Avoidance + Detection) | 2 | Banker's algorithm, RAG, deadlock detection |

### Week 3: Memory Management + Virtual Memory (10 hours)

| Day | Topic | Hours | Tasks |
|-----|-------|-------|-------|
| Day 1 | Paging | 2.5 | Page table, address translation, multi-level paging |
| Day 2 | Segmentation + Segmentation/Paging | 2 | Segmentation, combined schemes |
| Day 3 | Page Replacement Algorithms | 3.5 | FIFO, LRU, Optimal, LFU — trace all, solve 15 problems |
| Day 4 | Virtual Memory Concepts | 2 | Page fault handling, thrashing, working set |

### Week 4: Disk Scheduling + File Systems + Revision (10 hours)

| Day | Topic | Hours | Tasks |
|-----|-------|-------|-------|
| Day 1 | Disk Scheduling | 2.5 | FCFS, SSTF, SCAN, C-SCAN, LOOK, C-LOOK |
| Day 2 | File Systems | 2 | Allocation methods, free space management |
| Day 3 | PYQ Marathon — Full Subject | 3 | Solve 50 mixed OS PYQs |
| Day 4 | Final Revision | 2.5 | Revisit all formulas, re-solve error log |

### Week 4.5: Final Touch (5 hours)

| Day | Topic | Hours | Tasks |
|-----|-------|-------|-------|
| Day 1 | Weak Area Deep Dive | 3 | Focus on 2 weakest topics |
| Day 2 | Speed Practice | 2 | Solve 20 OS questions in 25 minutes |

---

## Key Formulas and Concepts to Master

### CPU Scheduling
```
Turnaround Time (TAT) = Completion Time - Arrival Time
Waiting Time (WT) = TAT - Burst Time
Response Time (RT) = First Response Time - Arrival Time

Average TAT = Σ TAT / n
Average WT = Σ WT / n

RR Time Quantum (q):
  If process needs ≤ q: completes in one round
  If process needs > q: preempted, goes to back of queue
  Number of round trips = ceil(Burst / q)
```

### Page Replacement Algorithms
```
FIFO: Replace oldest page
  - Belady's anomaly: more frames → more page faults (possible)
  - Simple to implement

LRU: Replace least recently used page
  - No Belady's anomaly
  - Implementation: counter or stack
  - Approximation: Second chance (clock algorithm)

Optimal: Replace page not used for longest time
  - Minimum page faults (benchmark)
  - Not implementable (needs future knowledge)

Page Fault Rate = Page Faults / Total Accesses
Effective Access Time (EAT) = (1-p) × memory_access + p × page_fault_time
```

### Paging
```
Logical Address = Page Number + Page Offset
Physical Address = Frame Number + Page Offset

Number of Pages = Logical Address Space / Page Size
Number of Frames = Physical Address Space / Page Size

Page Table Entry (PTE):
  [Page # | Frame # | Valid/Invalid | Dirty | Reference | Protection]

Page Table Size = Number of Pages × PTE Size

Multi-level Paging:
  Outer page table → Inner page table → Physical frame
  Reduces page table size for large address spaces

TLB (Translation Lookaside Buffer):
  TLB Hit: Physical address from TLB
  TLB Miss: Check page table, update TLB
  Effective access = hit_ratio × TLB_time + (1 - hit_ratio) × (TLB_time + memory_time)
```

### Deadlock
```
Four Necessary Conditions (Coffman):
  1. Mutual Exclusion: resource held exclusively
  2. Hold and Wait: process holds resource while waiting
  3. No Preemption: resources cannot be forcibly taken
  4. Circular Wait: circular chain of processes waiting

Banker's Algorithm (Avoidance):
  For each process: Max, Allocation, Need = Max - Allocation
  Available = Total - Σ Allocation
  
  Safe state: exists sequence <P₁, P₂, ..., Pₙ> such that:
    Need_i ≤ Available for all i (in order)
    Available += Allocation_i after each process completes
  
  If safe → grant request; If unsafe → deny/defer

Deadlock Detection:
  Resource Allocation Graph (RAG):
    Request edge: Pi → Rj (process requests resource)
    Assignment edge: Rj → Pi (resource assigned to process)
    If cycle exists AND resource has single instance → deadlock
    If multiple instances → use detection algorithm (similar to Banker's)
```

### Synchronization
```
Semaphore: integer variable accessed via wait() and P() and signal() and V()

Binary Semaphore (mutex): 0 or 1
Counting Semaphore: 0 to N (where N = number of resources)

Producer-Consumer with Semaphores:
  semaphore mutex = 1;
  semaphore empty = n;  // slots available
  semaphore full = 0;   // items available
  
  Producer:
    wait(empty);
    wait(mutex);
    // produce item, add to buffer
    signal(mutex);
    signal(full);
  
  Consumer:
    wait(full);
    wait(mutex);
    // remove item from buffer, consume
    signal(mutex);
    signal(empty);

Readers-Writers:
  semaphore rw_mutex = 1;
  semaphore mutex = 1;
  int read_count = 0;
  
  Writer:
    wait(rw_mutex);
    // write
    signal(rw_mutex);
  
  Reader:
    wait(mutex);
    read_count++;
    if (read_count == 1) wait(rw_mutex);
    signal(mutex);
    // read
    wait(mutex);
    read_count--;
    if (read_count == 0) signal(rw_mutex);
    signal(mutex);
```

### Disk Scheduling
```
FCFS: First Come First Serve — simple but high seek time
SSTF: Shortest Seek Time First — minimize seek, may starve
SCAN: Elevator algorithm — go to end, reverse, may miss edges
C-SCAN: Circular SCAN — jump to start after reaching end
LOOK: Like SCAN but don't go to end
C-LOOK: Like C-SCAN but don't go to end

Total Seek Time = Σ |current_track - next_track| for all requests
```

---

## Common Mistake Patterns

| Mistake | How to Avoid |
|---------|--------------|
| Wrong arrival/burst time in scheduling | Always draw complete Gantt chart first |
| Confusing turnaround time with waiting time | TAT = completion - arrival; WT = TAT - burst |
| FIFO page replacement error | Track which page entered first, not which is oldest |
| LRU implementation confusion | Use stack (most recent at top) or counter timestamps |
| Belady's anomaly wrong attribution | Only FIFO has Belady's anomaly; LRU and Optimal don't |
| Page table size calculation | Remember: page table size ≠ address space size |
| Banker's safety algorithm error | Always check Need ≤ Available, then add Allocation |
| Semaphore deadlock (wrong order) | Always acquire mutex AFTER data semaphore |
| Disk scheduling total seek miscalculation | Track current head position at each step |
| Virtual memory: valid/invalid bit confusion | Valid = page in memory; Invalid = page on disk |

---

## PYQ Practice Strategy

### Phase 1: Scheduling + Paging (Week 1–2)
- Solve 25 PYQs on CPU scheduling
- Solve 20 PYQs on paging and address translation

### Phase 2: Deadlock + Synchronization (Week 2–3)
- Solve 20 PYQs on deadlock (Banker's, detection)
- Solve 15 semaphore problems

### Phase 3: Virtual Memory + Mixed (Week 3–4)
- Solve 20 PYQs on page replacement algorithms
- Mixed: 50 questions in 70 minutes

### Key PYQ Problem Types
1. CPU scheduling — Gantt chart and averages
2. Page replacement — trace with given reference string
3. Address translation — page/offset calculation
4. Banker's algorithm — safety check and resource request
5. Semaphore — output prediction
6. Effective access time calculation
7. Disk scheduling — total seek time

---

## Topic-Wise Time Estimates

| Topic | Study Time | Practice Time | Total |
|-------|------------|---------------|-------|
| Processes & System Calls | 3 hrs | 2 hrs | 5 hrs |
| CPU Scheduling | 5 hrs | 4 hrs | 9 hrs |
| Threads & IPC | 2 hrs | 1.5 hrs | 3.5 hrs |
| Concurrency & Synchronization | 5 hrs | 4 hrs | 9 hrs |
| Deadlock | 4 hrs | 3 hrs | 7 hrs |
| Paging & Address Translation | 4 hrs | 3 hrs | 7 hrs |
| Virtual Memory (Page Replacement) | 4 hrs | 4 hrs | 8 hrs |
| Disk Scheduling & File Systems | 3 hrs | 2 hrs | 5 hrs |
| **Total** | **30 hrs** | **23.5 hrs** | **53.5 hrs** |

---

## Quick Revision Checklist

- [ ] FCFS, SJF, SRTF, RR, Priority scheduling rules
- [ ] Turnaround time and waiting time formulas
- [ ] Four conditions for deadlock
- [ ] Banker's algorithm safety check procedure
- [ ] FIFO, LRU, Optimal — trace and identify Belady's anomaly
- [ ] Page table address translation
- [ ] Effective access time formula with TLB
- [ ] Semaphore code for producer-consumer
- [ ] Disk scheduling algorithms — seek time calculation
- [ ] Binary vs counting semaphore difference
