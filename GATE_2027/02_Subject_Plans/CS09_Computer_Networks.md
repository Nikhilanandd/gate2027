# CS09: Computer Networks — GATE 2027 CSE Study Plan

## Overview

| Metric | Detail |
|--------|--------|
| **Expected Marks** | 5–7 (1–2 MCQs + 1–2 NAT/MSQ) |
| **Difficulty** | Moderate-Easy (**reduced scope in 2027**) |
| **Scoring Potential** | High — scope reduced, easier to score |
| **Time Estimate** | 30–35 hours total |
| **Priority** | Medium |

> **GATE 2027 Update:** CN scope is **significantly reduced**. No OSI model detail, no circuit switching, simplified transport and security. Focus on application layer, IP, and routing.

---

## GATE 2027 Syllabus

### Data Link Layer
1. **Layering Concept** — Purpose of layers, service models, protocol concepts
2. **LAN / Ethernet** — Ethernet (IEEE 802.3), MAC addresses, CSMA/CD, switches, VLANs
3. **Framing** — Byte stuffing, bit stuffing
4. **Error Control** — CRC, Hamming code, parity

### Network Layer
5. **Routing** — Shortest path algorithms, flooding, distance vector (RIP), link state (OSPF), path vector (BGP basics)
6. **IPv4** — Addressing, subnetting, CIDR, NAT, ARP, ICMP, DHCP

### Transport Layer
7. **TCP** — Connection management (3-way handshake), reliable data transfer, flow control (sliding window), congestion control (slow start, congestion avoidance, fast retransmit, fast recovery)
8. **UDP** — Connectionless service, checksum

### Application Layer
9. **DNS** — Hierarchical naming, resolution, record types
10. **SMTP** — Email sending protocol
11. **HTTP** — Request/response methods, status codes, persistent connections
12. **FTP** — Control and data connections
13. **Email** — SMTP, POP3, IMAP basics

### Security Basics
14. **Network Security** — Symmetric/asymmetric encryption, digital signatures, certificates, SSL/TLS basics

---

## PYQ Weightage Analysis (2017–2026)

| Topic | Avg. Questions/Year | Avg. Marks/Year | Trend |
|-------|---------------------|-----------------|-------|
| IP Addressing & Subnetting | 1–2 | 2–3 | Stable, **most common** |
| Routing Algorithms | 1 | 1–2 | Stable |
| TCP (Flow/Congestion Control) | 1 | 1–2 | Stable |
| Application Layer (DNS, HTTP) | 0–1 | 0–1 | Moderate |
| Error Detection (CRC, Hamming) | 0–1 | 0–1 | Moderate |
| Ethernet / Data Link | 0–1 | 0–1 | Declining |

**Most Common PYQ Patterns:**
- IP subnetting and CIDR calculation
- CRC computation
- Hamming code error detection
- Dijkstra's/Floyd's for routing
- TCP window size and throughput
- DNS resolution process
- CRC and error detection numerical

---

## Topic-Wise Priority

| Topic | Priority | Why |
|-------|----------|-----|
| IP Addressing & Subnetting (CIDR) | **HIGHEST** | 2–3 marks guaranteed, numerical |
| Routing Algorithms | **HIGH** | Frequently tested, overlaps with algorithms |
| TCP (Flow/Congestion Control) | **HIGH** | Always tested, conceptual + numerical |
| Error Detection (CRC, Hamming) | **MEDIUM** | Moderate frequency, formulaic |
| DNS / Application Layer | **MEDIUM** | Occasionally tested |
| Ethernet / Framing | **LOW** | Simple, rarely tested in detail |

---

## Recommended Resources

### Free YouTube
| Resource | Topics |
|----------|--------|
| **Knowledge Gate (Sanchit Jain)** — CN | Best for GATE — exhaustive |
| **Neso Academy** — CN | Good for fundamentals |
| **Gate Smashers** — CN | Quick revision |

### Books
| Book | Use |
|------|-----|
| **Tanenbaum — Computer Networks** | Gold standard |
| **Forouzan — Data Communications and Networking** | Good for fundamentals |
| **Kurose & Ross — Computer Networking: A Top-Down Approach** | Application layer focus |

---

## Week-by-Week Study Plan (3.5 Weeks)

### Week 1: Data Link + Network Layer (10 hours)

