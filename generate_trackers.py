#!/usr/bin/env python3
"""Generate 5 XLSX tracker files for GATE 2027 CSE preparation."""

import os
from datetime import date, timedelta

from openpyxl import Workbook
from openpyxl.styles import (
    Alignment,
    Border,
    Font,
    NamedStyle,
    PatternFill,
    Side,
    numbers,
)
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

OUTPUT_DIR = "/home/nikhil/Documents/GATE/GATE_2027/04_Trackers"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ── Style constants ──────────────────────────────────────────────────────────
HEADER_FONT = Font(name="Calibri", bold=True, color="FFFFFF", size=11)
BODY_FONT = Font(name="Calibri", size=10)
THIN_BORDER = Border(
    left=Side(style="thin"),
    right=Side(style="thin"),
    top=Side(style="thin"),
    bottom=Side(style="thin"),
)
WRAP = Alignment(wrap_text=True, vertical="top")
CENTER = Alignment(horizontal="center", vertical="center", wrap_text=True)

HEADER_FILLS = {
    "blue": PatternFill(start_color="1F4E79", end_color="1F4E79", fill_type="solid"),
    "green": PatternFill(start_color="2E7D32", end_color="2E7D32", fill_type="solid"),
    "orange": PatternFill(start_color="E65100", end_color="E65100", fill_type="solid"),
    "red": PatternFill(start_color="B71C1C", end_color="B71C1C", fill_type="solid"),
    "purple": PatternFill(start_color="4A148C", end_color="4A148C", fill_type="solid"),
}

ALT_ROW_FILL = PatternFill(start_color="F2F7FB", end_color="F2F7FB", fill_type="solid")


# ── Helpers ──────────────────────────────────────────────────────────────────
def style_header(ws, num_cols, fill_key="blue"):
    fill = HEADER_FILLS[fill_key]
    for col in range(1, num_cols + 1):
        cell = ws.cell(row=1, column=col)
        cell.font = HEADER_FONT
        cell.fill = fill
        cell.alignment = CENTER
        cell.border = THIN_BORDER


def style_body(ws, num_rows, num_cols):
    for r in range(2, num_rows + 1):
        for c in range(1, num_cols + 1):
            cell = ws.cell(row=r, column=c)
            cell.font = BODY_FONT
            cell.border = THIN_BORDER
            cell.alignment = WRAP
            if r % 2 == 0:
                cell.fill = ALT_ROW_FILL


def auto_width(ws, num_cols, min_w=12, max_w=35):
    for col in range(1, num_cols + 1):
        letter = get_column_letter(col)
        lengths = []
        for cell in ws[letter]:
            if cell.value:
                lengths.append(len(str(cell.value)))
        best = max(lengths) if lengths else min_w
        ws.column_dimensions[letter].width = min(max(best + 2, min_w), max_w)


def add_validation(ws, cell_range, formula_list):
    dv = DataValidation(type="list", formula1=f'"{formula_list}"', allow_blank=True)
    dv.error = f"Choose from: {formula_list}"
    dv.errorTitle = "Invalid Entry"
    dv.showErrorMessage = True
    ws.add_data_validation(dv)
    dv.add(cell_range)


def freeze_top(ws):
    ws.freeze_panes = "A2"


