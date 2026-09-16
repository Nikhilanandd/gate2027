#!/usr/bin/env python3
"""Generate curated GATE CSE-style questions in Moodle GIFT format.

All answers are computed programmatically where possible, so they are correct by
construction. Output: GATE_2027/06_PYQ_Papers/GATE_CSE_CURATED.gift
"""
import heapq
import math
import random
import re
import sys
from collections import Counter, deque

random.seed(2027)

OUT = '/home/nikhil/Documents/GATE/GATE_2027/06_PYQ_Papers/GATE_CSE_CURATED.gift'

Q = []
COUNTERS = Counter()


def esc(s):
    s = str(s).replace('\\', '\\\\')
    for ch in ('~', '=', '#', '{', '}', ':'):
        s = s.replace(ch, '\\' + ch)
    return s


def mcq(subj, text, correct, wrongs, src):
    correct = str(correct)
    uniq = []
    for w in wrongs:
        w = str(w)
        if w != correct and w not in uniq:
            uniq.append(w)
    assert len(uniq) >= 3, f'{subj}: only {len(uniq)} unique wrongs for: {text[:60]}'
    opts = [(correct, True)] + [(w, False) for w in uniq[:3]]
    random.shuffle(opts)
    Q.append(dict(subj=subj, type='mcq', text=text, opts=opts, src=src))
    COUNTERS[subj] += 1


def msq(subj, text, corrects, wrongs, src):
    cs, ws = [], []
    for c in corrects:
        c = str(c)
        if c not in cs:
            cs.append(c)
    for w in wrongs:
        w = str(w)
        if w not in cs and w not in ws:
            ws.append(w)
    assert len(cs) >= 2 and len(ws) >= 1, f'{subj}: bad MSQ: {text[:60]}'
    opts = [(c, True) for c in cs] + [(w, False) for w in ws]
    random.shuffle(opts)
    Q.append(dict(subj=subj, type='msq', text=text, opts=opts, src=src))
    COUNTERS[subj] += 1


def nat(subj, text, answer, src):
    Q.append(dict(subj=subj, type='nat', text=text, answer=str(answer), src=src))
    COUNTERS[subj] += 1


# ============================ Digital Logic (31) ============================
DL = 'Digital Logic'
S = 'Curated - Number Systems'

for n in [45, 173, 200, 110, 254]:
    nat(DL, f'The decimal equivalent of the binary number ({bin(n)[2:]})2 is ________.', n, S)
for n in [100, 255, 128]:
    nat(DL, f'The number of 1s in the 8-bit binary representation of the decimal number {n} is ________.',
        bin(n).count('1'), S)
for h, v in [('2F', 0x2F), ('AB', 0xAB), ('FF', 0xFF)]:
    nat(DL, f'The decimal equivalent of the hexadecimal number ({h})16 is ________.', v, S)

S = 'Curated - Data Representation'
nat(DL, 'The minimum (most negative) value representable in 8-bit 2\'s complement notation is ________.', -128, S)
nat(DL, 'The maximum (most positive) value representable in 8-bit 2\'s complement notation is ________.', 127, S)

S = 'Curated - Combinational Circuits'
for ratio, lines in [('8:1', 3), ('16:1', 4), ('32:1', 5)]:
    nat(DL, f'The number of select lines required for a {ratio} multiplexer is ________.', lines, S)
nat(DL, 'A 3-to-8 decoder has ________ output lines.', 8, S)
nat(DL, 'A 4-to-16 decoder has ________ output lines.', 16, S)


def bool_eval(expr, env):
    return int(eval(expr, {}, env))


for expr, env in [("(not A) and B or A and (not B)", {'A': 1, 'B': 0, 'C': 0}),
                  ("A and B or C", {'A': 1, 'B': 1, 'C': 0}),
                  ("(A or (not B)) and ((not A) or C)", {'A': 0, 'B': 0, 'C': 0})]:
    v = bool_eval(expr, env)
    nat(DL, f'For the Boolean function f = {expr} (where \'not\' denotes complement, \'and\' denotes AND, \'or\' denotes OR), '
            f'the value of f when A = {env["A"]}, B = {env["B"]}, C = {env["C"]} is ________.', v, S)

for desc, cnt in [('f = A + BC', sum(1 for a in (0, 1) for b in (0, 1) for c in (0, 1) if a or (b and c))),
                  ("f = AB + A'C", sum(1 for a in (0, 1) for b in (0, 1) for c in (0, 1) if (a and b) or ((not a) and c)))]:
    nat(DL, f'The number of minterms in the canonical sum-of-products form of the 3-variable Boolean function {desc} is ________.',
        cnt, S)

nat(DL, 'The 4-bit Gray code equivalent of the binary number 1011 is ________ (enter the 4-bit binary pattern).',
    '1110', S)
nat(DL, 'The minimum number of 2-input NAND gates required to implement a 2-input XOR gate is ________.', 4, S)
nat(DL, 'The minimum number of 2-input NAND gates required to implement a 2-input XNOR gate is ________.', 5, S)
mcq(DL, 'The Boolean expression for the SUM output of a half adder with inputs A and B is',
    'A XOR B', ['A AND B', 'A OR B', 'NOT (A AND B)'], 'Curated - Combinational Circuits')

S = 'Curated - Sequential Circuits'
for mod, ff in [(6, 3), (10, 4), (12, 4)]:
    nat(DL, f'The minimum number of flip-flops required to design a mod-{mod} counter is ________.', ff, S)
msq(DL, 'Which of the following are universal gates?',
    ['NAND', 'NOR'], ['AND', 'XOR'], 'Curated - Boolean Algebra')
nat(DL, 'A JK flip-flop with J = 1 and K = 1 and current state Q = 0 will have the next state Q(next) = ________.', 1, S)

# ======================= Computer Organization (14) ========================
COA = 'Computer Organization'
S = 'Curated - Memory Hierarchy'

nat(COA, 'A direct-mapped cache has a block size of 64 bytes. The number of bits used for the block offset is ________.',
    int(math.log2(64)), S)
nat(COA, 'A direct-mapped cache has 256 lines. The number of bits used for the index is ________.',
    int(math.log2(256)), S)
