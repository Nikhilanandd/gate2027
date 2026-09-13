# GATE 2027 — CSE Preparation Ecosystem

> **Organized by:** IIT Madras | **Exam:** Feb 6–21, 2027 | **Portal:** [gate2027.iitm.ac.in](https://gate2027.iitm.ac.in)

---

## Repository Structure

```
GATE/
├── CS_GATE2027_Syllabus.pdf          # Official syllabus PDF
├── generate_trackers.py              # Python script to regenerate XLSX trackers
│
└── GATE_2027/
    ├── 01_Planning/                  # Strategy & schedules
    │   ├── MASTER_PLAN.md            # 4-phase timeline, subject priorities, hour targets
    │   ├── DAILY_SCHEDULE.md         # 3 schedule variants (college/no college/weekend)
    │   └── WEEKLY_PLANNER.md         # 7-day template, progress tracker, mock analysis
    │
    ├── 02_Subject_Plans/             # One detailed plan per subject
    │   ├── CS01_Digital_Logic.md
    │   ├── CS02_Computer_Organization.md
    │   ├── CS03_Programming_Data_Structures.md
    │   ├── CS04_Algorithms.md
    │   ├── CS05_Theory_of_Computation.md
    │   ├── CS06_Compiler_Design.md
    │   ├── CS07_Operating_Systems.md
    │   ├── CS08_Databases.md
    │   ├── CS09_Computer_Networks.md
    │   └── CS10_Engineering_Mathematics.md
    │
    ├── 03_Resources/                 # Books, courses, test series
    │   ├── RESOURCE_GUIDE.md         # Free YouTube + paid resources with prices
    │   └── BUYING_CHECKLIST.md       # Budget tiers (₹0 → ₹15k+), deadlines
    │
    ├── 04_Trackers/                  # XLSX progress trackers (open in Excel/Sheets)
    │   ├── SYLLABUS_TRACKER.xlsx     # Per-topic completion status
    │   ├── PYQ_ANALYSIS.xlsx         # PYQ practice log 2015-2026
    │   ├── MOCK_TEST_LOG.xlsx        # 20 mock tests + score trends
    │   ├── ERROR_LOG.xlsx            # Mistake tracking with categories
    │   └── REVISION_CALENDAR.xlsx    # 24-week schedule + daily hours log
    │
    └── 05_Revision/                  # Final months strategy
        └── FINAL_REVISION_PLAN.md    # Last 4 weeks day-by-day + exam day tactics
```

---

## Quick Start

### 1. Read First
| Priority | File | Why |
|----------|------|-----|
| 🔴 | `01_Planning/MASTER_PLAN.md` | Know the full picture — dates, phases, targets |
| 🔴 | `01_Planning/DAILY_SCHEDULE.md` | Pick a schedule variant that fits your college routine |
| 🟡 | `03_Resources/BUYING_CHECKLIST.md` | What to buy and when (with deadlines) |

### 2. Track Progress Daily
- Open `04_Trackers/REVISION_CALENDAR.xlsx` → Log study hours
- Open `04_Trackers/ERROR_LOG.xlsx` → Log every mistake
- Open `04_Trackers/SYLLABUS_TRACKER.xlsx` → Mark topics done

### 3. Weekly Routine
- **Monday–Saturday:** Follow `WEEKLY_PLANNER.md` daily themes
- **Sunday:** Mock test → Log in `MOCK_TEST_LOG.xlsx` → Analyze → Update error log

### 4. Regenerate Trackers
```bash
python3 generate_trackers.py
```

---

## Subject Priority (by expected marks)

| # | Subject | Expected | Priority | Plan |
|---|---------|----------|----------|------|
| 1 | Engineering Mathematics | 12–14 | HIGH | `CS10_*.md` |
| 2 | Programming & Data Structures | 8–11 | HIGHEST | `CS03_*.md` |
| 3 | Operating Systems | 8–10 | HIGHEST | `CS07_*.md` |
| 4 | Algorithms | 7–9 | HIGH | `CS04_*.md` |
| 5 | Database Management Systems | 7–9 | HIGH | `CS08_*.md` |
| 6 | Theory of Computation | 5–7 | MEDIUM | `CS05_*.md` |
| 7 | Computer Networks | 5–7 | MEDIUM | `CS09_*.md` |
| 8 | Computer Organization | 4–6 | MEDIUM | `CS02_*.md` |
| 9 | Digital Logic | 3–5 | MEDIUM | `CS01_*.md` |
| 10 | Compiler Design | 3–5 | MEDIUM | `CS06_*.md` |
| 11 | General Aptitude | 15 | HIGH | Covered in `MASTER_PLAN.md` |

---

## Key Dates

| Date | Event |
|------|-------|
| **Sep 27, 2026** | GATE registration deadline (regular) |
| **Oct 5, 2026** | Extended registration (late fee) |
| **Jan 4, 2027** | City allotment notification |
| **Feb 6, 7, 13, 14, 20, 21, 2027** | Exam days |
| **Mar 19, 2027** | Results |

---

## GATE 2027 Changes vs 2026

- **New paper:** Robotics & Automation (RA)
- **Digital Logic updated:** explicit minimization techniques + circuit design
- **COA updated:** hardwired vs microprogrammed control, cache mapping
- **CN scope reduced:** removed OSI/TCP-IP comparison, switching, MAC, network security, UDP
- All other CSE sections unchanged

---

## License

For personal use only. Not for redistribution.