# ── GATE CSE Syllabus Data ──────────────────────────────────────────────────
SYLLABUS = {
    "Engineering Mathematics": {
        "Linear Algebra": [
            "Matrix Algebra",
            "Systems of Linear Equations",
            "Eigenvalues & Eigenvectors",
            "LU Decomposition",
        ],
        "Calculus": [
            "Limits & Continuity",
            "Differentiability",
            "Maxima & Minima",
            "Mean Value Theorem",
            "Integration",
        ],
        "Probability & Statistics": [
            "Counting Techniques",
            "Conditional Probability",
            "Bayes Theorem",
            "Random Variables (PDF/CDF)",
            "Distributions (Binomial/Poisson/Normal)",
            "Mean/Variance/Std Dev",
        ],
        "Discrete Mathematics": [
            "Propositional & First-Order Logic",
            "Sets & Relations",
            "Functions",
            "Partial Orders & Lattices",
            "Graphs (matching, coloring, connectivity)",
            "Combinatorics (recurrence, generating functions)",
        ],
        "Numerical Methods": [
            "Roots of Equations (Bisection/Newton-Raphson)",
            "Interpolation & Extrapolation",
            "Numerical Integration",
        ],
    },
    "Digital Logic": {
        "Boolean Algebra": [
            "Boolean Functions",
            "Canonical & Standard Forms",
            "Minimization (K-map, Quine-McCluskey)",
        ],
        "Combinational Circuits": [
            "Multiplexers & Demux",
            "Encoders & Decoders",
            "Adders & Subtractors",
            "Code Converters",
        ],
        "Sequential Circuits": [
            "Latches & Flip-Flops",
            "Counters (Synchronous/Asynchronous)",
            "Shift Registers",
            "Finite State Machines",
        ],
        "Number Systems": [
            "Representation (Binary/Octal/Hex)",
            "Signed Magnitude / 1's / 2's Complement",
        ],
    },
    "Computer Organization & Architecture": {
        "Machine Instructions": [
            "Addressing Modes",
            "Instruction Formats",
            "Machine Cycles & Pipelining",
        ],
        "Memory System": [
            "Hierarchy (Cache/Main/Virtual)",
            "Cache Mapping & Replacement",
            "Cache Performance",
            "Virtual Memory & TLB",
        ],
        "I/O Organization": [
            "Interrupts & DMA",
            "I/O Techniques (Programmed/Interrupt/DMA)",
        ],
        "Pipeline": [
            "Instruction Pipeline",
            "Data Hazards & Control Hazards",
            "Branch Prediction",
        ],
    },
    "Programming & Data Structures": {
        "Programming in C": [
            "Functions & Recursion",
            "Pointers & Arrays",
            "Structures & Unions",
            "File Handling",
            "Preprocessor Directives",
        ],
        "Data Structures": [
            "Arrays & Strings",
            "Linked Lists (Singly/Doubly/Circular)",
            "Stacks & Queues",
            "Trees (BST, AVL, B/B+ Trees)",
            "Graphs (BFS/DFS/Representation)",
            "Hashing (Collision Resolution)",
            "Heap & Priority Queue",
        ],
        "Algorithms": [
            "Asymptotic Complexity (Big-O/Theta/Omega)",
            "Divide & Conquer",
            "Greedy Algorithms",
            "Dynamic Programming",
            "Backtracking",
            "Branch & Bound",
        ],
        "Sorting & Searching": [
            "Merge Sort / Quick Sort / Heap Sort",
            "Bubble / Insertion / Selection Sort",
            "Counting / Radix / Bucket Sort",
            "Linear Search / Binary Search",
        ],
        "Graph Algorithms": [
            "Shortest Path (Dijkstra/Bellman-Ford/Floyd)",
            "MST (Prim/Kruskal)",
            "Topological Sort",
            "Strongly Connected Components",
            "Bipartiteness",
        ],
        "Algorithm Design Paradigms": [
            "Activity Selection (Greedy)",
            "0/1 Knapsack (DP)",
            "Longest Common Subsequence (DP)",
            "Matrix Chain Multiplication (DP)",
            "N-Queens (Backtracking)",
        ],
    },
    "Algorithms": {
        "Complexity Analysis": [
            "Asymptotic Notations",
            "Recurrence Relations (Master Theorem)",
            "Amortized Analysis",
        ],
        "Algorithm Paradigms": [
            "Divide and Conquer",
            "Greedy",
            "Dynamic Programming",
            "Backtracking",
        ],
        "Graph Algorithms": [
            "BFS & DFS Applications",
            "Shortest Path Algorithms",
            "MST Algorithms",
            "Network Flow",
        ],
        "Computational Complexity": [
            "P vs NP",
            "NP-Completeness & Reductions",
            "Travelling Salesman (NP-Hard)",
        ],
    },
    "Theory of Computation": {
        "Automata Theory": [
            "DFA & NFA",
            "Regular Expressions",
            "Equivalence of DFA/NFA/RE",
            "Closure Properties",
            "Minimization of DFA",
        ],
        "Context-Free Languages": [
            "Context-Free Grammars",
            "Pushdown Automata",
            "Normal Forms (CNF/GNF)",
            "Closure Properties",
            "Parsing Ambiguity",
        ],
        "Turing Machines": [
            "Standard TM",
            "Variants of TM",
            "Halting Problem",
            "Decidability & Undecidability",
            "Recursively Enumerable Languages",
        ],
        "Complexity Theory": [
            "P, NP, NP-Hard, NP-Complete",
            "Polynomial Time Reductions",
            "Cook-Levin Theorem (SAT)",
        ],
    },
    "Compiler Design": {
        "Lexical Analysis": [
            "Regular Expressions to DFA",
            "NFA to DFA Conversion",
            "Lexical Analyser Generators (Lex)",
        ],
        "Syntax Analysis": [
            "CFG & Parse Trees",
            "LL(1) Parsing",
            "LR(0)/SLR(1)/LALR(1)/CLR(1) Parsing",
            "Operator Precedence Parsing",
        ],
        "Semantic Analysis": [
            "Syntax-Directed Definitions",
            "Type Checking",
            "Symbol Tables",
        ],
        "Code Generation & Optimization": [
            "Intermediate Representations (3-Address Code)",
            "Code Optimization Techniques",
            "Code Generation (Target Code)",
            "Register Allocation",
        ],
        "Runtime Environments": [
            "Stack Allocation",
            "Heap Allocation",
        ],
    },
    "Operating System": {
        "Process Management": [
            "Process & Thread Concepts",
            "CPU Scheduling (FCFS/SJF/RR/Priority/MLFQ)",
            "Process Synchronization (Mutex/Semaphore)",
            "Deadlock (Detection/Prevention/Avoidance)",
            "Banker's Algorithm",
        ],
        "Memory Management": [
            "Paging & Segmentation",
            "Page Replacement (FIFO/LRU/OPT/LFU)",
            "Allocation Strategies",
            "Thrashing & Working Set",
        ],
        "File Systems": [
            "File Allocation Methods",
            "Directory Structure",
            "Disk Scheduling (FCFS/SSTF/SCAN/C-SCAN)",
            "Free Space Management",
        ],
        "I/O Management": [
            "I/O Systems & Controllers",
            "Buffering & Caching",
            "Spooling",
        ],
    },
    "Databases": {
        "Relational Model": [
            "ER Model to Relational Mapping",
            "Relational Algebra & Calculus",
            "SQL (DDL/DML/DCL/TCL)",
            "Joins (Inner/Outer/Cartesian)",
            "Normalization (1NF to BCNF)",
            "Functional Dependencies & Closure",
        ],
        "Transaction Management": [
            "ACID Properties",
            "Serializability (Conflict/View)",
            "Recoverability",
            "Concurrency Control (2PL/Timestamp/MVCC)",
            "Recovery (Shadow Paging/Log-based)",
        ],
        "Indexing & Hashing": [
            "B+ Tree Indexing",
            "Hash Indexing",
            "Query Processing & Optimization",
            "Cost Estimation",
        ],
        "NoSQL & Advanced": [
            "NoSQL Concepts",
            "Stored Procedures & Triggers",
            "Views & Authorization",
        ],
    },
    "Computer Networks": {
        "Physical & Data Link": [
            "OSI & TCP/IP Models",
            "Signal Encoding (NRZ/Manchester/AMI)",
            "Channel Capacity (Nyquist/Shannon)",
            "Framing & Error Detection/Correction",
            "Flow Control (Stop-and-Wait/Sliding Window)",
            "ARQ Protocols",
        ],
        "MAC & LLC": [
            "CSMA/CD & Ethernet",
            "CSMA/CA & Wireless LAN (802.11)",
            "Token Ring",
            "Switching & VLANs",
        ],
        "Network Layer": [
            "IPv4 Addressing & Subnetting",
            "IPv6",
            "Routing (RIP/OSPF/BGP)",
            "ICMP & ARP",
            "NAT & DHCP",
        ],
        "Transport Layer": [
            "TCP & UDP",
            "TCP Connection Management",
            "TCP Flow Control & Congestion",
            "Ports & Sockets",
        ],
        "Application Layer": [
            "DNS",
            "HTTP/HTTPS",
            "FTP",
            "SMTP/POP3/IMAP",
            "SNMP",
        ],
        "Network Security": [
            "Symmetric & Asymmetric Encryption",
            "Digital Signatures & Certificates",
            "Firewalls",
        ],
    },
}