tag = 32 - int(math.log2(32)) - int(math.log2(16 * 1024 // 32))
nat(COA, 'A 32-bit address is used with a direct-mapped cache of size 16 KB and block size 32 bytes. '
         'The number of tag bits is ________.', tag, S)
nat(COA, 'A 2-way set-associative cache has a total size of 64 KB and a block size of 64 bytes. '
         'The number of sets is ________.', 64 * 1024 // (64 * 2), S)
nat(COA, 'A 4-way set-associative cache has 64 sets. The total number of cache lines is ________.', 4 * 64, S)

hit, tlb_t, mem_t = 0.9, 10, 100
eat = hit * (tlb_t + mem_t) + (1 - hit) * (tlb_t + 2 * mem_t)
nat(COA, 'A TLB has a hit ratio of 0.9. The TLB access time is 10 ns and the main memory access time is 100 ns. '
         'The TLB is accessed first, followed by memory. The effective memory access time (in ns) is ________.',
    int(eat), S)

S = 'Curated - CPU Performance'
nat(COA, 'A non-pipelined processor takes 5 ns to execute an instruction. A 5-stage pipelined version runs at '
         '1 ns per stage. For a very large number of instructions, the ideal speedup is ________.', 5, S)
cpi = 0.4 * 1 + 0.3 * 2 + 0.3 * 3
nat(COA, 'A program executes three instruction classes: 40% ALU operations with CPI 1, 30% load operations with CPI 2, '
         'and 30% branch operations with CPI 3. The average CPI is ________.', round(cpi, 1), S)
nat(COA, 'If 80% of a program can be parallelized perfectly, the maximum speedup achievable with an unbounded '
         'number of processors (Amdahl\'s law) is ________.', 5, S)
nat(COA, 'A memory of 1 MB is to be built using 64 KB memory chips. The number of chips required is ________.', 16, S)
mcq(COA, 'In little-endian representation, the 32-bit value 0x12345678 is stored starting at address 100. '
         'The byte at address 100 is',
    '0x78', ['0x12', '0x56', '0x34'], 'Curated - Data Representation')
mcq(COA, 'Which addressing mode does NOT require a memory access to fetch the operand?',
    'Immediate addressing', ['Direct addressing', 'Indirect addressing', 'Indexed addressing'],
    'Curated - Instruction Set')
mcq(COA, 'DMA is primarily used to',
    'transfer data between memory and I/O devices without CPU involvement for each word',
    ['increase the clock frequency of the CPU',
     'provide virtual memory support',
     'implement interrupts in the processor'],
    'Curated - I/O Organization')
msq(COA, 'Which of the following are valid cache replacement policies?',
    ['LRU', 'FIFO', 'Random'], ['Best fit'], 'Curated - Memory Hierarchy')

# ===================== Programming & Data Structures (41) =====================
PDS = 'Programming & Data Structures'
S = 'Curated - C Programming'

for text, ans in [
    ('int a = 5, b = 2; int r = a / b + a % b;', 2 + 1),
    ('int a = 7, b = 3; int r = (a > b) ? (a % b) : (b % a);', 7 % 3),
    ('int x = 4; int r = x << 2;', 16),
    ('int a = 12, b = 5; int r = a & b;', 12 & 5),
    ('int a = 12, b = 5; int r = a | b;', 12 | 5),
]:
    nat(PDS, f'What is the value of r after executing the following C code?\n{text} ________.', ans, S)

S = 'Curated - Pointers'
nat(PDS, 'int a[5] = {10, 20, 30, 40, 50}; int *p = a + 2; The value of *(p + 1) is ________.', 40, S)
nat(PDS, 'On a machine where int occupies 4 bytes, int a[10]; int *p = &a[3]; int *q = &a[7]; '
         'The value of (q - p) is ________.', 4, S)
nat(PDS, 'char s[] = "program"; The value of sizeof(s) is ________.', 8, S)
nat(PDS, 'struct S { char c; int i; }; On a 32-bit machine where char takes 1 byte and int takes 4 bytes, '
         'with no packing, the value of sizeof(struct S) is ________.', 8, S)

S = 'Curated - Trees'
for h in [2, 3, 4, 5]:
    nat(PDS, f'A full binary tree of height {h} (the root is at height 0) has ________ nodes.', 2 ** (h + 1) - 1, S)
for n in [15, 31]:
    nat(PDS, f'A full binary tree with {n} nodes has ________ leaf nodes.', (n + 1) // 2, S)
for n in [100, 64]:
    nat(PDS, f'The height of a complete binary tree with {n} nodes (single node tree has height 0) is ________.',
        int(math.floor(math.log2(n))), S)
for n, c in [(3, 5), (4, 14)]:
    nat(PDS, f'The number of distinct binary search trees that can be formed with {n} distinct keys is ________.', c, S)
nat(PDS, 'In a binary tree, the maximum number of nodes at level k (root at level 0) is ________.', 2 ** 5, S)
nat(PDS, 'The maximum number of nodes in a binary tree of height 3 (root at height 0) is ________.', 15, S)

S = 'Curated - Searching & Hashing'
for n in [1000, 100, 31]:
    nat(PDS, f'In binary search on a sorted array of {n} elements, the maximum number of comparisons required '
             f'is ________.', math.ceil(math.log2(n + 1)), S)

keys, size = [5, 15, 25, 35, 45], 4
collisions = len(keys) - len(set(k % size for k in keys))
nat(PDS, f'Keys {keys} are inserted into a hash table of size {size} using h(k) = k mod {size} with chaining. '
         f'The number of collisions is ________.', collisions, S)
keys2, size2 = [12, 22, 32, 42, 52], 5
nat(PDS, f'Keys {keys2} are inserted into a hash table of size {size2} using h(k) = k mod {size2} with chaining. '
         f'The number of collisions is ________.', len(keys2) - len(set(k % size2 for k in keys2)), S)

S = 'Curated - Stacks & Queues'
mcq(PDS, 'Elements 1, 2, 3 are pushed onto a stack in that order, with interleaved pops. '
         'Which of the following output sequences is NOT possible?',
    '3, 1, 2', ['3, 2, 1', '1, 2, 3', '2, 1, 3'], S)
nat(PDS, 'The minimum number of stacks required to implement a queue is ________.', 2, S)
mcq(PDS, 'The postfix (reverse Polish) form of the infix expression (A + B) * (C - D) is',
    'AB+CD-*', ['AB+CD*-', 'A+B*C-D', 'ABC+D-*'], S)

S = 'Curated - Linked Lists'
nat(PDS, 'In a singly linked list, the number of pointer fields updated when inserting a new node at the '
         'beginning is ________.', 2, S)
nat(PDS, 'In a singly linked list with 10 nodes, deleting the last node requires traversing ________ nodes '
         'to reach its predecessor.', 9, S)
nat(PDS, 'A doubly linked list with n nodes has a total of ________ pointer fields.', 2 * 5, S)

S = 'Curated - Graphs'
for n in [5, 6, 10]:
    nat(PDS, f'A complete undirected graph with {n} vertices has ________ edges.', n * (n - 1) // 2, S)
nat(PDS, 'The adjacency matrix of a graph with 100 vertices has ________ entries.', 100 * 100, S)

S = 'Curated - Strings & Recursion'
nat(PDS, 'The number of substrings of a string of length 5 (excluding the empty string) is ________.', 15, S)
nat(PDS, 'For the recurrence f(n) = f(n-1) + f(n-2) with f(0) = 0 and f(1) = 1, the value of f(6) is ________.', 8, S)
nat(PDS, 'For the recurrence f(n) = n * f(n-1) with f(0) = 1, the value of f(5) is ________.', 120, S)
nat(PDS, 'For the recurrence g(n) = g(n-1) + g(n-2) + 1 with g(0) = 0 and g(1) = 1, the value of g(4) is ________.', 7, S)

S = 'Curated - Data Structures'
msq(PDS, 'Which of the following operations have O(1) average time complexity?',
    ['Push onto a stack', 'Enqueue in a queue', 'Insert into a hash table'],
    ['Insert into a sorted array'], S)

# ============================= Algorithms (48) =============================
ALG = 'Algorithms'
S = 'Curated - Complexity Analysis'
for rec, ans in [
    ('T(n) = 2T(n/2) + n', 'Theta(n log n)'),
    ('T(n) = T(n/2) + n', 'Theta(n)'),
    ('T(n) = 2T(n/2) + n log n', 'Theta(n log^2 n)'),
    ('T(n) = 4T(n/2) + n', 'Theta(n^2)'),
    ('T(n) = T(n-1) + n', 'Theta(n^2)'),
    ('T(n) = 2T(n-1) + 1', 'Theta(2^n)'),
]:
    mcq(ALG, f'Using the Master Theorem or the recursion-tree method, the tight asymptotic bound for the recurrence '
             f'{rec} is',
        ans, ['Theta(n)', 'Theta(n log n)', 'Theta(n^2)', 'Theta(2^n)', 'Theta(log n)'],
        'Curated - Recurrences')

mcq(ALG, 'Which of the following functions grows the fastest asymptotically?',
    '2^n', ['n^3', 'n log n', 'log^2 n'], S)
mcq(ALG, 'Which of the following is Theta(n log n)?',
    'n log n', ['n^2', 'log n', '2^n'], S)

S = 'Curated - Sorting'
nat(ALG, 'The number of levels in the recursion tree of merge sort on an array of 16 elements is ________ '
         '(a single-element array is at level 0).', int(math.log2(16)) + 1, S)
for n in [4, 8]:
    cnt = n * math.ceil(math.log2(n)) - 2 ** math.ceil(math.log2(n)) + 1
    nat(ALG, f'The maximum (worst-case) number of comparisons performed by merge sort on {n} elements is ________.',
        int(cnt), S)
for n in [8, 10, 16]:
    nat(ALG, f'The number of comparisons performed by quicksort in the worst case on an array of {n} distinct '
             f'elements is ________.', n * (n - 1) // 2, S)
nat(ALG, 'The number of swaps performed by selection sort on an array of n elements in the worst case is ________ '
         '(assume n = 10).', 9, S)
nat(ALG, 'The height of the recursion tree for quicksort in the best case with n = 16 is ________ '
         '(a single element is at level 0).', int(math.log2(16)), S)

S = 'Curated - Searching'
for n in [15, 63, 1023]:
    nat(ALG, f'The maximum number of iterations of binary search on a sorted array of {n} elements is ________.',
        math.ceil(math.log2(n + 1)), S)

S = 'Curated - Dynamic Programming'


def lcs_len(a, b):
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            dp[i][j] = dp[i - 1][j - 1] + 1 if a[i - 1] == b[j - 1] else max(dp[i - 1][j], dp[i][j - 1])
    return dp[-1][-1]


def edit_dist(a, b):
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(len(a) + 1):
        dp[i][0] = i
    for j in range(len(b) + 1):
        dp[0][j] = j
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            dp[i][j] = dp[i - 1][j - 1] if a[i - 1] == b[j - 1] else 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    return dp[-1][-1]


def coin_ways(coins, amount):
    dp = [0] * (amount + 1)
    dp[0] = 1
    for c in coins:
        for x in range(c, amount + 1):
            dp[x] += dp[x - c]
    return dp[amount]


for a, b in [('ABCBDAB', 'BDCABA'), ('AGGTAB', 'GXTXAYB'), ('ABCDGH', 'AEDFHR'), ('GATE', 'LATE')]:
    nat(ALG, f'The length of the longest common subsequence of the strings "{a}" and "{b}" is ________.',
        lcs_len(a, b), S)
for a, b in [('kitten', 'sitting'), ('sunday', 'saturday'), ('cat', 'cut')]:
    nat(ALG, f'The minimum edit distance (Levenshtein distance) between "{a}" and "{b}" is ________.',
        edit_dist(a, b), S)
for coins, amt in [([1, 2, 5], 5), ([1, 3, 4], 6), ([2, 5, 10], 10)]:
    nat(ALG, f'The number of distinct ways to make a sum of {amt} using an unlimited supply of coins with '
             f'denominations {coins} is ________.', coin_ways(coins, amt), S)

S = 'Curated - Graph Algorithms'
for n in [4, 5]:
    nat(ALG, f'The number of distinct spanning trees of a complete graph with {n} vertices (Cayley\'s formula) '
             f'is ________.', n ** (n - 2), S)
mcq(ALG, 'Dijkstra\'s single-source shortest path algorithm can produce incorrect results with negative edge weights '
         'because',
    'a vertex whose distance is finalized may later need to be updated',
    ['it cannot handle more than V - 1 edges',
     'it always performs exactly V iterations',
     'it requires the graph to be complete'],
    S)
mcq(ALG, 'The Bellman-Ford algorithm detects a negative weight cycle reachable from the source by',
    'performing one extra relaxation round and checking whether any distance still decreases',
    ['sorting the edges by weight',
     'running Dijkstra after one pass',
     'checking whether the graph is connected'],
    S)
mcq(ALG, 'Which algorithm computes all-pairs shortest paths in Theta(V^3) time using dynamic programming?',
    'Floyd-Warshall', ['Dijkstra', 'Bellman-Ford', 'Prim'], S)
nat(ALG, 'A connected undirected graph with V vertices has a spanning tree with ________ edges (V = 7).', 6, S)
mcq(ALG, 'Breadth-first search on a graph with V vertices and E edges (adjacency list representation) runs in',
    'O(V + E)', ['O(V^2)', 'O(E log V)', 'O(V * E)'], S)
mcq(ALG, 'A directed graph has a topological ordering if and only if it is',
    'a directed acyclic graph', ['strongly connected', 'a complete graph', 'a tree'], S)

S = 'Curated - Heaps'
nat(ALG, 'The height of a binary heap with 100 elements is ________ (a single-node heap has height 0).',
    int(math.floor(math.log2(100))), S)
nat(ALG, 'In a binary heap stored as a 1-indexed array, the parent of the node at index 7 is at index ________.', 3, S)

S = 'Curated - Algorithm Design'
mcq(ALG, 'Find-minimum on a binary min-heap takes',
    'O(1)', ['O(log n)', 'O(n)', 'O(n log n)'], S)
mcq(ALG, 'Inserting an element into a sorted array of n elements takes',
    'O(n)', ['O(1)', 'O(log n)', 'O(n log n)'], S)
mcq(ALG, 'The amortized cost of appending an element to a dynamic array (doubling strategy) is',
    'O(1)', ['O(log n)', 'O(n)', 'O(n^2)'], S)
nat(ALG, 'The recursion tree for T(n) = 2T(n/2) + n with n = 16 has ________ levels (root at level 1).', 5, S)
nat(ALG, 'The recursion tree for T(n) = T(n/4) + 1 with n = 256 has ________ levels (root at level 1).',
    int(math.log2(256) / math.log2(4)) + 1, S)

mcq(ALG, 'Which of the following problems can be solved optimally by a greedy algorithm?',
    'Fractional knapsack', ['0/1 knapsack', 'Longest common subsequence', 'Edit distance'], S)
mcq(ALG, 'Which of the following problems does NOT admit an optimal greedy solution?',
    '0/1 knapsack', ['Huffman coding', 'Dijkstra\'s algorithm', 'Kruskal\'s algorithm'], S)
mcq(ALG, 'The activity selection problem is solved optimally by selecting activities in the order of',
    'earliest finishing time', ['earliest start time', 'shortest duration', 'largest start time'], S)

msq(ALG, 'Which of the following problems are NP-complete?',
    ['Boolean satisfiability (SAT)', '3-SAT', 'Hamiltonian cycle'],
    ['2-SAT'], S)

# =========================== Operating Systems (41) ===========================
OS = 'Operating Systems'
S = 'Curated - Memory Management'
for ps, bits in [('4 KB', 12), ('8 KB', 13), ('512 bytes', 9)]:
    nat(OS, f'A system uses pages of size {ps}. The number of bits required for the page offset is ________.', bits, S)
nat(OS, 'A system has a 32-bit virtual address space and a page size of 4 KB. The number of virtual pages is ________.',
    2 ** 20, S)
nat(OS, 'A system has a 16-bit virtual address space and a page size of 256 bytes. The number of virtual pages '
        'is ________.', 2 ** 8, S)
nat(OS, 'A system has a 32-bit virtual address space, 4 KB pages, and 4-byte page table entries. '
        'The size of the page table (in KB) is ________.', 2 ** 20 * 4 // 1024, S)
nat(OS, 'A system has a 20-bit virtual address space, 1 KB pages, and 4-byte page table entries. '
        'The number of page table entries is ________.', 2 ** 10, S)
nat(OS, 'A page table has 2^20 entries, each of size 8 bytes. The size of the page table (in MB) is ________.',
    2 ** 20 * 8 // (1024 * 1024), S)
nat(OS, 'A two-level page table uses a 10-10-12 split of a 32-bit address with 4-byte entries. '
        'The number of entries in the inner (second-level) page table is ________.', 2 ** 10, S)
nat(OS, 'A two-level page table uses a 10-10-12 split of a 32-bit address with 4-byte entries. '
        'The size of the outer (first-level) page table (in KB) is ________.', 2 ** 10 * 4 // 1024, S)

hit, tlb_t, mem_t = 0.8, 20, 200
nat(OS, f'A TLB has a hit ratio of {hit}, TLB access time {tlb_t} ns, and memory access time {mem_t} ns. '
         f'The TLB is accessed before memory (sequential access). The effective access time (in ns) is ________.',
    int(hit * (tlb_t + mem_t) + (1 - hit) * (tlb_t + 2 * mem_t)), S)
hit, tlb_t, mem_t = 0.9, 10, 100
nat(OS, f'A TLB has a hit ratio of {hit}, TLB access time {tlb_t} ns, and memory access time {mem_t} ns. '
         f'The TLB and memory are accessed in parallel, and a TLB miss requires one extra memory access. '
         f'The effective access time (in ns) is ________.',
    int(hit * mem_t + (1 - hit) * (mem_t + mem_t)), S)
nat(OS, 'A TLB has 64 entries and a page size of 4 KB. The maximum amount of memory addressable through the TLB '
        '(TLB reach) in KB is ________.', 64 * 4, S)


def page_faults(ref, frames, policy):
    mem, faults = [], 0
    for p in ref:
        if p in mem:
            if policy == 'lru':
                mem.remove(p)
                mem.append(p)
        else:
            faults += 1
            if len(mem) >= frames:
                mem.pop(0)
            mem.append(p)
    return faults


ref1 = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
nat(OS, f'For the page reference string {ref1} and 3 frames, the number of page faults using the FIFO '
        f'replacement policy is ________.', page_faults(ref1, 3, 'fifo'), S)
nat(OS, f'For the page reference string {ref1} and 3 frames, the number of page faults using the LRU '
        f'replacement policy is ________.', page_faults(ref1, 3, 'lru'), S)
ref2 = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
nat(OS, f'For the page reference string {ref2} and 3 frames, the number of page faults using the FIFO '
        f'replacement policy is ________.', page_faults(ref2, 3, 'fifo'), S)


def fcfs_wait(procs):
    t, waits = 0, []
    for a, b in sorted(procs):
        if t < a:
            t = a
        waits.append(t - a)
        t += b
    return waits


def sjf_wait(procs):
    import heapq
    procs = sorted(procs)
    t, i, waits, heap = 0, 0, [], []
    n = len(procs)
    while i < n or heap:
        if not heap and i < n and t < procs[i][0]:
            t = procs[i][0]
        while i < n and procs[i][0] <= t:
            heapq.heappush(heap, (procs[i][1], procs[i][0]))
            i += 1
        if heap:
            b, a = heapq.heappop(heap)
            waits.append(t - a)
            t += b
    return waits


def rr_wait(procs, q):
    procs = sorted(procs)
    n = len(procs)
    rem = [b for a, b in procs]
    t, i, dq, waits = 0, 0, deque(), [0] * n
    done = 0
    while done < n:
        if not dq and i < n and t < procs[i][0]:
            t = procs[i][0]
        while i < n and procs[i][0] <= t:
            dq.append(i)
            i += 1
        if not dq:
            continue
        j = dq.popleft()
        run = min(q, rem[j])
        rem[j] -= run
        t += run
        while i < n and procs[i][0] <= t:
            dq.append(i)
            i += 1
        if rem[j] > 0:
            dq.append(j)
        else:
            done += 1
            waits[j] = t - procs[j][0] - procs[j][1]
    return waits


S = 'Curated - CPU Scheduling'
procs = [(0, 7), (2, 4), (4, 1), (5, 4)]
w = fcfs_wait(procs)
nat(OS, 'Consider four processes with (arrival time, burst time) = P1(0, 7), P2(2, 4), P3(4, 1), P4(5, 4). '
        'The average waiting time (in units, rounded to 2 decimals) under non-preemptive FCFS is ________.',
    round(sum(w) / len(w), 2), S)
w = sjf_wait(procs)
nat(OS, 'Consider four processes with (arrival time, burst time) = P1(0, 7), P2(2, 4), P3(4, 1), P4(5, 4). '
        'The average waiting time (in units, rounded to 2 decimals) under non-preemptive SJF is ________.',
    round(sum(w) / len(w), 2), S)
w = fcfs_wait(procs)
nat(OS, 'Consider four processes with (arrival time, burst time) = P1(0, 7), P2(2, 4), P3(4, 1), P4(5, 4). '
        'The average turnaround time (in units, rounded to 2 decimals) under non-preemptive FCFS is ________.',
    round((sum(w) + sum(b for a, b in procs)) / len(procs), 2), S)
w = rr_wait(procs, 2)
nat(OS, 'Consider four processes with (arrival time, burst time) = P1(0, 7), P2(2, 4), P3(4, 1), P4(5, 4). '
        'The average waiting time (in units, rounded to 2 decimals) under round robin with time quantum 2 is ________.',
    round(sum(w) / len(w), 2), S)
procs2 = [(0, 4), (1, 3), (2, 1)]
w = rr_wait(procs2, 1)
nat(OS, 'Consider three processes with (arrival time, burst time) = P1(0, 4), P2(1, 3), P3(2, 1). '
        'The average waiting time (in units, rounded to 2 decimals) under round robin with time quantum 1 is ________.',
    round(sum(w) / len(w), 2), S)

S = 'Curated - Synchronization'
nat(OS, 'A counting semaphore is initialized to 5. After 8 P (wait) operations and 3 V (signal) operations, '
        'the value of the semaphore is ________.', 5 - 8 + 3, S)
nat(OS, 'A counting semaphore is initialized to 3. After 4 P (wait) operations and 6 V (signal) operations, '
        'the value of the semaphore is ________.', 3 - 4 + 6, S)
nat(OS, 'How many total processes (including the original) exist after 3 consecutive fork() calls that all succeed? '
        '________.', 2 ** 3, S)
nat(OS, 'How many total processes (including the original) exist after 4 consecutive fork() calls that all succeed? '
        '________.', 2 ** 4, S)
nat(OS, 'In a system with 5 processes, each process needs a maximum of 3 units of a single resource type. '
        'The minimum number of resource units required to guarantee that deadlock can never occur is ________.',
    5 * (3 - 1) + 1, S)
mcq(OS, 'Banker\'s algorithm is used for',
    'deadlock avoidance', ['deadlock prevention', 'deadlock detection', 'deadlock recovery'], S)
mcq(OS, 'A system is said to be in a safe state if',
    'there exists a sequence of processes in which every process can complete with the available resources',
    ['no process is currently blocked',
     'all processes hold at most one resource',
     'the resource allocation graph has no cycles'],
    S)
mcq(OS, 'Which of the following is NOT a necessary condition for deadlock?',
    'Preemption of resources', ['Mutual exclusion', 'Hold and wait', 'Circular wait'], S)

S = 'Curated - Disk Scheduling'
reqs, head = [98, 183, 37, 122, 14, 124, 65, 67], 53
d = 0
h = head
for r in reqs:
    d += abs(r - h)
    h = r
nat(OS, f'The disk request queue is {reqs} with the head initially at {head}. The total head movement (in cylinders) '
        f'using the FCFS disk scheduling algorithm is ________.', d, S)


def sstf(reqs, head):
    reqs = list(reqs)
    d = 0
    while reqs:
        nxt = min(reqs, key=lambda r: abs(r - head))
        d += abs(nxt - head)
        head = nxt
        reqs.remove(nxt)
    return d


nat(OS, f'The disk request queue is {reqs} with the head initially at {head}. The total head movement (in cylinders) '
        f'using the SSTF disk scheduling algorithm is ________.', sstf(reqs, head), S)
reqs2, head2 = [10, 22, 20, 2, 40, 6, 38], 20
nat(OS, f'The disk request queue is {reqs2} with the head initially at {head2}. The total head movement (in cylinders) '
        f'using the FCFS disk scheduling algorithm is ________.',
    sum(abs(b - a) for a, b in zip([head2] + reqs2, reqs2)), S)

S = 'Curated - File Systems'
nat(OS, 'An inode contains 10 direct block pointers, 1 single indirect pointer, and 1 double indirect pointer. '
        'The block size is 1 KB and a pointer is 4 bytes. The maximum file size (in KB) is ________.',
    10 + 256 + 256 * 256, S)
nat(OS, 'A file system uses 12 direct pointers, 1 single indirect pointer, 1 double indirect pointer, and '
        '1 triple indirect pointer. The block size is 4 KB and a pointer is 4 bytes. The amount of file data '
        'addressable through the single indirect pointer (in KB) is ________.', 1024 * 4, S)

S = 'Curated - Process Management'
mcq(OS, 'Which of the following is NOT a requirement for a correct solution to the critical section problem?',
    'Priority inversion must be prevented',
    ['Mutual exclusion must be guaranteed', 'Progress must be guaranteed', 'Bounded waiting must be guaranteed'], S)
mcq(OS, 'Peterson\'s solution to the critical section problem satisfies',
    'mutual exclusion, progress, and bounded waiting',
    ['only mutual exclusion', 'only mutual exclusion and progress', 'mutual exclusion and bounded waiting only'], S)
mcq(OS, 'Internal fragmentation occurs when',
    'allocated memory is larger than the requested memory',
    ['free memory blocks are too small to satisfy a request',
     'the page table grows beyond one page',
     'the TLB is flushed on a context switch'], S)
mcq(OS, 'Compaction is a technique used to address',
    'external fragmentation', ['internal fragmentation', 'page faults', 'thrashing'], S)
mcq(OS, 'Thrashing occurs when',
    'the system spends more time servicing page faults than executing processes',
    ['the CPU utilization is 100 percent',
     'the page size is too large',
     'the degree of multiprogramming is too low'], S)
mcq(OS, 'The working set model is used to',
    'estimate the set of pages a process needs in the near future to control thrashing',
    ['allocate disk blocks to files',
     'schedule processes by priority',
     'recover from deadlocks'], S)
msq(OS, 'Which of the following are necessary conditions for deadlock?',
    ['Mutual exclusion', 'Hold and wait', 'Circular wait'], ['Preemption'], S)

# ================================ Databases (34) ================================
DB = 'Databases'
S = 'Curated - Relational Algebra'

R1 = [(1, 10), (2, 10), (3, 20), (4, 30)]
S1 = [(10, 'x'), (20, 'y'), (20, 'z')]
cnt = sum(1 for a, b in R1 for c, d in S1 if b == c)
nat(DB, f'Relation R(A, B) has tuples {R1} and relation S(B, C) has tuples {S1}. '
        f'The number of tuples in the natural join R JOIN S is ________.', cnt, S)
R2 = [(1, 'a'), (1, 'b'), (2, 'c')]
S2 = [(1, 'p'), (2, 'q'), (2, 'r')]
cnt = sum(1 for a, b in R2 for c, d in S2 if a == c)
nat(DB, f'Relation R(A, B) has tuples {R2} and relation S(A, C) has tuples {S2}. '
        f'The number of tuples in the natural join R JOIN S is ________.', cnt, S)
nat(DB, f'Relation R has {len(R1)} tuples and relation S has {len(S1)} tuples. '
        f'The number of tuples in the Cartesian product R x S is ________.', len(R1) * len(S1), S)
nat(DB, f'Relation R has 5 tuples and relation S has 7 tuples. The number of tuples in the Cartesian product '
        f'R x S is ________.', 35, S)
mcq(DB, 'Which of the following is NOT one of the basic operators of relational algebra?',
    'Aggregation', ['Selection', 'Projection', 'Cartesian product'], S)
mcq(DB, 'If relations R and S have no tuples in common on the join attribute, the natural join R JOIN S returns',
    'an empty relation', ['all tuples of R', 'all tuples of S', 'the Cartesian product'], S)
mcq(DB, 'If relation R has 3 attributes and relation S has 4 attributes, the Cartesian product R x S has',
    '7 attributes', ['12 attributes', '3 attributes', '4 attributes'], S)

S = 'Curated - Functional Dependencies'
nat(DB, 'Relation R(A, B, C) has the functional dependency A -> B. The number of superkeys of R is ________.', 4, S)
nat(DB, 'Relation R(A, B, C) has the functional dependency AB -> C. The number of superkeys of R is ________.', 2, S)
nat(DB, 'Relation R(A, B, C, D) has the functional dependencies A -> B and B -> A and C -> D and D -> C. '
        'The number of candidate keys of R is ________.', 4, S)
nat(DB, 'For the FD set F = {A -> B, B -> C, C -> D}, the size of the attribute closure A+ is ________.', 4, S)
nat(DB, 'For the FD set F = {A -> B, B -> C, C -> D}, the size of the attribute closure B+ is ________.', 3, S)
nat(DB, 'Relation R(A, B) has the functional dependency A -> B. The number of superkeys of R is ________.', 2, S)
nat(DB, 'The number of possible serial schedules of 2 transactions is ________.', 2, S)

S = 'Curated - Normalization'
mcq(DB, 'Relation R(A, B, C, D) has the functional dependencies AB -> CD and D -> A. The highest normal form '
        'satisfied by R is',
    '3NF', ['1NF', '2NF', 'BCNF'], S)
mcq(DB, 'Relation R(A, B, C) has the functional dependencies A -> B and B -> C. The highest normal form '
        'satisfied by R is',
    '2NF', ['1NF', '3NF', 'BCNF'], S)
mcq(DB, 'Relation R(A, B, C, D) has the functional dependencies AB -> C and AB -> D. The highest normal form '
        'satisfied by R is',
    'BCNF', ['1NF', '2NF', '3NF'], S)
mcq(DB, 'A BCNF decomposition is always',
    'lossless but not necessarily dependency preserving',
    ['dependency preserving but not necessarily lossless',
     'both lossless and dependency preserving',
     'neither lossless nor dependency preserving'], S)
mcq(DB, '3NF is often preferred over BCNF because a 3NF decomposition',
    'can always be made both lossless and dependency preserving',
    ['always has fewer tables', 'never requires joins', 'eliminates all redundancy'], S)
mcq(DB, 'A relation is in 2NF if it is in 1NF and',
    'every non-prime attribute is fully functionally dependent on every candidate key',
    ['every determinant is a superkey',
     'it has no multivalued dependencies',
     'it has at most one candidate key'], S)

S = 'Curated - SQL'
nat(DB, 'Consider the table T(x, y) with rows (1, 2), (1, 3), (2, 4), and (NULL, 5). '
        'The result of SELECT COUNT(*) FROM T is ________.', 4, S)
nat(DB, 'Consider the table T(x, y) with rows (1, 2), (1, 3), (2, 4), and (NULL, 5). '
        'The result of SELECT COUNT(x) FROM T is ________.', 3, S)
nat(DB, 'Consider the table T(x, y) with rows (1, 2), (1, 3), (2, 4), and (NULL, 5). '
        'The result of SELECT COUNT(DISTINCT x) FROM T is ________.', 2, S)

S = 'Curated - Transactions'
mcq(DB, 'Consider the schedule: r1(A), w2(A), r1(B), w2(B). This schedule is',
    'not conflict serializable', ['conflict serializable as T1 then T2', 'conflict serializable as T2 then T1',
                                  'a serial schedule'], S)
mcq(DB, 'Consider the schedule: r1(A), r2(B), w1(A), w2(B). This schedule is',
    'conflict serializable', ['not conflict serializable', 'not recoverable', 'a strict schedule'], S)
nat(DB, 'The number of possible serial schedules of 3 transactions is ________.', 6, S)
nat(DB, 'The number of possible serial schedules of 4 transactions is ________.', 24, S)
mcq(DB, 'Two-phase locking (2PL) guarantees',
    'conflict serializability', ['deadlock freedom', 'recoverability', 'strict serializability'], S)
msq(DB, 'Which of the following are ACID properties of transactions?',
    ['Atomicity', 'Consistency', 'Isolation'], ['Concurrency'], S)

S = 'Curated - ER Model & Storage'
nat(DB, 'An ER diagram has 3 entity sets and 2 many-to-many relationship sets. The minimum number of tables '
        'required in the relational schema is ________.', 5, S)
nat(DB, 'An ER diagram has 2 entity sets connected by a many-to-one relationship set. '
        'The minimum number of tables required is ________.', 2, S)
mcq(DB, 'In a B+ tree, all the actual key values are stored in',
    'the leaf nodes', ['the root node', 'internal nodes only', 'both internal and leaf nodes'], S)
mcq(DB, 'In a B+ tree of order n, the maximum number of pointers in an internal node is',
    'n', ['n - 1', 'n + 1', '2n'], S)
nat(DB, 'In a B+ tree of order 5 (each non-root node must have between 2 and 4 keys), the minimum number of keys '
        'in a non-root leaf node is ________.', 2, S)

# ============================ Theory of Computation (18) ============================
TOC = 'Theory of Computation'
S = 'Curated - Finite Automata'
for desc, states in [('strings over {a, b} that end with "ab"', 3),
                     ('strings over {a, b} with an even number of a\'s', 2),
                     ('strings over {a, b} where the number of a\'s is divisible by 3', 3),
                     ('strings over {a, b} that contain "aba" as a substring', 4)]:
    nat(TOC, f'The minimum number of states in a DFA that accepts exactly the set of {desc} is ________.',
        states, S)
nat(TOC, 'An NFA has 3 states. The maximum number of states in the DFA obtained by the subset construction '
        'is ________.', 2 ** 3, S)
nat(TOC, 'An NFA has 2 states. The maximum number of states in the DFA obtained by the subset construction '
        'is ________.', 2 ** 2, S)

S = 'Curated - Regular Languages'
nat(TOC, 'The number of strings of length 4 over the alphabet {a, b} is ________.', 2 ** 4, S)
nat(TOC, 'The number of strings of length 5 over {0, 1} that start with 1 is ________.', 2 ** 4, S)
mcq(TOC, 'The regular expressions (a + b)* and (a* b*)* are',
    'equivalent', ['not equivalent', 'equivalent only over unary alphabets', 'equivalent only for finite strings'], S)
mcq(TOC, 'The regular expression (a + b)* ab (a + b)* represents',
    'all strings containing ab as a substring', ['all strings ending with ab', 'all strings starting with ab',
                                                 'all strings containing exactly one ab'], S)
mcq(TOC, 'The pumping lemma for regular languages is primarily used to',
    'prove that a given language is not regular', ['prove that a language is regular',
                                                  'minimize a DFA', 'convert an NFA to a DFA'], S)
mcq(TOC, 'The language {a^n b^n | n >= 0} is',
    'not regular', ['regular', 'finite', 'regular but not context-free'], S)

S = 'Curated - Grammars & Decidability'
mcq(TOC, 'A type-3 grammar in the Chomsky hierarchy generates exactly the',
    'regular languages', ['context-free languages', 'context-sensitive languages', 'recursively enumerable languages'], S)
mcq(TOC, 'The grammar with productions S -> aSb | epsilon generates',
    'a context-free language that is not regular', ['a regular language', 'a finite language',
                                                    'a context-sensitive but not context-free language'], S)
nat(TOC, 'The grammar S -> aSa | bSb | a | b | epsilon has ________ productions.', 5, S)
mcq(TOC, 'Which of the following problems is undecidable?',
    'Whether a given Turing machine halts on every input',
    ['Whether a given DFA accepts the empty string',
     'Whether a given CFG generates the empty string',
     'Whether two DFAs accept the same language'], S)
mcq(TOC, 'Which of the following sets is uncountable?',
    'The set of all languages over {0, 1}',
    ['The set of all strings over {0, 1}', 'The set of all Turing machines', 'The set of all regular languages'], S)
mcq(TOC, 'Regular languages are closed under',
    'union, intersection, and complementation', ['union only', 'intersection only', 'union and intersection but not complementation'], S)

# ============================ Computer Networks (8) ============================
CN = 'Computer Networks'
S = 'Curated - IP Addressing & Routing'
nat(CN, 'A subnet uses the prefix /26. The number of usable host addresses in the subnet is ________.', 62, S)
nat(CN, 'A subnet uses the prefix /27. The number of usable host addresses in the subnet is ________.', 30, S)
nat(CN, 'A 3000-byte IP datagram has a 20-byte header and must traverse a link with an MTU of 1500 bytes. '
        'The number of fragments required is ________.', 3, S)
mcq(CN, 'The IP address 192.168.1.1 belongs to class',
    'C', ['A', 'B', 'D'], S)

S = 'Curated - Data Link & Transport'


def crc_remainder(data, gen):
    d = [int(c) for c in data + '0' * (len(gen) - 1)]
    g = [int(c) for c in gen]
    for i in range(len(data)):
        if d[i]:
            for j in range(len(g)):
                d[i + j] ^= g[j]
    return ''.join(str(x) for x in d[len(data):])


rem = crc_remainder('1101011011', '10011')
nat(CN, f'Using CRC with generator polynomial 10011 for the data 1101011011, the remainder is ________ '
        f'(enter the bit string as a decimal number).', int(rem), S)
nat(CN, 'In the Go-Back-N protocol with a sender window size of 5, the minimum number of distinct sequence '
        'numbers required is ________.', 6, S)
nat(CN, 'Two hosts are 3000 km apart on a link with signal propagation speed 2 x 10^8 m/s. '
        'The one-way propagation delay (in milliseconds) is ________.', 15, S)
msq(CN, 'Which of the following are application layer protocols?',
    ['HTTP', 'DNS'], ['TCP', 'IP'], S)

# ============================= Compiler Design (8) =============================
CD = 'Compiler Design'
S = 'Curated - Lexical & Syntax Analysis'
nat(CD, 'The number of tokens produced by the lexical analyzer for the statement "int a = b + c * 5;" is ________ '
        '(count int, identifiers, operators, and the semicolon as separate tokens).', 9, S)
mcq(CD, 'For the grammar S -> aB | b, B -> c, the set FIRST(S) is',
    '{a, b}', ['{a}', '{b}', '{a, b, c}'], S)
mcq(CD, 'For the grammar S -> aB, B -> b, the set FOLLOW(B) is',
    '{$}', ['{a}', '{b}', '{a, b}'], S)
mcq(CD, 'A grammar is LL(1) if and only if',
    'the predictive parsing table has no conflicting entries',
    ['it is left-recursive', 'it is ambiguous', 'it has no epsilon productions'], S)
mcq(CD, 'The number of states in the canonical LR(0) collection for the grammar S -> aS | b is',
    '4', ['2', '3', '5'], S)

S = 'Curated - Code Generation & Optimization'
nat(CD, 'The number of three-address code instructions generated for the statement a = b + c * d is ________.', 2, S)
nat(CD, 'Using the Sethi-Ullman numbering, the minimum number of registers required to evaluate the expression '
        '(b + c) * (d - e) without spilling is ________.', 2, S)
mcq(CD, 'Peephole optimization operates on',
    'a small window of consecutive instructions',
    ['the entire control flow graph', 'the abstract syntax tree only', 'the symbol table'], S)

# ========================== Engineering Mathematics (28) ==========================
EM = 'Engineering Mathematics'
S = 'Curated - Linear Algebra'
nat(EM, 'The determinant of the matrix [[2, 1], [3, 4]] is ________.', 2 * 4 - 1 * 3, S)
nat(EM, 'The determinant of the matrix [[1, 2, 3], [0, 1, 4], [5, 6, 0]] is ________.',
    1 * (1 * 0 - 4 * 6) - 2 * (0 * 0 - 4 * 5) + 3 * (0 * 6 - 1 * 5), S)
nat(EM, 'A is a 3 x 3 matrix with determinant 3. The determinant of 2A is ________.', 2 ** 3 * 3, S)
nat(EM, 'The largest eigenvalue of the matrix [[4, 1], [2, 3]] is ________.', 5, S)
nat(EM, 'The largest eigenvalue of the matrix [[1, 2], [2, 1]] is ________.', 3, S)
nat(EM, 'The rank of the matrix [[1, 2, 3], [2, 4, 6], [1, 1, 1]] is ________.', 2, S)
mcq(EM, 'The system of equations x + y = 2 and 2x + 2y = 5 has',
    'no solution', ['a unique solution', 'infinitely many solutions', 'exactly two solutions'], S)
mcq(EM, 'The system of equations x + y = 2 and 2x + 2y = 4 has',
    'infinitely many solutions', ['no solution', 'a unique solution', 'exactly two solutions'], S)

S = 'Curated - Discrete Mathematics'
nat(EM, 'The number of distinct ways to arrange the letters of the word GATE is ________.', 24, S)
nat(EM, 'The number of 3-digit numbers with all distinct digits (no leading zero) is ________.', 9 * 9 * 8, S)
nat(EM, 'The number of ways to choose 2 items from a set of 5 distinct items is ________.', 10, S)
nat(EM, 'In a class of 100 students, 60 like tea, 50 like coffee, and 30 like both. '
        'The number of students who like neither tea nor coffee is ________.', 100 - (60 + 50 - 30), S)
nat(EM, 'The number of integers from 1 to 100 that are divisible by 3 or 5 is ________.', 33 + 20 - 6, S)
nat(EM, 'The greatest common divisor of 48 and 180 is ________.', math.gcd(48, 180), S)
nat(EM, 'The least common multiple of 12 and 15 is ________.', 12 * 15 // math.gcd(12, 15), S)
nat(EM, 'The value of 17^3 mod 10 is ________.', pow(17, 3, 10), S)
nat(EM, 'The value of 3^100 mod 7 is ________.', pow(3, 100, 7), S)
nat(EM, 'The number of edges in a tree with 10 vertices is ________.', 9, S)
nat(EM, 'In a graph with 8 edges, the sum of the degrees of all vertices is ________.', 16, S)

S = 'Curated - Probability'
nat(EM, 'Two fair dice are thrown. The number of outcomes in which the sum of the numbers is 9 is ________.', 4, S)
nat(EM, 'Two fair dice are thrown. The number of outcomes in which the sum of the numbers is 7 is ________.', 6, S)
nat(EM, 'The number of ways to draw 2 aces from a standard deck of 4 aces is ________.', 6, S)
nat(EM, 'A bag contains 3 red and 4 blue balls. Two balls are drawn without replacement. '
        'The probability that both are red is ________ (round to 3 decimals).', round(3 / 7 * 2 / 6, 3), S)
nat(EM, 'A disease affects 1% of a population. A test has sensitivity 99% and specificity 95%. '
        'Given a positive test result, the probability that the person has the disease is ________ '
        '(round to 3 decimals).', round(0.01 * 0.99 / (0.01 * 0.99 + 0.99 * 0.05), 3), S)
nat(EM, 'Box A contains 2 red and 3 black balls; Box B contains 3 red and 2 black balls. A box is chosen at '
        'random and one ball is drawn, which is red. The probability that it came from Box A is ________ '
        '(round to 2 decimals).', round(0.5 * 0.4 / (0.5 * 0.4 + 0.5 * 0.6), 2), S)

S = 'Curated - Calculus & Numerical Methods'
nat(EM, 'The derivative of x^3 + 2x evaluated at x = 2 is ________.', 3 * 4 + 2, S)
nat(EM, 'The value of the limit as x tends to 0 of sin(x)/x is ________.', 1, S)
nat(EM, 'Using the Newton-Raphson method with initial guess x0 = 1 for f(x) = x^2 - 2, '
        'the next iterate x1 is ________ (round to 1 decimal).', round(1 - (1 - 2) / 2, 1), S)

# ============================= General Aptitude (23) =============================
GA = 'General Aptitude'
S = 'Curated - Quantitative Aptitude'
nat(GA, 'A number increased by 20% becomes 96. The original number is ________.', 80, S)
nat(GA, 'If 40% of the students in a class are girls and there are 240 boys, the total number of students is ________.',
    400, S)
nat(GA, 'The price of an item is increased by 25% and then decreased by 20%. The net percentage change in price '
        'is ________.', 0, S)
nat(GA, 'An amount of 180 is divided in the ratio 2 : 3 : 4. The largest share is ________.', 80, S)
mcq(GA, 'If A : B = 2 : 3 and B : C = 4 : 5, then A : B : C is',
    '8 : 12 : 15', ['2 : 3 : 5', '6 : 9 : 10', '8 : 12 : 20'], S)
nat(GA, 'A train 120 m long travels at 54 km/h. The time taken (in seconds) to pass a pole is ________.', 8, S)
nat(GA, 'A car covers 300 km in 4 hours. Its average speed in km/h is ________.', 75, S)
nat(GA, 'A can complete a job in 12 days and B can complete it in 6 days. Working together, they can complete '
        'the job in ________ days.', 4, S)
nat(GA, 'If 5 workers can build a wall in 10 days, the number of days 10 workers will take (same rate) is ________.',
    5, S)
nat(GA, 'The average of 5 numbers is 20. If the number 30 is removed, the average of the remaining numbers '
        'is ________ (round to 1 decimal).', round(70 / 4, 1), S)
nat(GA, 'The average of the first 10 natural numbers is ________ (round to 1 decimal).', 5.5, S)

S = 'Curated - Logical Reasoning'
mcq(GA, 'Find the next term in the series: 2, 6, 12, 20, 30, ?',
    '42', ['36', '40', '44'], S)
mcq(GA, 'Find the next term in the series: 1, 4, 9, 16, ?',
    '25', ['20', '24', '30'], S)
mcq(GA, 'All roses are flowers. Some flowers fade quickly. Which conclusion follows?',
    'Cannot be determined from the given statements',
    ['All roses fade quickly', 'Some roses fade quickly', 'No rose fades quickly'], S)
mcq(GA, 'If it rains, the ground is wet. The ground is wet. Therefore',
    'nothing definite can be concluded about the rain',
    ['it definitely rained', 'it definitely did not rain', 'it will rain again'], S)
mcq(GA, 'Which of the following is the odd one out? 121, 144, 169, 200',
    '200', ['121', '144', '169'], S)
mcq(GA, 'Which of the following is the odd one out? apple, banana, carrot, mango',
    'carrot', ['apple', 'banana', 'mango'], S)

S = 'Curated - Geometry & Data Interpretation'
nat(GA, 'The area of a circle of radius 7 (use pi = 22/7) is ________.', 154, S)
nat(GA, 'The perimeter of a rectangle of length 10 and width 5 is ________.', 30, S)
nat(GA, 'A fair coin is tossed twice. The probability of getting at least one head is ________ (round to 2 decimals).',
    0.75, S)
nat(GA, 'A shopkeeper sells an item for 600 that cost him 500. His profit percentage is ________.', 20, S)
nat(GA, 'The quarterly sales of a shop were 100, 150, 120, and 130 units. The average quarterly sales is ________.',
    125, S)


# ====================== Additional curated questions (58) ======================

S = 'Curated - Number Systems'
nat(DL, 'The decimal equivalent of the octal number (17)8 is ________.', 15, S)
nat(DL, 'The binary addition 1011 + 1101 equals ________ (enter the result as a decimal number).', 24, S)
nat(DL, 'The 1\'s complement of the 8-bit binary number 00001111 is ________ (enter as a decimal number).', 240, S)
nat(DL, 'The number of select lines required for a 64:1 multiplexer is ________.', 6, S)
nat(DL, 'A 4-bit ripple carry adder is built using ________ full adders.', 4, S)
mcq(DL, 'The characteristic equation Q(next) = T XOR Q belongs to the',
    'T flip-flop', ['D flip-flop', 'SR flip-flop', 'JK flip-flop'], 'Curated - Sequential Circuits')

S = 'Curated - CPU Performance'
nat(COA, 'A program has 10^9 instructions with an average CPI of 1.5. The clock rate is 3 GHz. '
         'The execution time (in seconds) is ________.', 0.5, S)
nat(COA, 'A cache has a hit rate of 90%, a hit time of 2 ns, and a miss penalty of 50 ns. '
         'The average memory access time (in ns) is ________.', 7, S)
mcq(COA, 'In a write-through cache, a write operation',
    'updates both the cache block and the corresponding main memory location',
    ['updates only the cache block', 'updates only the main memory', 'invalidates the cache block'], S)

S = 'Curated - Recursion & Trees'
nat(PDS, 'For the recursive function f(n) = n * f(n-1) with f(0) = 1, the value of f(6) is ________.', 720, S)
nat(PDS, 'In a complete binary tree with 15 nodes, the number of internal (non-leaf) nodes is ________.', 7, S)
nat(PDS, 'A binary search tree is built by inserting 5, 3, 7, 2, 4, 6, 8 in that order. '
         'The number of leaf nodes in the resulting tree is ________.', 4, S)
mcq(PDS, 'Inserting a node at the end of a singly linked list without a tail pointer takes',
    'O(n)', ['O(1)', 'O(log n)', 'O(n log n)'], 'Curated - Linked Lists')
nat(PDS, 'The number of comparisons required to find the maximum of an array of 100 elements is ________.', 99, S)
nat(PDS, 'On a 64-bit machine, the value of sizeof(int *) is ________ bytes.', 8, S)


def huffman_cost(freqs):
    h = list(freqs)
    heapq.heapify(h)
    total = 0
    while len(h) > 1:
        a = heapq.heappop(h)
        b = heapq.heappop(h)
        total += a + b
        heapq.heappush(h, a + b)
    return total


def knap01(weights, values, cap):
    best = 0
    n = len(weights)
    for mask in range(1 << n):
        w = v = 0
        for i in range(n):
            if mask & (1 << i):
                w += weights[i]
                v += values[i]
        if w <= cap and v > best:
            best = v
    return best


S = 'Curated - Graph Algorithms'
nat(ALG, 'The minimum spanning tree of a connected graph with 10 vertices has ________ edges.', 9, S)
nat(ALG, 'The frequencies of five characters are 5, 7, 10, 15, and 20. The total number of bits required '
         'to encode a file using Huffman coding (weighted external path length) is ________.',
    huffman_cost([5, 7, 10, 15, 20]), S)
nat(ALG, 'The number of swaps performed by bubble sort in the worst case on an array of 5 elements is ________.', 10, S)
nat(ALG, 'For the 0/1 knapsack problem with capacity 10, item weights [5, 4, 6, 3] and item values '
         '[10, 40, 30, 50], the maximum total value is ________.', knap01([5, 4, 6, 3], [10, 40, 30, 50], 10), S)
mcq(ALG, 'Dijkstra\'s algorithm implemented with a binary heap runs in',
    'O((V + E) log V)', ['O(V^2)', 'O(E^2)', 'O(V^3)'], S)
mcq(ALG, 'The space complexity of the Floyd-Warshall algorithm is',
    'O(V^2)', ['O(V)', 'O(E)', 'O(V^3)'], S)
nat(ALG, 'Using the tournament method, the number of comparisons to find both the minimum and maximum of '
         'an array of 100 elements is ________.', 148, S)
mcq(ALG, 'Building a binary heap from an array of n elements (bottom-up heapify) takes',
    'O(n)', ['O(n log n)', 'O(log n)', 'O(n^2)'], S)
mcq(ALG, 'The best-case time complexity of insertion sort on an array of n elements is',
    'O(n)', ['O(n log n)', 'O(n^2)', 'O(log n)'], S)

S = 'Curated - Memory Management'
nat(OS, 'A system has a 24-bit virtual address space and 4 KB pages. The number of page table entries '
        'in a single-level page table is ________.', 2 ** 12, S)
mcq(OS, 'In round robin scheduling, if the time quantum is larger than the largest burst time, the algorithm '
        'behaves like',
    'FCFS', ['SJF', 'SRTF', 'Priority scheduling'], S)
mcq(OS, 'When a process executes a P (wait) operation on a counting semaphore whose value is 0, the process',
    'blocks until another process performs a V (signal) operation',
    ['continues execution normally', 'terminates immediately', 'receives an error'], S)
nat(OS, 'A file of 100 blocks is stored using contiguous allocation starting at disk block 50. '
        'The number of disk accesses needed to read the entire file (given the starting block and length '
        'are already known) is ________.', 1, S)
mcq(OS, 'The FIFO page replacement policy can suffer from',
    'Belady\'s anomaly', ['internal fragmentation', 'thrashing', 'priority inversion'], S)
ref4 = [1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5]
nat(OS, f'For the page reference string {ref4} and 4 frames, the number of page faults using the LRU '
        f'replacement policy is ________.', page_faults(ref4, 4, 'lru'), S)


def opt_faults(ref, frames):
    mem, faults = [], 0
    for i, p in enumerate(ref):
        if p in mem:
            continue
        faults += 1
        if len(mem) < frames:
            mem.append(p)
        else:
            future = ref[i + 1:]
            victim = max(mem, key=lambda x: future.index(x) if x in future else 10 ** 9)
            mem.remove(victim)
            mem.append(p)
    return faults


nat(OS, f'For the page reference string {ref1} and 3 frames, the number of page faults using the optimal '
        f'replacement policy is ________.', opt_faults(ref1, 3), S)
nat(OS, f'For the page reference string {ref1} and 4 frames, the number of page faults using the optimal '
        f'replacement policy is ________.', opt_faults(ref1, 4), S)
mcq(OS, 'Threads belonging to the same process share',
    'the address space and open files', ['the stack', 'the register set', 'the program counter'], S)

S = 'Curated - Relational Algebra'
R3 = [(1, 5), (2, 3), (3, 8)]
S3 = [(4, 'a'), (6, 'b'), (9, 'c')]
cnt = sum(1 for a, b in R3 for c, d in S3 if b < c)
nat(DB, f'Relation R(A, B) has tuples {R3} and relation S(B, C) has tuples {S3}. '
        f'The number of tuples in the theta join R JOIN(R.B < S.B) S is ________.', cnt, S)
nat(DB, 'The natural join of R(A, B, C) and S(C, D) produces a relation with ________ attributes.', 4, S)
nat(DB, 'A relation with 2 attributes has ________ superkeys.', 4, S)
mcq(DB, 'A decomposition of R into R1 and R2 is lossless if and only if',
    'the common attributes R1 ∩ R2 form a superkey of R1 or R2',
    ['R1 and R2 have no common attributes',
     'R1 ∪ R2 contains all attributes of R',
     'both R1 and R2 are in BCNF'], S)
nat(DB, 'In a B+ tree of order 100, the maximum number of children of an internal node is ________.', 100, S)
nat(DB, 'Relation R(A, B) has 3 tuples with B = 1 and 2 tuples with B = 2. Relation S(B, C) has 4 tuples '
        'with B = 1 and 5 tuples with B = 2. The number of tuples in the natural join R JOIN S is ________.',
    3 * 4 + 2 * 5, S)
nat(DB, 'Consider the table T(x, y) with rows (1, 2), (1, 3), (2, 4), and (NULL, 5). '
        'The result of SELECT COUNT(*) FROM T WHERE x > 1 is ________.', 1, 'Curated - SQL')

S = 'Curated - Finite Automata'
nat(TOC, 'The minimum number of states in a DFA that accepts strings over {a, b} containing at least two a\'s '
        'is ________.', 3, S)
nat(TOC, 'The minimum number of final (accepting) states in a DFA that accepts strings over {a, b} ending '
        'with b is ________.', 1, S)
mcq(TOC, 'The language of all strings over {a, b} with an equal number of a\'s and b\'s is',
    'context-free but not regular', ['regular', 'finite', 'not context-free'], S)
nat(TOC, 'The number of strings of length 3 over {a, b} that end with a is ________.', 4, S)

S = 'Curated - IP Addressing & Routing'
nat(CN, 'If 3 bits are borrowed from the host portion of a class C network, the number of subnets created '
        'is ________.', 8, S)


def ones_complement_checksum(w1, w2):
    s = int(w1, 2) + int(w2, 2)
    while s >> 8:
        s = (s & 0xFF) + (s >> 8)
    return format(~s & 0xFF, '08b')


nat(CN, 'Using 8-bit 1\'s complement checksum, the checksum of the two words 11001100 and 10101010 is ________ '
        '(enter the 8-bit result as a decimal number).',
    int(ones_complement_checksum('11001100', '10101010'), 2), S)
nat(CN, 'A stop-and-wait protocol uses 1000-bit frames on a 1 Mbps link with a 20 ms round-trip time. '
        'The link utilization is ________ (enter as a decimal, rounded to 2 places).',
    round(1000 / (1e6 * 0.02), 2), S)
mcq(CN, 'In IPv4, fragmentation of a datagram is performed by',
    'the network layer at the routers along the path',
    ['the transport layer', 'the data link layer', 'the application layer'], S)

S = 'Curated - Lexical & Syntax Analysis'
nat(CD, 'The number of tokens produced for the statement "for (i = 0; i < 10; i++)" is ________ '
        '(count keywords, identifiers, constants, operators, and punctuation as tokens).', 13, S)
mcq(CD, 'The primary output of the lexical analysis phase is',
    'a stream of tokens', ['a parse tree', 'three-address code', 'a symbol table only'], S)
mcq(CD, 'Left recursion is eliminated from a grammar to make it suitable for',
    'top-down (recursive descent) parsing', ['bottom-up parsing', 'lexical analysis', 'code generation'], S)

S = 'Curated - Discrete Mathematics'
nat(EM, 'The number of functions from a set of 3 elements to a set of 2 elements is ________.', 8, S)
nat(EM, 'The number of one-to-one (injective) functions from a set of 3 elements to a set of 5 elements is ________.', 60, S)
nat(EM, 'The largest eigenvalue of the matrix [[3, 1], [1, 3]] is ________.', 4, S)
nat(EM, 'A fair coin is tossed 3 times. The probability of getting exactly 2 heads is ________ '
        '(round to 3 decimals).', round(3 / 8, 3), S)
nat(EM, 'The sum of the infinite geometric series 1 + 1/2 + 1/4 + 1/8 + ... is ________.', 2, S)

S = 'Curated - Quantitative Aptitude'
nat(GA, 'The ages of A and B are in the ratio 4 : 5 and their sum is 45. The age of A is ________.', 20, S)
nat(GA, 'A sum of money doubles itself in 8 years at simple interest. The annual rate of interest '
        'is ________ percent.', 12.5, S)
mcq(GA, 'Which of the following is the odd one out? 8, 27, 64, 100',
    '100', ['8', '27', '64'], S)

# ================================ GIFT output ================================
ABBR = {'Digital Logic': 'DL', 'Computer Organization': 'COA', 'Programming & Data Structures': 'PDS',
        'Algorithms': 'ALG', 'Operating Systems': 'OS', 'Databases': 'DB', 'Theory of Computation': 'TOC',
        'Computer Networks': 'CN', 'Compiler Design': 'CD', 'Engineering Mathematics': 'EM',
        'General Aptitude': 'GA'}


def build_gift():
    parts = []
    curcat = None
    counters = Counter()
    for q in sorted(Q, key=lambda x: x['subj']):
        cat = f'GATE CSE Curated/{q["subj"]}'
        if cat != curcat:
            parts.append(f'\n$CATEGORY: {cat}\n')
            curcat = cat
        counters[q['subj']] += 1
        title = f'Curated_{ABBR[q["subj"]]}_{counters[q["subj"]]:03d}'
        text = esc(q['text'])
        if q['type'] == 'mcq':
            items = []
            for opt, ok in q['opts']:
                items.append(('=' if ok else '~') + esc(opt))
            body = '{' + ' '.join(items) + '}'
        elif q['type'] == 'msq':
            k = sum(1 for _, ok in q['opts'] if ok)
            w = round(100 / k, 2)
            items = []
            for opt, ok in q['opts']:
                items.append((f'~%{w}%' if ok else '~%-100%') + esc(opt))
            body = '{' + ' '.join(items) + '}'
        else:
            body = '{#' + q['answer'] + '}'
        parts.append(f'::{title}::[plain]{text} {body}\n####Source: {esc(q["src"])}\n')
    return '\n'.join(parts)


def main():
    print(f'Total curated questions: {len(Q)}', file=sys.stderr)
    print('By subject:', dict(COUNTERS), file=sys.stderr)
    print('By type:', dict(Counter(q['type'] for q in Q)), file=sys.stderr)
    expected = {'Digital Logic': 38, 'Computer Organization': 17, 'Programming & Data Structures': 47,
                'Algorithms': 57, 'Operating Systems': 50, 'Databases': 41, 'Theory of Computation': 22,
                'Computer Networks': 12, 'Compiler Design': 11, 'Engineering Mathematics': 33,
                'General Aptitude': 25}
    ok = True
    for subj, n in expected.items():
        got = COUNTERS.get(subj, 0)
        if got != n:
            print(f'MISMATCH {subj}: expected {n}, got {got}', file=sys.stderr)
            ok = False
    if len(Q) != 353:
        print(f'MISMATCH total: expected 353, got {len(Q)}', file=sys.stderr)
        ok = False
    with open(OUT, 'w', encoding='utf-8') as f:
        f.write(build_gift())
    print(f'wrote {OUT} ({len(Q)} questions)', file=sys.stderr)
    if not ok:
        sys.exit(1)


if __name__ == '__main__':
    main()