| Day | Topic | Hours | Tasks |
|-----|-------|-------|-------|
| Day 1 | Layering + Ethernet + Framing | 2.5 | Layered model, Ethernet frame, CSMA/CD |
| Day 2 | Error Detection (CRC, Hamming) | 3 | CRC computation, Hamming code — solve 10 problems |
| Day 3 | IP Addressing + Subnetting | 2.5 | Classful, CIDR, subnet masks — solve 15 problems |
| Day 4 | NAT + ARP + ICMP | 2 | NAT translation, ARP process |

### Week 2: Routing + Transport (10 hours)

| Day | Topic | Hours | Tasks |
|-----|-------|-------|-------|
| Day 1 | Routing Algorithms | 3 | Dijkstra's, Bellman-Ford, distance vector, link state |
| Day 2 | Routing Protocols | 2 | RIP, OSPF, BGP differences |
| Day 3 | TCP (Connection + Reliable Transfer) | 2.5 | 3-way handshake, ACK, retransmission |
| Day 4 | TCP Flow + Congestion Control | 2.5 | Sliding window, slow start, congestion avoidance |

### Week 3: Application Layer + Security + Revision (10 hours)

| Day | Topic | Hours | Tasks |
|-----|-------|-------|-------|
| Day 1 | DNS | 2.5 | Resolution process, record types, caching |
| Day 2 | HTTP + SMTP + FTP | 2.5 | Request/response, status codes, email protocols |
| Day 3 | Security Basics | 2 | Symmetric/asymmetric crypto, digital signatures |
| Day 4 | PYQ Marathon | 3 | Solve 35 mixed CN PYQs |

### Week 3.5: Final Revision (5 hours)

| Day | Topic | Hours | Tasks |
|-----|-------|-------|-------|
| Day 1 | IP + Routing Revision | 2.5 | Re-solve subnetting and routing numericals |
| Day 2 | TCP + Application Layer Revision | 2.5 | Revise congestion control, DNS, HTTP |

---

## Key Concepts and Formulas to Master

### IP Addressing & CIDR
```
Class A: 1.0.0.0 – 126.255.255.255, Default mask: 255.0.0.0 (/8)
Class B: 128.0.0.0 – 191.255.255.255, Default mask: 255.255.0.0 (/16)
Class C: 192.0.0.0 – 223.255.255.255, Default mask: 255.255.255.0 (/24)

CIDR: /n means first n bits are network bits
Number of addresses = 2^(32-n)

Subnet mask: n bits of 1s followed by (32-n) bits of 0s
Network address: AND of IP and subnet mask
Broadcast address: OR of IP with complement of subnet mask
First usable: Network + 1
Last usable: Broadcast - 1
Number of hosts per subnet: 2^(32-n) - 2

Supernetting: combining multiple /n into /m (m < n)
  Example: 192.168.0.0/24 + 192.168.1.0/24 = 192.168.0.0/23
```

### Hamming Code
```
Data bits: d
Parity bits: r where 2^r ≥ d + r + 1

Positions: powers of 2 (1, 2, 4, 8, ...) are parity bits
Other positions are data bits

Parity bit p_i checks positions where i-th bit is 1
  p1: positions 1, 3, 5, 7, 9, 11, ... (bit 0 = 1)
  p2: positions 2, 3, 6, 7, 10, 11, ... (bit 1 = 1)
  p4: positions 4, 5, 6, 7, 12, 13, ... (bit 2 = 1)

Error detection: syndrome = binary position of error
  syndrome = 0 → no error
  syndrome = k → error at position k
```

### CRC
```
Generator polynomial G(x): divisor
Message M(x): dividend
CRC: remainder of M(x) × x^r / G(x) where r = degree of G(x)

Steps:
  1. Append r zeros to message
  2. Divide (message + zeros) by G(x) using XOR
  3. Remainder = CRC
  4. Transmitted: message + CRC
  5. Receiver divides by G(x) — if remainder = 0, no error
```

### TCP Congestion Control
```
Slow Start:
  cwnd starts at 1 MSS
  Doubles every RTT (exponential growth)
  Until cwnd ≥ ssthresh → switch to congestion avoidance

Congestion Avoidance:
  cwnd increases by 1 MSS per RTT (linear growth)
  On timeout: ssthresh = cwnd/2, cwnd = 1 MSS, restart slow start
  On triple duplicate ACK: ssthresh = cwnd/2, cwnd = ssthresh + 3 (fast recovery)

Fast Retransmit:
  Send 3 duplicate ACKs → retransmit immediately (don't wait for timeout)

TCP Throughput:
  Throughput ≈ (cwnd × MSS) / RTT
  Max throughput = W / RTT where W = window size
```