PYQ_TOPICS = {
    "Engineering Mathematics": 15,
    "Digital Logic": 5,
    "Computer Organization & Architecture": 8,
    "Programming & Data Structures": 10,
    "Algorithms": 10,
    "Theory of Computation": 8,
    "Compiler Design": 5,
    "Operating System": 10,
    "Databases": 10,
    "Computer Networks": 9,
}

SUBJECT_SHORT = {
    "Engineering Mathematics": "Math",
    "Digital Logic": "DL",
    "Computer Organization & Architecture": "COA",
    "Programming & Data Structures": "PDS",
    "Algorithms": "Algo",
    "Theory of Computation": "TOC",
    "Compiler Design": "Compiler",
    "Operating System": "OS",
    "Databases": "DBMS",
    "Computer Networks": "CN",
}


# ═════════════════════════════════════════════════════════════════════════════
# FILE 1: SYLLABUS_TRACKER.xlsx
# ═════════════════════════════════════════════════════════════════════════════
def create_syllabus_tracker():
    wb = Workbook()

    # ── Sheet 1: Syllabus Status ─────────────────────────────────────────
    ws1 = wb.active
    ws1.title = "Syllabus Status"
    ws1.sheet_properties.tabColor = "1F4E79"

    headers1 = [
        "Subject", "Topic", "Sub-topic", "GATE_2027_Status", "Priority",
        "Difficulty", "Status", "Notes", "Resources", "Target_Week",
    ]
    ws1.append(headers1)
    style_header(ws1, len(headers1), "blue")

    row_idx = 2
    for subj, topics in SYLLABUS.items():
        priority = "High" if PYQ_TOPICS.get(subj, 5) >= 10 else (
            "Medium" if PYQ_TOPICS.get(subj, 5) >= 6 else "Low"
        )
        for topic, subtopics in topics.items():
            for st in subtopics:
                ws1.append([subj, topic, st, "Not Started", priority, "", "Not Started", "", "", ""])
                row_idx += 1

    num_rows = ws1.max_row
    style_body(ws1, num_rows, len(headers1))
    freeze_top(ws1)
    auto_width(ws1, len(headers1))

    # Data validations
    add_validation(ws1, "D2:D1000", "Not Started,In Progress,First Pass Done,Revised,Mastered")
    add_validation(ws1, "E2:E1000", "High,Medium,Low")
    add_validation(ws1, "F2:F1000", "Easy,Medium,Hard,Very Hard")
    add_validation(ws1, "G2:G1000", "Not Started,In Progress,First Pass Done,Revised,Mastered")

    # ── Sheet 2: Subject Summary ─────────────────────────────────────────
    ws2 = wb.create_sheet("Subject Summary")
    ws2.sheet_properties.tabColor = "2E7D32"

    headers2 = [
        "Subject", "Total Topics", "Not Started", "In Progress",
        "First Pass", "Revised", "Mastered", "% Complete",
    ]
    ws2.append(headers2)
    style_header(ws2, len(headers2), "green")

    subjects = list(SYLLABUS.keys())
    last_data_row = 1 + sum(
        len(sub) for topics in SYLLABUS.values() for sub in topics.values()
    )

    for i, subj in enumerate(subjects, start=2):
        ws2.cell(row=i, column=1, value=subj)
        subject_range = f"'Syllabus Status'"
        # COUNTIFS formula to count per subject
        ws2.cell(
            row=i, column=2,
            value=f'=COUNTIFS({subject_range}!A$2:A${last_data_row},A{i},{subject_range}!A$2:A${last_data_row},"<>")',
        )
        ws2.cell(
            row=i, column=3,
            value=f'=COUNTIFS({subject_range}!A$2:A${last_data_row},A{i},{subject_range}!G$2:G${last_data_row},"Not Started")',
        )
        ws2.cell(
            row=i, column=4,
            value=f'=COUNTIFS({subject_range}!A$2:A${last_data_row},A{i},{subject_range}!G$2:G${last_data_row},"In Progress")',
        )
        ws2.cell(
            row=i, column=5,
            value=f'=COUNTIFS({subject_range}!A$2:A${last_data_row},A{i},{subject_range}!G$2:G${last_data_row},"First Pass Done")',
        )
        ws2.cell(
            row=i, column=6,
            value=f'=COUNTIFS({subject_range}!A$2:A${last_data_row},A{i},{subject_range}!G$2:G${last_data_row},"Revised")',
        )
        ws2.cell(
            row=i, column=7,
            value=f'=COUNTIFS({subject_range}!A$2:A${last_data_row},A{i},{subject_range}!G$2:G${last_data_row},"Mastered")',
        )
        ws2.cell(
            row=i, column=8,
            value=f'=IF(B{i}=0,0,ROUND((F{i}+G{i})/B{i}*100,1))',
        )
        ws2.cell(row=i, column=8).number_format = '0.0"%"'

    style_body(ws2, len(subjects) + 1, len(headers2))
    freeze_top(ws2)
    auto_width(ws2, len(headers2))

    path = os.path.join(OUTPUT_DIR, "SYLLABUS_TRACKER.xlsx")
    wb.save(path)
    return path


