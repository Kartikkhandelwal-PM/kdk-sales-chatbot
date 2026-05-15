"""
Generates KDK-Sales-Agent-KnowledgeBase.md
Comprehensive AI sales agent training document combining:
  - Product features (GST, TDS, ITR)
  - DIY vs DIFM segment USPs
  - Competitor comparison tables
  - Sales pitches, questionnaire, objection handling
"""
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

OUT = Path(__file__).parent / "KDK-Sales-Agent-KnowledgeBase.md"

DOC = """# KDK Software — AI Sales Agent Knowledge Base
> **Purpose:** This document trains the AI sales agent with complete product knowledge, competitor intelligence, segment-specific pitches, and objection handling for Express GST, Express TDS, and Express ITR.

---

# PART 1 — ABOUT KDK SOFTWARE

KDK Software is a leading Indian tax-technology company providing cloud-based compliance software for GST, TDS, and Income Tax filing. Their flagship suite — Express GST, Express TDS, and Express ITR — runs on the **Spectrum Cloud** platform.

## Core Platform Advantages
- **Fully cloud-based** — work from anywhere, anytime, any device. No system dependency, no data loss risk.
- **Two segments served:** DIY (enterprises managing own compliance) and DIFM (CAs/tax professionals managing client compliance)
- **VAPT certified** with ISO-27001 security, 2-Factor Authentication, and end-to-end encryption
- **Integrated suite** — GST, TDS, and ITR in one platform with unified client data
- **Inbuilt "Call Me" support** — click a button, get an instant call from support. No waiting on hold.
- **Auto data sync** from government portals from the registration date — no manual fetching
- **Mobile app** available for on-the-go access
- **Budget-friendly pricing** — pay as per requirement, easy to upgrade

---

# PART 2 — UNDERSTANDING CLIENT SEGMENTS

## DIY — Do It Yourself (Enterprises / Businesses)
**Who they are:** Companies, businesses, and corporates managing their own GST/TDS/ITR compliance in-house.

**What they need:**
- Automation to reduce manual work
- Speed and accuracy in return filing
- Error detection before submission to avoid notices and penalties
- Reports and analytics for business decisions
- Secure, centralized data storage

**Key pain points:**
- System dependency with desktop software — data loss risk
- Manual reconciliation taking too much time
- Missing notices leading to heavy penalties
- No graphical visibility into compliance health
- Team productivity issues with multiple logins

**Pitch angle for DIY:** "You're doing your own compliance — let Express software automate 80% of it. One dashboard, auto-sync from the government portal, instant error detection, and reports at one click. Your team does less manual work and makes zero errors."

---

## DIFM — Do It For Me (CAs / Chartered Accountants / Tax Professionals)
**Who they are:** Chartered Accountants, tax practitioners, and accounting firms managing compliance for tens or hundreds of clients.

**What they need:**
- Bulk client management from a single screen
- Productivity tools to serve more clients with the same team
- Automated reports and client communication (emails, notices, returns)
- User access control for team members
- Data security for client confidentiality

**Key pain points:**
- Logging into each client separately for notices, returns, challans
- Manually downloading and emailing reports to clients
- No unified dashboard across all clients
- System-dependent desktop software limiting remote work
- Team members accessing wrong client data — security risk

**Pitch angle for DIFM:** "You manage 100+ clients and your team spends 60% of their time on repetitive tasks — downloading reports, checking notices one by one, emailing 2B data manually. Express automates all of that. Send 2B data to all clients on the 15th automatically. See all notices on one screen. Your team serves 2x the clients in the same time."

---

## Bundle Clients (GST + TDS + ITR Together)
**Who they are:** Either large enterprises handling all three compliances internally, or CA firms offering complete compliance services to clients.

**Why bundle:**
- One platform login — no switching between tools
- Unified client master across all three products
- Data synergy: GST turnover flows into ITR; TDS data integrates across products
- Single support relationship — one team, one point of contact
- Consistent UI — team learns once, uses everywhere
- Single renewal, single contract, bundle pricing advantage
- Complete compliance under one roof — from transaction to return to audit

**Pitch angle for Bundle:** "Instead of managing 3 vendors with 3 support teams and 3 different logins, get everything under one roof at KDK. Your GST data connects to your ITR. Your TDS is filed from the same place. One login, one team, one bill. And when something goes wrong, one call fixes it all."

---

# PART 3 — EXPRESS GST

## Product Overview
Express GST is a cloud-based GST compliance software for filing GST returns, doing reconciliation, managing e-invoicing, and e-way bills. It serves both enterprises (DIY) and CA firms (DIFM).

## Key Features

### Return Filing
- GSTR-1 (with all 19 heads, single-window view)
- GSTR-1A, IFF (Invoice Furnishing Facility)
- GSTR-3B (auto-prepared from GSTR-1 & 2B with validations)
- GSTR-6 and GSTR-6A (ISD distribution)
- GSTR-9 (Annual Return) with auto-email to clients
- GSTR-9C (auto-prepared)

### Reconciliation
- GSTR-2A / GSTR-2B vs Books reconciliation in just 4 clicks
- No invoice count limit (competitors cap at 10,000 or 30,000)
- Conflict reports: In 2A not in 2B, ITC Eligibility conflict, POS conflict, RCM conflict
- Monthly, multi-month, and annual reconciliation reports
- Auto Tally sync — no manual export required

### E-Invoice & E-Way Bill (DIY)
- E-Invoice generation directly from Express GST (DIY segment) — no separate portal needed
- E-Way Bill generation, cancellation, update, and management
- R1 vs E-Way Bill reconciliation
- R1 vs E-Invoice comparison

### Data Import & Integration
- Tally connector (including Client PC option — unique to Express GST)
- Excel import (blank template and pre-filled)
- JSON import
- Connection with all major ERPs
- Auto-fetch from GST portal from registration date on client creation

### Dashboards & Reports
- Single-window graphical dashboard: Sales by R1, Purchase by 2A, Tax Liability, ITC trends
- PAN-level multi-branch dashboard and reconciliation
- Notices & Orders: all clients on one screen, reply status, PDF download
- IMS (Invoice Management System) dashboard with bulk actions
- Ledger statements: Cash, Credit, Non-Return Liability, PMT-09 — since 2017
- GSTN Insights: all registration details on one screen
- Return Register: auto-sent 2x per week via email

### Automation
- Schedule 2A/2B auto-email to all clients on the 15th of every month
- Auto return register email twice a week
- Auto-fetch data from registration date
- Auto-detect suspended / suo-moto cancelled GSTNs and move to B2C
- DRC-01(B) and 86(b) validations in GSTR-3B

### Unique Features
- **ITC Tracker** — track ITC claims and reversals
- **Lost ITC Tracker** — identify ITC that should have been claimed
- **Rule 37A compliance** — suppliers who haven't paid tax (reversal required)
- **Rule 42 & 43** — ITC reversal tracking
- **PAN-based Tax Audit Ready Report**
- **Conflict Summary report**
- **Books vs R1 comparison** (invoice level in DIY)
- **Cross-charge report**
- **HSN Summary for GSTR-9**
- **Annual ITC Comparison**
- **GSTR-1 vs 3B vs Books comparison**
- **Vendor Management**
- **2-Factor Authentication** + User Management (unlimited users)
- Inbuilt **"Call Me"** support button — instant connection

---

## EXPRESS GST — USPs by Segment

### For DIY (Enterprises)
1. **ITC Reversed Rule 37 & 37A** — automatic identification and calculation
2. **Rule 42 & 43** — ITC reversal tracking for partial-use assets
3. **PAN-based Tax Audit Ready Report** — saves audit preparation time
4. **R1 vs E-Way Bill reconciliation** — catch mismatches before notice
5. **IMS Dashboard** — manage all incoming supplier invoices in bulk
6. **Debit Notes** — proper tracking and reconciliation
7. **2A/2B Dashboard** with detailed amendment tracking
8. **Vendor Management** — track supplier compliance
9. **Conflict Summary** — see all reconciliation conflicts in one place
10. **Lost ITC Tracker** — recover ITC you may have missed claiming
11. **Books vs R1** — invoice-level comparison
12. **User Management** — unlimited users with role-based access
13. **2-Factor Authentication** — enterprise-grade data security
14. **PAN Wise Reports** — multi-GSTIN business view
15. **Books vs 6A** — ISD reconciliation
16. **Cross-charge Report** — for businesses with multiple branches
17. **Books vs E-Way Bill** — freight and supply verification
18. **PAN Level data import** — import sales for all branches in one step
19. **Connection with All ERPs** — seamless integration
20. **No Dependency on Team Members** — data available from 2017, anyone can access
21. **Easy Migration** from any existing software
22. **Return Register** — always up to date, no manual tracking
23. **Detailed Amendment 2A/2B Dashboard** — track all amended invoices
24. **R1 vs 3B vs Books** — three-way comparison at a glance
25. **R1 vs E-Invoice** — ensure GST portal and e-invoice data match
26. **HSN Summary** — ready for GSTR-9 without extra work
27. **GSTR-9 Email** — send annual returns to clients automatically
28. **Auto Prepare GSTR-9C** — reduces annual return preparation time significantly

### For DIFM (CAs / Tax Professionals)
1. **Cloud-based** — work from office, home, or client site — no system dependency
2. **Auto 2B data email to all clients on the 15th** — zero manual effort
3. **Notice & Replies** — all clients' notices on one screen, track reply status
4. **IMS vs. Purchases register** — help clients reconcile purchases with IMS
5. **Remote Client PC Tally Sync** — sync Tally data even from client's PC remotely
6. **Exhaustive User Rights Management** — control exactly what each team member sees
7. **Import PAN-level sales data to GSTR-1** — file for multi-GSTIN clients efficiently
8. **Office Management Summary** — overview of all client work status
9. **Increase Productivity and Revenue** — serve more clients in less time
10. **Best Support in Industry** — dedicated team, instant "Call Me" feature
11. **Auto Populated Return Register** — know every client's return status without checking
12. **Ledger Balances** — view without logging into GST portal
13. **GSTR-1 vs E-Way Bill** — reconciliation for all clients
14. **IMS with Bulk Actions** — process multiple client invoices simultaneously
15. **Client Dashboards** — GSTIN Summary per client in one view
16. **Migrate from any software in minutes** — onboard new clients fast
17. **Mobile App** — check client status on the go
18. **Centralized Repository** — all client data in one secure place
19. **Single Dashboard View** — complete summary without switching screens
20. **VAPT Certified + Encryption** — client data is secure and compliant

---

## EXPRESS GST — Competitor Comparison

### vs All Competitors (Summary Table)

| Feature | Express GST | Web GST | My GST Cafe | Winman | Tax Pro | CompuGST | Easy GST | Speqta GST | ClearTax | EasemyGST | SCI GST | GEN GST |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Platform** | ✅ Cloud | ❌ Desktop | Both | ❌ Desktop | Online+Offline | No segments | ✅ Cloud | ❌ Desktop | ✅ Cloud | ✅ Cloud | ❌ Desktop | Both |
| **DIY & DIFM Segments** | ✅ Both | ❌ No | Both | ❌ No | ❌ No | ❌ No | ❌ No | ❌ No | ✅ Cloud | ✅ Cloud | ❌ No | ❌ No |
| **Bulk Client Import** | ✅ Auto-fetch + Excel | One-by-one | One-by-one | One-by-one | Excel only | Single only | One-by-one | Complex Excel | Manual/Excel | Manual | No Excel import | One-by-one |
| **Return Register Auto-Email** | ✅ 2x/week | ❌ Manual | No mail | Monthly only | Manual | Excel only | ❌ Not available | Available | Available | ❌ Not available | Higher version | Available |
| **Notices & Orders (all clients)** | ✅ One screen + reply | One-by-one + captcha | View only, no status | ❌ Not available | ❌ Not available | Single client | ❌ Not available | Redirects to portal | ❌ Not available | ❌ Not available | ❌ Not available | Captcha each time |
| **Auto 2A/2B Email (15th)** | ✅ All clients auto | ❌ Manual | ❌ Manual | ❌ Manual | ❌ Manual | ❌ Not available | ❌ Not available | Manual each client | ❌ No | ❌ No | ❌ Not available | ❌ Not available |
| **Reconciliation Conflict Report** | ✅ ITC, POS, RCM, 2A-not-2B | Partial | No conflict rpt | 30K cap | Basic | Excel only | Bank only | GSTR-2A & 1 | Manual run | 15-min process | Excel only | Partial match only |
| **Auto Data Fetch (Reg. Date)** | ✅ On client creation | ❌ Manual | ❌ Manual | ❌ Manual | ❌ Manual | ❌ Manual | Captcha/year | PC only | Manual | Manual | Auto populate | Captcha |
| **Client PC Tally Sync** | ✅ Available | ❌ No | ❌ No | ❌ No | ❌ No | ❌ No | ❌ No | ❌ No | ❌ No | ❌ No | ❌ No | ❌ No |
| **Graphical Dashboard** | ✅ Full graphical | Multiple windows | Multiple windows | Multiple windows | ❌ None | Different pages | Basic only | Multiple pages | Basic tabs | Sales+Purchase | ❌ Not available | Very difficult |
| **E-Invoice (DIY)** | ✅ Available | ❌ Not available | ERP-based | 3-day delay | API-based | 2-day delay | ❌ Not available | ❌ Not available | ❌ Not available | ✅ Available | ❌ Not available | ✅ Available |
| **Bulk Report Download** | ✅ One click all | One-by-one | One-by-one | One-by-one | One-by-one | One-by-one | One-by-one | One-by-one | Single page click | Single page click | One-by-one | One-by-one |
| **Support** | ✅ Call Me button | Phone number | Phone number | 30-min wait | Phone number | Available | Support number | Anydesk ticket | Self-help portal | Support number | Number only | Number only |
| **No Run-Reco Needed** | ✅ No need | – | – | – | – | – | – | ❌ Must run each time | – | Auto | – | – |
| **Ledger Since 2017** | ✅ All 5 types | Cash+ITC+Reversal | Without PMT-09 | ❌ Not available | – | Download from start | ❌ Not available | – | – | Period-wise | – | – |

### vs ClearTax (Detailed)

| Feature | **Express GST** | ClearTax |
|---|---|---|
| Platform | Cloud | Cloud |
| Reconciliation | Advanced 2A/2B — invoice & supplier level + conflict reports | AI-based matching engine |
| GSTR-3B Filing | **Auto-prepares from GSTR-1 & 2B + 100+ validations** | Supports with validations |
| GSTR-1/IFF | Excel/Tally + **100+ validation checks** | Excel/Tally import |
| Notice/Audit Management | ✅ **Central notice tracking with reply status** | ❌ Basic reports only, no notice module |
| Software Speed | **7x faster** | Slow in comparison |
| Data Migration | **Bulk import for all clients** | Single client creation only |
| Return Reminder | **Auto-email twice/week for all clients** | No mail facility |
| Data Fetching | **Auto-fetch from registration date + Tally auto-sync** | Manual import required |
| Report Download | **Single click for all 12 months** | Not available |
| Budget | **Price per requirement, easy upgrade** | Standard price — expensive for CAs |
| Configuration | **All accounting software + advanced Tally from any location** | Only Excel + Tally, same location only |
| Advanced Features | Schedule 2A/2B, Notices, ITR integration, full taxation suite | Return filing and reco only |
| Target | CAs + multi-GSTIN businesses | SMEs and corporates |

---

# PART 4 — EXPRESS TDS

## Product Overview
Express TDS is a cloud-based TDS/TCS return filing software for preparing and submitting 24Q, 26Q, 27Q, and 27EQ returns. It serves both enterprises managing their own TDS (DIY) and CA firms filing TDS for clients (DIFM).

## Key Features

### Return Filing
- 24Q (Salary TDS), 26Q (Non-Salary), 27Q (Foreign Payments), 27EQ (TCS)
- FVU generation — **Java-FREE** (no technical issues on peak days)
- CSI file — **auto-fetched**, no manual portal generation needed
- Correction returns with online correction facility

### Challan Management
- **Auto-import from Govt portal** on deductor creation — no manual sync
- **Drag & Drop challan mapping** — map single or multiple TDS entries simultaneously
- Map single TDS entry with multiple challans
- Unconsumed challan visibility with auto-sync
- Challan deletion process

### Client & Master Management
- Multiple import options: **Excel, TXT file, TDS file auto-scan**
- Bulk deductor creation (no one-by-one manual entry)
- Deductee master: add, edit, activate/deactivate in bulk
- Financial year selection and change

### Certificates & Correspondence
- Form 16, 16A, 27D generation
- **DSC digital signing** of certificates
- **Direct email to deductees** — no manual mail composition (DIY)
- TDS filed return acknowledgement (PDF)

### TRACES Integration
- Consolidated file import for correction returns
- **All request status on one screen** — no one-by-one TRACES checking
- Justification report (raise, download, generate)
- Lower Deduction Certificate verification

### Dashboards & Reports
- **Health Analysis Report** — Invalid PAN, unverified challan, late fees, interest, LDC issues — all in one Excel
- **Computation & Health Report** — MIS: TDS computation, late fee, interest, LDC verification, challan status, PAN verification
- **Graphical view** — Deductee details, PAN status, compliance, liability (last 5 quarters)
- **Notices & Orders** — all deductors on one screen, reply status, PDF download
- **Return Register** — auto-maintained, PDF download available
- **TAN Insights** — all TAN registration info on single click
- 3CD Annexure Report (DIY segment)

### Automation
- **Bulk PAN verification** — single click, verifies 1.5 lakh+ PANs rapidly (speed-up feature unique to Express TDS)
- **Auto interest and late fee allocation** from unconsumed challans
- **Deductee-wise entry email** (DIY) — send payment details to each deductee
- Salary TDS Calculator

---

## EXPRESS TDS — Competitor Comparison

### vs All TDS Competitors (Summary Table)

| Feature | **Express TDS** | Clear TDS | GEN TDS | Compu TDS | Webtel TDS | TDS Man |
|---|---|---|---|---|---|---|
| **Platform** | ✅ Cloud | ✅ Cloud | ❌ Desktop | ❌ Desktop | Cloud (but buffering) | ❌ Desktop |
| **DIY & DIFM** | ✅ Both | ✅ Both | ❌ One segment | ❌ One segment | Enterprise plan only | ✅ Both (Desktop) |
| **Bulk Client Import** | ✅ Excel + TXT + TDS auto-scan | ❌ No bulk import | TXT file only | TXT file only | ❌ One-by-one | ✅ Multiple options |
| **Return Register** | ✅ Auto + PDF | Select per client | Auto but per-client download | Auto but Excel download each time | Manual update | Filing status only |
| **Notices & Orders** | ✅ All clients, one screen | ❌ Not available | ❌ Not available | ❌ Not available | Enterprise plan only | ❌ Not available |
| **Request Status** | ✅ All deductors, one screen | One-by-one | Manual TRACES | Manual TRACES | ❌ Not available | – |
| **TAN Insights** | ✅ One click, all info | Manual TRACES login | – | ❌ Not available | ❌ Not available | Manual portal |
| **Java Required** | ✅ Java-FREE | ✅ Java-free | ❌ Java REQUIRED | ❌ Java REQUIRED | ❌ Frequent updates needed | Java required |
| **Bulk PAN Verification Speed** | ✅ 1.5L+ PANs fast | Slow | Desktop-dependent, slow | Desktop-dependent, slow | Available | – |
| **Challan Auto-Import** | ✅ On deductor creation | Manual sync | Manual one-by-one | Manual one-by-one | Captcha required | Manual, redirects |
| **Challan Mapping** | ✅ Drag & Drop | ❌ No drag & drop | One-by-one | One-by-one | Manual selection | One-by-one |
| **TDS Certificates + Email** | ✅ 16/16A/27D + DSC + Email | Available | DSC yes, ❌ No email | ❌ No DSC (needs 3rd party PDF signer) | Available | PDF Converter needed |
| **CSI File** | ✅ Auto-fetch | ✅ Auto | ❌ Manual portal login | ❌ Manual portal login | – | Auto-tick option |
| **Health Analysis Report** | ✅ Comprehensive, single Excel | ❌ Not available | Partial, multiple windows | ❌ Not available | ❌ Not available | Separate pages |
| **Graphical View** | ✅ 5-quarter deductee + compliance view | ❌ Not available | ❌ Not available | ❌ Not available | ❌ Not available | ❌ Not available |
| **3CD Annexure (DIY)** | ✅ Available | ✅ Available | ✅ Available | ✅ Available | ❌ Not available | ❌ Not available |
| **Deductee-wise Email (DIY)** | ✅ Direct email | – | ❌ Manual compose | ❌ Manual compose | – | – |
| **Auto Interest/Late Fee Adjust** | ✅ Unconsumed challan auto-adjust | – | – | – | – | – |

### vs ClearTax/ClearTDS (Detailed)

| Dimension | **Express TDS** | ClearTax / ClearTDS |
|---|---|---|
| Ease of Use | Simple, intuitive; drag & drop challans | Structured workflow; strong validation |
| Validation | **100+ checks; early warnings; navigation to errors** | Only PAN and challan validation |
| TRACES Integration | **Full conso file import + certificates** | Depends on TRACES portal — slow |
| Challan Handling | **Drag-drop; unconsumed challan visibility + auto-sync** | Challan verification only |
| TDS Certificates | **Form 16, 16A, 27D + DSC signing + direct email** | Form 16/16A only |
| FVU | Java-free | FVU + Aadhaar OTP e-filing |
| Notices & Orders | ✅ **All deductors, one screen, apply justification** | ❌ Not available |
| Pending Request Status | ✅ **Multi-client, multi-request, one screen** | ❌ Not available |
| Auto Interest/Late Fee | ✅ **Auto-adjust with unconsumed challan** | ❌ Not available |
| Health & Computation Report | ✅ **Full MIS (TDS, late fee, interest, LDC, challan, PAN)** | ❌ Not available |
| Validation + Error Navigation | ✅ **Before FVU with error navigation to fix quickly** | ❌ Not available |
| Client Creation | **User ID/PW + Excel + TXT + TDS auto-scan** | Limited options |
| Security | Cloud + **2FA + ISO-27001 + encryption** | Not highlighted |
| Budget | **Price per requirement, easy to upgrade** | Standard price — expensive for CAs |

---

# PART 5 — EXPRESS ITR

## Product Overview
Express ITR (on Spectrum Cloud) is a cloud-based Income Tax Return preparation and filing software covering ITR-1 to ITR-7 for individuals, firms, companies, and trusts. It serves both enterprises (DIY) and CA firms (DIFM).

## Key Features

### Return Types Supported
- ITR-1 to ITR-7
- Regular, Belated, and Revised returns
- ITR-U (Updated Return) filing

### Income & Data Feeding
- Salary income with HRA calculation
- House property income
- Capital gains (import via broker template, Excel, or manual entry)
- Business income: regular, presumptive (44AD, 44ADA, 44AE), speculative, intraday, F&O
- Other sources income
- Agricultural income, Exempt income
- Virtual Digital Assets (Schedule VDA)
- Foreign assets details
- Clubbing income
- Pass-Through Income (Schedule PTI)
- Specified Business Income (Section 35AD)

### Deductions & Tax Calculations
- 80C, 80D, 80CCD(2) (NPS employer contribution), 80GG (rent paid), 80P, 80PA, 80IAC
- Advance Tax calculator and payment tracking
- Challan payment
- Carry forward TDS and set-off claims (Rule 5A/37BA)
- Previous year's carried forward TDS claim
- Tax rate change for companies, AOP/BOI, trusts

### Import & Integration
- **Form 16 import** — auto-populate salary details
- **AIS/26AS direct import** — no manual TRACES download
- **GST Turnover import** from GST portal into ITR
- 3CB-3CD Excel import with PDF clause download
- 3CD JSON import
- Capital gain import: broker templates, Excel
- Schedule III data import via Excel
- JSON file import from previous years
- Bulk client import: individual, Excel, JSON, auto-scan

### Audit & Financial Statements
- Tax Audit Forms: 3CA-3CB-3CD preparation
- Balance sheet and P&L preparation
- Schedule III financial statements (preview and download)
- Depreciation chart — IT Act and Companies Act
- Auditor master creation and management
- Significant Accounting Policies
- Method of Accounting
- Quantitative Details (Schedule QD)
- Inventory Details
- Key Persons / Ownership Information
- Holding and Subsidiary Company details
- Directors and Shareholders information

### Dashboards & Reports
- **Return Register** — auto maintained
- **Notices & Orders** — all clients on one screen + PDF download
- **Previous year data comparison** in dashboard
- **PAN Insights** — auto validation + error detection
- Computation PDF download
- Downloaded AIS/26AS PDF
- Notice & Orders view and download
- Error Locator — must clear all errors before JSON download (no risky filings)
- **User Management** — unlimited users

---

## EXPRESS ITR — Competitor Comparison

### vs All ITR Competitors (Summary Table)

| Feature | **Express ITR (Spectrum Cloud)** | Winman ITR | ClearTax | CompuTax | Genius |
|---|---|---|---|---|---|
| **Platform** | ✅ Cloud | ❌ Desktop | ✅ Cloud | ❌ Desktop | ❌ Desktop |
| **Client Creation** | ✅ Individual + Bulk Excel + JSON + Auto-Scan | Individual only | Individual only | Manual only | One option |
| **Return Register** | ✅ Auto + PDF download | ❌ Not available | Basic | Complex layout | Basic overview |
| **Notices & Orders** | ✅ One screen + PDF + save demand | ❌ Not available | ❌ Not available | ❌ Not available | ❌ Not available |
| **Previous Year Comparison** | ✅ Auto, in dashboard | Manual | Manual portal download | ❌ Not available | ❌ Not possible |
| **PAN Insights** | ✅ Auto validation + early error detection | Basic only | Basic check | Limited | Standard |
| **AIS/26AS Import** | ✅ Direct import | Manual | Manual TRACES | Manual TRACES | Manual TRACES |
| **3CB-3CD** | ✅ Excel import + PDF clauses | JSON import | Manual | Supported | Limited |
| **User Management** | ✅ Unlimited users | Subscription-based | ❌ Not available | ❌ Not available | ❌ Not available |
| **Error Locator** | ✅ Must clear before JSON download | ❌ Can download with errors (risk of revised return) | Blocks on errors | Blocks on errors | Blocks on errors |
| **Data Security** | ✅ Cloud + encrypted | ❌ Desktop risk | ✅ Cloud | ❌ Desktop risk | ❌ Desktop risk |
| **Benefit** | Work anywhere, data safe | – | Cloud access | – | – |

---

# PART 6 — BUNDLE PITCH (GST + TDS + ITR)

## When to Recommend the Bundle
Recommend the full bundle when:
- Client is a **CA firm** offering complete compliance services (GST filing + TDS filing + ITR filing for clients)
- Client is a **large enterprise** managing all three compliances internally
- Client mentions pain of using multiple software from different vendors
- Client wants to reduce vendor management overhead

## Bundle Pitch Script

**Opening:** "Let me ask you something — how many different software tools are you currently using for GST, TDS, and income tax? And how many support numbers do you have to call when something breaks?"

**Pain Point:** "Most businesses and CA firms use 2 or 3 different software tools. They have different logins, different interfaces, different renewal dates, and different support teams. Your staff has to learn three different systems. When data changes in GST, you have to manually update ITR. When a TDS payment changes, nothing connects."

**Solution:** "With KDK's Express suite — GST, TDS, and ITR together — all your data lives in one place. Your GST turnover feeds directly into your ITR. Your client master is created once and used across all three. Your team logs in once. You call one support number. You get one bill."

**Key Bundle Benefits:**
- **Unified client master** — create client once, use across GST, TDS, ITR
- **Data flow** — GST turnover auto-imports into ITR; TDS data integrates
- **One login** — single dashboard, no tool switching
- **Bundle pricing** — better per-product price than buying separately
- **Single support** — one team handles everything; no blame-shifting between vendors
- **Consistent UI** — staff learns once, works everywhere
- **Single renewal** — one contract, one renewal date, easy budgeting
- **Complete compliance view** — from sales transaction (GST) → TDS deduction → Annual ITR filing

**Closing:** "You're already paying for two or three tools. With KDK's bundle, you consolidate everything, save money, and your team works in one system. Want me to show you what the pricing looks like when you combine all three?"

---

# PART 7 — QUALIFICATION QUESTIONNAIRE

Use these questions to qualify the prospect, understand their segment (DIY or DIFM), and identify which product(s) to pitch.

## A. General Qualification

**Q1. What is your role / what does your organization do?**
- If they say CA / Tax Professional / Accounting Firm → DIFM segment (pitch on productivity and client management)
- If they say Business / Enterprise / Company → DIY segment (pitch on automation and compliance health)

**Q2. How many GSTINs / TAN numbers / PAN clients do you currently handle?**
- <10 clients: small CA or DIY
- 10–100 clients: mid-size CA firm — strong bundle candidate
- 100+ clients: large CA firm — emphasize productivity and bulk features

**Q3. Are you currently using any compliance software? Which one?**
- If yes: identify competitor and use comparison data to highlight Express advantages
- If no: "This is your first time automating — let me show you what you've been missing"

**Q4. What are your biggest pain points with your current process?**
- Manual work → show automation features
- Notices missed → show Notice & Orders module
- Data errors → show validation features
- Team productivity → show bulk features and user management

**Q5. Do you work from a fixed office location or from multiple locations?**
- Multiple locations / remote → Cloud is perfect, desktop is a dealbreaker for them

**Q6. Is your data currently on a desktop software or cloud?**
- Desktop → highlight data loss risk and system dependency
- Cloud → compare features directly

## B. GST-Specific Questions

**Q7. How do you currently handle GSTR-2A/2B reconciliation?**
- Manual → show 4-click auto-reconciliation with conflict reports
- Another software → highlight no invoice limit and conflict report advantage

**Q8. Do you send GSTR-2A/2B data to your clients every month?**
- Yes, manually → show auto-email on 15th feature
- No → show them the opportunity to add value to clients

**Q9. How do you track GST notices and orders across all your clients?**
- One by one → show single-screen notice tracking with reply status

**Q10. Are you filing e-invoices? Through what platform?**
- Third party → show in-software e-invoice generation (DIY)

**Q11. How are you importing sales/purchase data — Excel, Tally, or manually?**
- Tally → show auto-sync connector + client PC option
- Excel → show import with 100+ validations

**Q12. How much time does your team spend on reconciliation every month?**
- Significant time → show 4-click auto-reco and auto Tally sync

## C. TDS-Specific Questions

**Q13. How many TDS returns do you file per quarter?**
- High volume → pitch on bulk features, auto-challan, PAN verification speed

**Q14. Are you currently facing issues with Java for FVU generation?**
- Yes → Java-free FVU is a clear win

**Q15. How do you currently check PAN compliance and verify challans?**
- Manual → show bulk PAN verification with speed-up feature (1.5L+ PANs)

**Q16. How do you currently track notices / requests on TRACES for all your clients?**
- One-by-one on TRACES → show single-screen request tracking

**Q17. Do you currently email TDS certificates to deductees?**
- Manual / not doing it → show DSC-signed Form 16/16A direct email

**Q18. How long does your TDS return preparation take per client?**
- Long → show auto-challan import, drag-drop mapping, health report, and error navigation

## D. ITR-Specific Questions

**Q19. Which ITR forms do you typically file (ITR-1 through ITR-7)?**
- Helps identify complexity level and pitch appropriate features

**Q20. Are you doing tax audit work (3CA-3CB-3CD)?**
- Yes → show 3CD Excel import, audit form generation

**Q21. How do you import AIS/26AS data into ITR currently?**
- Manual → show direct AIS import feature

**Q22. Do you have clients with capital gains from stocks or mutual funds?**
- Yes → show broker template import and capital gain data feeding

**Q23. Do your clients use Tally for accounting? How do you get their financial data?**
- Manual → show 3CB-3CD data flow and financial statement preparation

## E. Decision-Making Questions

**Q24. Who else is involved in this decision?**
- Understand the buying committee and address all stakeholders

**Q25. What is your timeline for switching / starting?**
- Immediate → push for demo and trial
- Next quarter → maintain follow-up cadence

**Q26. What is your budget range?**
- Budget concern → emphasize per-requirement pricing, easy upgrade path, and ROI (time saved × hourly rate)

**Q27. What would it take for you to make a decision today?**
- Identify the final objection and address it

---

# PART 8 — OBJECTION HANDLING

## Objection 1: "We already use ClearTax / another software"
**Response:**
"I completely understand — switching software feels like a big step. But let me ask you this: are you currently able to send 2A/2B data to all your clients automatically on the 15th? Can you see all your clients' notices on one screen without logging into each one separately? Can your team access data from anywhere without being tied to a particular computer?

Most ClearTax users we speak with are doing all of that manually. Express GST automates every one of those tasks. And we can migrate your entire client data from ClearTax in minutes — it's built into the software. Would you be willing to see a quick 15-minute demo?"

## Objection 2: "Your price is higher than competitors"
**Response:**
"I hear you on price — but let's talk about the real cost. If your team spends 3 extra hours per client per month on manual work that Express automates — that's hours multiplied by your billing rate. How many clients do you have? [Calculate the time saving].

Also, our pricing is per requirement — you pay for what you need, and you can upgrade as you grow. Unlike competitors with standard fixed pricing, we're flexible. And when you factor in the time saved, the notices avoided, and the penalties prevented, the ROI is very clear."

## Objection 3: "We are comfortable with desktop software"
**Response:**
"I understand comfort with what's familiar. But let me ask — what happens if your laptop crashes? Or if you need to work from home, or from a client's office? With desktop software, you're tied to that one machine. If there's a hardware failure, your data is at risk.

With Express on the cloud, your data is backed up automatically, VAPT-certified, and accessible from any device, anywhere. Many of our users said the same thing before switching — and within a week they never looked back."

## Objection 4: "We have a small number of clients, do we need this?"
**Response:**
"Actually, that's exactly when it makes sense to switch — before you grow. Our smaller CA users tell us that once they automated the repetitive work with Express, they were able to take on 40-50% more clients without adding staff.

And even with a small client base, the time you save on reconciliation, notice tracking, and report generation adds up quickly. At what point would you say your client load justifies a better tool — and are you willing to wait until you're already overwhelmed?"

## Objection 5: "Data security concern — we're worried about cloud"
**Response:**
"That's a very valid concern, and it's one we take extremely seriously. Express is VAPT certified — that's Vulnerability Assessment and Penetration Testing, the same security standard used by banks and government portals. We have ISO-27001 certification, end-to-end encryption, and two-factor authentication.

Consider this: your client data sitting on a desktop or laptop is far more vulnerable — to theft, hardware failure, ransomware, or accidental deletion. On our cloud, it's encrypted, backed up, and protected 24/7 by a dedicated security team."

## Objection 6: "What if the internet goes down?"
**Response:**
"Fair concern — though most offices today have reliable internet with mobile hotspot backup. But here's the real question: how often does your internet actually go down for significant time? And when it does, does your work completely stop anyway?

We've also found that our users typically spend 10-15% of their time on the software for data entry and submission — the rest is review and analysis. A brief internet outage rarely causes meaningful disruption. And with mobile app access, you can check status from your phone even if the office connection is down."

## Objection 7: "Migration from current software is too complex"
**Response:**
"Migration is our specialty — we do it every day. Express GST can import client data from ClearTax, Tally, and most other software in minutes. Our onboarding team walks you through the migration step-by-step, and your historical data comes with you — all the way back to your registration date.

We've migrated thousands of CA firms and enterprises. What software are you currently using? Let me tell you exactly how the migration works for that specific tool."

## Objection 8: "We don't need all three products"
**Response:**
"Absolutely — and that's perfectly fine. You only pay for what you need. If you only need GST right now, start with Express GST. When you're ready for TDS or ITR, they're right there on the same platform — no migration, no new vendor.

Many of our clients started with just one product and then added the others over time. Each product works standalone. But I'll tell you — clients who use all three save the most time because the data flows between them automatically. Would you like to see what the pricing looks like just for the one you need today?"

---

# PART 9 — QUICK REFERENCE CARDS

## Express GST — 30-Second Pitch
"Express GST is a cloud-based GST solution that files all your returns, reconciles 2A/2B in 4 clicks with no invoice limit, auto-emails 2B data to all clients on the 15th, tracks all notices on one screen, and sends you a return register update twice a week — all automatically. It's 7x faster than ClearTax and works from anywhere."

## Express TDS — 30-Second Pitch
"Express TDS is a cloud-based TDS filing solution that's Java-free, auto-imports challans from the government portal, uses drag-and-drop challan mapping, verifies 1.5 lakh PANs instantly, tracks all TRACES notices and requests for all clients on one screen, and gives you a Health Analysis Report so you catch every error before FVU generation."

## Express ITR — 30-Second Pitch
"Express ITR is a cloud-based income tax filing solution that handles ITR-1 to ITR-7, imports AIS/26AS directly, imports Form 16 in one click, supports capital gain via broker templates, prepares 3CA-3CB-3CD tax audit forms, tracks notices for all clients on one screen, and has an error locator so you never file a wrong return."

## Bundle — 30-Second Pitch
"KDK's complete suite — Express GST, TDS, and ITR — gives you one login, one client master, one support team, and one bill. Your GST turnover feeds your ITR automatically. Your team works across all three modules in the same interface. Stop managing three vendors and start managing one platform."

---

*End of KDK Software AI Sales Agent Knowledge Base*
*Products: Express GST | Express TDS | Express ITR*
*Segments: DIY (Enterprises) | DIFM (CAs / Tax Professionals) | Bundle*
"""

OUT.write_text(DOC, encoding="utf-8")
size_kb = OUT.stat().st_size / 1024
print(f"Created: {OUT.name}")
print(f"Size: {size_kb:.0f} KB")
print(f"Lines: {len(DOC.splitlines())}")