### TCP Flow Control
```
Receiver advertises window size (rwnd)
Sender window = min(cwnd, rwnd)

Sliding Window:
  Sender maintains send window
  Can send up to window size without ACK
  On ACK: slide window forward

Zero Window:
  When receiver window = 0: sender stops sending
  Sender sends probe packets periodically
```

### DNS
```
Resolution Process:
  1. Client checks local cache
  2. If miss → queries recursive resolver (ISP)
  3. Resolver checks root servers → TLD servers → authoritative server
  4. Response cached at each level

Record Types:
  A: domain → IPv4 address
  AAAA: domain → IPv6 address
  CNAME: alias → canonical name
  MX: domain → mail server
  NS: domain → name server
  PTR: IP → domain (reverse DNS)
```

### HTTP
```
Methods: GET, POST, PUT, DELETE, HEAD, OPTIONS
Status Codes:
  2xx: Success (200 OK, 201 Created)
  3xx: Redirection (301 Moved, 304 Not Modified)
  4xx: Client Error (400 Bad Request, 403 Forbidden, 404 Not Found)
  5xx: Server Error (500 Internal, 503 Service Unavailable)

Persistent Connection: multiple requests over single TCP connection
HTTP/1.1: persistent by default (keep-alive)
HTTP/2: multiplexing, header compression
```

---

## Common Mistake Patterns

| Mistake | How to Avoid |
|---------|--------------|
| Wrong subnet mask calculation | Count 1-bits from left; /n means n bits of 1 |
| Confusing network and broadcast address | Network: AND with mask; Broadcast: OR with complement |
| Hamming code position numbering | Start from 1 (not 0); powers of 2 are parity bits |
| CRC remainder calculation errors | Use polynomial long division (XOR), not regular division |
| TCP window size confusion | Send window = min(cwnd, rwnd) |
| Congestion control state machine error | Slow start → (ssthresh) → congestion avoidance; timeout → slow start |
| DNS resolution order error | Root → TLD → Authoritative (not the reverse) |
| HTTP status code misclassification | 2xx = success, 3xx = redirect, 4xx = client error, 5xx = server error |
| CIDR supernetting errors | Check that addresses are contiguous before combining |
| Routing protocol confusion | RIP = distance vector, OSPF = link state, BGP = path vector |

---

## PYQ Practice Strategy

### Phase 1: IP Addressing + Routing (Week 1–2)
- Solve 25 IP subnetting PYQs
- Solve 15 routing algorithm PYQs

### Phase 2: TCP + Error Detection (Week 2–3)
- Solve 15 TCP congestion/flow control problems
- Solve 10 CRC/Hamming problems

### Phase 3: Mixed Practice (Week 3)
- Solve 35 mixed CN PYQs in 50 minutes
- Focus on numerical problems

### Key PYQ Problem Types
1. IP subnetting — find network, broadcast, first/last host
2. CIDR — number of addresses, supernetting
3. Hamming code — find error position, correct
4. CRC — compute CRC, detect errors
5. Dijkstra's — shortest path routing table
6. TCP window — throughput calculation
7. DNS — resolution trace
8. Congestion control — cwnd behavior over time

---

## Topic-Wise Time Estimates

| Topic | Study Time | Practice Time | Total |
|-------|------------|---------------|-------|
| Layering + Ethernet | 2 hrs | 1.5 hrs | 3.5 hrs |
| Error Detection (CRC, Hamming) | 3 hrs | 3 hrs | 6 hrs |
| IP Addressing + CIDR | 4 hrs | 4 hrs | 8 hrs |
| Routing Algorithms | 4 hrs | 3 hrs | 7 hrs |
| TCP (Flow/Congestion) | 4 hrs | 3 hrs | 7 hrs |
| Application Layer | 3 hrs | 2 hrs | 5 hrs |
| Security Basics | 1.5 hrs | 1 hr | 2.5 hrs |
| **Total** | **21.5 hrs** | **17.5 hrs** | **39 hrs** |

---

## Quick Revision Checklist

- [ ] IP subnet mask from CIDR notation
- [ ] Network and broadcast address calculation
- [ ] Hamming code — parity bit positions and syndrome calculation
- [ ] CRC computation steps
- [ ] Dijkstra's algorithm for routing
- [ ] Distance vector vs link state differences
- [ ] TCP 3-way handshake and 4-way teardown
- [ ] Slow start, congestion avoidance, fast retransmit, fast recovery
- [ ] DNS resolution hierarchy (root → TLD → authoritative)
- [ ] HTTP methods and status codes
- [ ] RIP, OSPF, BGP — which layer, which algorithm