# ═════════════════════════════════════════════════════════════════════════════
# FILE 2: PYQ_ANALYSIS.xlsx
# ═════════════════════════════════════════════════════════════════════════════
def create_pyq_analysis():
    wb = Workbook()

    # ── Sheet 1: PYQ by Year ─────────────────────────────────────────────
    ws1 = wb.active
    ws1.title = "PYQ by Year"
    ws1.sheet_properties.tabColor = "E65100"

    headers1 = [
        "Year", "Subject", "Topic", "Question", "Marks", "Type",
        "Difficulty", "My_Attempt", "Correct", "Time_Sec",
        "Error_Type", "Notes",
    ]
    ws1.append(headers1)
    style_header(ws1, len(headers1), "orange")

    subjects = list(SYLLABUS.keys())
    for year in range(2015, 2027):
        for idx, subj in enumerate(subjects[:4]):  # sample a few per year
            ws1.append([year, subj, "", "", "", "", "", "", "", "", "", ""])
    style_body(ws1, ws1.max_row, len(headers1))
    freeze_top(ws1)
    auto_width(ws1, len(headers1))

    add_validation(ws1, "F2:F2000", "MCQ,MSQ,NAT")
    add_validation(ws1, "G2:G2000", "Easy,Medium,Hard,Very Hard")
    add_validation(ws1, "H2:H2000", "Yes,No,Partial")
    add_validation(ws1, "I2:I2000", "Yes,No")
    add_validation(ws1, "K2:K2000",
                   "Conceptual,Silly,Time Pressure,Not Attempted,Calculation")

    # ── Sheet 2: PYQ Statistics ──────────────────────────────────────────
    ws2 = wb.create_sheet("PYQ Statistics")
    ws2.sheet_properties.tabColor = "F57C00"

    headers2 = [
        "Subject", "Total_Questions", "Correct", "Accuracy_%",
        "Avg_Time", "Strong_Topics", "Weak_Topics",
    ]
    ws2.append(headers2)
    style_header(ws2, len(headers2), "orange")

    for i, subj in enumerate(subjects, start=2):
        ws2.cell(row=i, column=1, value=subj)
        src = "'PYQ by Year'"
        ws2.cell(
            row=i, column=2,
            value=f'=COUNTIF({src}!B$2:B$2000,A{i})',
        )
        ws2.cell(
            row=i, column=3,
            value=f'=COUNTIFS({src}!B$2:B$2000,A{i},{src}!I$2:I$2000,"Yes")',
        )
        ws2.cell(
            row=i, column=4,
            value=f'=IF(B{i}=0,0,ROUND(C{i}/B{i}*100,1))',
        )
        ws2.cell(
            row=i, column=5,
            value=f'=IF(B{i}=0,"",ROUND(AVERAGEIFS({src}!J$2:J$2000,{src}!B$2:B$2000,A{i}),0)&"s")',
        )

    style_body(ws2, len(subjects) + 1, len(headers2))
    freeze_top(ws2)
    auto_width(ws2, len(headers2))

    path = os.path.join(OUTPUT_DIR, "PYQ_ANALYSIS.xlsx")
    wb.save(path)
    return path


# ═════════════════════════════════════════════════════════════════════════════
# FILE 3: MOCK_TEST_LOG.xlsx
# ═════════════════════════════════════════════════════════════════════════════
def create_mock_test_log():
    wb = Workbook()

    # ── Sheet 1: Mock Tests ──────────────────────────────────────────────
    ws1 = wb.active
    ws1.title = "Mock Tests"
    ws1.sheet_properties.tabColor = "4A148C"

    headers1 = [
        "Date", "Test_Source", "Test_Name", "Total_Marks", "GA_Marks",
        "Subject_Marks", "Score", "Percentile_Est", "Time_Taken",
        "Questions_Attempted", "Correct", "Accuracy_%",
        "Top_3_Strengths", "Top_3_Weaknesses", "Action_Items",
    ]
    ws1.append(headers1)
    style_header(ws1, len(headers1), "purple")

    for i in range(1, 21):
        ws1.append([f"Mock {i}", "", "", 100, "", "", "", "", "", "", "", "", "", "", ""])
    style_body(ws1, 21, len(headers1))
    freeze_top(ws1)
    auto_width(ws1, len(headers1))

    add_validation(ws1, "B2:B21", "GATE Academy,MADE Easy,Unacademy,Self-Made,Previous Year Full")
    add_validation(ws1, "M2:N21", "PDS,Algo,OS,DBMS,TOC,CN,COA,DL,Compiler,Math,GA")

    # ── Sheet 2: Score Trend ─────────────────────────────────────────────
    ws2 = wb.create_sheet("Score Trend")
    ws2.sheet_properties.tabColor = "7B1FA2"

    headers2 = [
        "Mock_Number", "Date", "Score", "GA", "PDS", "Algo", "OS",
        "DBMS", "TOC", "CN", "COA", "DL", "Compiler", "Math",
    ]
    ws2.append(headers2)
    style_header(ws2, len(headers2), "purple")

    for i in range(1, 21):
        ws2.append([i, "", "", "", "", "", "", "", "", "", "", "", "", ""])
    style_body(ws2, 21, len(headers2))
    freeze_top(ws2)
    auto_width(ws2, len(headers2))

    # Add note
    note_row = 23
    ws2.cell(row=note_row, column=1,
             value="TIP: Select the data in rows 2-21 and insert a Line Chart to visualize score trends.")
    ws2.cell(row=note_row, column=1).font = Font(
        name="Calibri", italic=True, color="7B1FA2", size=10
    )
    ws2.merge_cells(f"A{note_row}:N{note_row}")

    path = os.path.join(OUTPUT_DIR, "MOCK_TEST_LOG.xlsx")
    wb.save(path)
    return path


# ═════════════════════════════════════════════════════════════════════════════
# FILE 4: ERROR_LOG.xlsx
# ═════════════════════════════════════════════════════════════════════════════
def create_error_log():
    wb = Workbook()

    # ── Sheet 1: Error Log ───────────────────────────────────────────────
    ws1 = wb.active
    ws1.title = "Error Log"
    ws1.sheet_properties.tabColor = "B71C1C"

    headers1 = [
        "Date", "Source", "Subject", "Topic", "Question_Ref",
        "My_Answer", "Correct_Answer", "Error_Type", "Root_Cause",
        "Concept_to_Revise", "Revise_By", "Revised_YN", "Notes",
    ]
    ws1.append(headers1)
    style_header(ws1, len(headers1), "red")

    style_body(ws1, 2, len(headers1))
    freeze_top(ws1)
    auto_width(ws1, len(headers1))

    add_validation(ws1, "B2:B10000", "PYQ,Mock,Practice")
    add_validation(ws1, "H2:H10000",
                   "Conceptual,Careless,Time_Pressure,Misread,Calculation,Method_Wrong")
    add_validation(ws1, "L2:L10000", "Yes,No")

    # ── Sheet 2: Error Summary ───────────────────────────────────────────
    ws2 = wb.create_sheet("Error Summary")
    ws2.sheet_properties.tabColor = "D32F2F"

    headers2 = [
        "Subject", "Conceptual", "Careless", "Time_Pressure", "Misread",
        "Calculation", "Method_Wrong", "Total_Errors",
    ]
    ws2.append(headers2)
    style_header(ws2, len(headers2), "red")

    subjects = list(SYLLABUS.keys())
    src = "'Error Log'"
    for i, subj in enumerate(subjects, start=2):
        ws2.cell(row=i, column=1, value=subj)
        ws2.cell(row=i, column=2,
                 value=f'=COUNTIFS({src}!C$2:C$10000,A{i},{src}!H$2:H$10000,"Conceptual")')
        ws2.cell(row=i, column=3,
                 value=f'=COUNTIFS({src}!C$2:C$10000,A{i},{src}!H$2:H$10000,"Careless")')
        ws2.cell(row=i, column=4,
                 value=f'=COUNTIFS({src}!C$2:C$10000,A{i},{src}!H$2:H$10000,"Time_Pressure")')
        ws2.cell(row=i, column=5,
                 value=f'=COUNTIFS({src}!C$2:C$10000,A{i},{src}!H$2:H$10000,"Misread")')
        ws2.cell(row=i, column=6,
                 value=f'=COUNTIFS({src}!C$2:C$10000,A{i},{src}!H$2:H$10000,"Calculation")')
        ws2.cell(row=i, column=7,
                 value=f'=COUNTIFS({src}!C$2:C$10000,A{i},{src}!H$2:H$10000,"Method_Wrong")')
        ws2.cell(row=i, column=8,
                 value=f'=SUM(B{i}:G{i})')

    style_body(ws2, len(subjects) + 1, len(headers2))
    freeze_top(ws2)
    auto_width(ws2, len(headers2))

    path = os.path.join(OUTPUT_DIR, "ERROR_LOG.xlsx")
    wb.save(path)
    return path


# ═════════════════════════════════════════════════════════════════════════════
# FILE 5: REVISION_CALENDAR.xlsx
# ═════════════════════════════════════════════════════════════════════════════
def create_revision_calendar():
    wb = Workbook()

    # ── Sheet 1: Weekly Revision ─────────────────────────────────────────
    ws1 = wb.active
    ws1.title = "Weekly Revision"
    ws1.sheet_properties.tabColor = "00695C"

    headers1 = [
        "Week_Number", "Date_Range", "Subjects_Planned", "Topics_to_Revise",
        "Resources_to_Use", "Hours_Planned", "Hours_Actual",
        "Completion_%", "Notes",
    ]
    ws1.append(headers1)
    HEADER_FILL_TEAL = PatternFill(start_color="00695C", end_color="00695C", fill_type="solid")
    for col in range(1, len(headers1) + 1):
        cell = ws1.cell(row=1, column=col)
        cell.font = HEADER_FONT
        cell.fill = HEADER_FILL_TEAL
        cell.alignment = CENTER
        cell.border = THIN_BORDER

    start_date = date(2026, 9, 1)
    for week in range(1, 25):
        week_start = start_date + timedelta(weeks=week - 1)
        week_end = week_start + timedelta(days=6)
        date_range = f"{week_start.strftime('%b %d')} - {week_end.strftime('%b %d, %Y')}"
        ws1.append([week, date_range, "", "", "", "", "", "", ""])

    num_rows = ws1.max_row
    style_body(ws1, num_rows, len(headers1))
    freeze_top(ws1)
    auto_width(ws1, len(headers1))

    add_validation(ws1, "C2:C25",
                   "PDS,Algo,OS,DBMS,TOC,CN,COA,DL,Compiler,Math,GA,Multiple")

    # ── Sheet 2: Daily Log ───────────────────────────────────────────────
    ws2 = wb.create_sheet("Daily Log")
    ws2.sheet_properties.tabColor = "00897B"

    headers2 = [
        "Date", "Day", "Subject_1", "Hours_1", "Subject_2", "Hours_2",
        "Subject_3", "Hours_3", "Total_Hours", "Revision_Done",
        "PYQ_Practice", "Mock_Test", "Notes",
    ]
    ws2.append(headers2)
    HEADER_FILL_TEAL2 = PatternFill(start_color="00897B", end_color="00897B", fill_type="solid")
    for col in range(1, len(headers2) + 1):
        cell = ws2.cell(row=1, column=col)
        cell.font = HEADER_FONT
        cell.fill = HEADER_FILL_TEAL2
        cell.alignment = CENTER
        cell.border = THIN_BORDER

    day_names = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    current = date(2026, 9, 1)
    end_date = date(2027, 2, 20)
    row_idx = 2
    while current <= end_date:
        ws2.append([
            current.strftime("%Y-%m-%d"),
            day_names[current.weekday()],
            "", "", "", "", "", "", "", "", "", "", "",
        ])
        # Total_Hours formula = SUM of Hours columns
        ws2.cell(
            row=row_idx, column=9,
            value=f"=SUM(D{row_idx},F{row_idx},H{row_idx})",
        )
        row_idx += 1
        current += timedelta(days=1)

    style_body(ws2, ws2.max_row, len(headers2))
    freeze_top(ws2)
    auto_width(ws2, len(headers2))

    add_validation(ws2, f"C2:C{ws2.max_row}",
                   "PDS,Algo,OS,DBMS,TOC,CN,COA,DL,Compiler,Math,GA")
    add_validation(ws2, f"E2:E{ws2.max_row}",
                   "PDS,Algo,OS,DBMS,TOC,CN,COA,DL,Compiler,Math,GA")
    add_validation(ws2, f"G2:G{ws2.max_row}",
                   "PDS,Algo,OS,DBMS,TOC,CN,COA,DL,Compiler,Math,GA")
    add_validation(ws2, f"J2:J{ws2.max_row}", "Yes,No")
    add_validation(ws2, f"K2:K{ws2.max_row}", "Yes,No")
    add_validation(ws2, f"L2:L{ws2.max_row}", "Yes,No")

    path = os.path.join(OUTPUT_DIR, "REVISION_CALENDAR.xlsx")
    wb.save(path)
    return path


# ═════════════════════════════════════════════════════════════════════════════
# Main
# ═════════════════════════════════════════════════════════════════════════════
def main():
    generators = [
        ("SYLLABUS_TRACKER.xlsx", create_syllabus_tracker),
        ("PYQ_ANALYSIS.xlsx", create_pyq_analysis),
        ("MOCK_TEST_LOG.xlsx", create_mock_test_log),
        ("ERROR_LOG.xlsx", create_error_log),
        ("REVISION_CALENDAR.xlsx", create_revision_calendar),
    ]

    print("=" * 65)
    print("  GATE 2027 CSE Tracker Generator")
    print("=" * 65)

    for name, fn in generators:
        path = fn()
        size = os.path.getsize(path)
        if size > 1024:
            size_str = f"{size / 1024:.1f} KB"
        else:
            size_str = f"{size} B"
        print(f"  [OK] {name:<25s}  {size_str:>8s}  -> {path}")

    print("=" * 65)
    print("  All 5 tracker files generated successfully.")
    print("=" * 65)


if __name__ == "__main__":
    main()
