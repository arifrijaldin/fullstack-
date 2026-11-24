# 🏛️ Hybrid Integration & Enterprise Financial Reconciliation Platform

[![Author](https://img.shields.io/badge/Author-Akhmad%20Arif%20Rijaldin%2C%20S.Kom.-blue.svg)](https://arifrijaldin1portofolio.netlify.app/)
[![Role](https://img.shields.io/badge/Role-Senior%20Full--Stack%20AI%20%26%20Systems%20Integration%20Engineer-purple.svg)]()
[![Python Version](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Database](https://img.shields.io/badge/Database-SAP%20Sybase%2017%20%7C%20SQLite-orange.svg)]()
[![Frontend](https://img.shields.io/badge/UI-Tailwind%20CSS%20%7C%20Glassmorphism-cyan.svg)]()
[![Automation](https://img.shields.io/badge/Automation-Chrome%20CDP%20%7C%20Win32%20API-red.svg)]()
[![Uptime](https://img.shields.io/badge/Uptime-24%2F7%20Autonomous-success.svg)]()

> **Production-Grade Enterprise Hybrid Integration Pipeline, Multi-Way Financial Reconciliation, and Robotic Process Automation (RPA) Platform bridging Legacy On-Premise Systems with Cloud SaaS.**

---

## 📌 Executive Summary

In high-stakes enterprise and hospitality operations, manual transaction audits, end-of-day financial cut-offs, and disjointed legacy systems cause significant human error, operational fatigue, and financial revenue leakage.

This platform is a **robust, 24/7 autonomous engineering ecosystem** that eliminates operational discrepancies and automates the entire financial cut-off lifecycle:
1. **Hybrid Legacy-to-Cloud Integration**: Bridges on-premise relational databases (**SAP Sybase SQL Anywhere 17**) with modern cloud SaaS portals via raw ODBC socket pooling and **Chrome DevTools Protocol (CDP)**.
2. **Multi-Way Transaction Reconciliation Engine**: Reconciles cross-channel financial data across 4 heterogeneous streams: On-Premise Relational DB, Cloud SaaS API, 3rd-Party Digital Vouchers (OTAs/Corporate), and unstructured folio remarks.
3. **Autonomous End-of-Day (EOD) Cut-Off**: Pre-flight verification of ledger balances and automatic generation of official Accounts Receivable aging (**M-10**) and Manager Daily Reports (**MDR**) via low-level Win32 memory inspection and virtual printer subsystems.
4. **Executive Reporting Pipeline**: Zero-downtime, human-in-the-loop desktop MAPI distribution orchestrating multi-attachment reports to corporate stakeholders and C-level executives.

---

## 🏗️ System Architecture

```
  [External Vouchers / OTAs]       [Unstructured Folio Remarks]
             │                                   │
             ▼                                   ▼
┌─────────────────────────────────────────────────────────────┐
│             MULTI-WAY DATA HARMONIZATION ENGINE             │
│  - Heuristic Rate & Split-Billing Parser                    │
│  - Anti-Double Charge & Anomaly Detection Gates             │
└───────────────┬─────────────────────────────┬───────────────┘
                │                             │
                ▼                             ▼
   ┌───────────────────────────┐ ┌───────────────────────────┐
   │    ON-PREMISE LEGACY      │ │        CLOUD SAAS         │
   │  SAP Sybase SQL Anywhere  │ │  Sofyan One Cloud Portal  │
   │   (Raw ODBC / PyODBC)     │ │  (Headless Chrome / CDP)  │
   └────────────┬──────────────┘ └─────────────┬─────────────┘
                │                              │
                └───────────────┬──────────────┘
                                │ (Real-Time Bidirectional Sync)
                                ▼
┌─────────────────────────────────────────────────────────────┐
│          CORE FINANCIAL BALANCE RECONCILIATION GATEWAY      │
│  - Sub-Second Execution (< 3s Latency)                      │
│  - 100% Zero-Discrepancy Ledger Reconciliation              │
│  - Cross-Room Balance Migration Tracker                     │
│  - Dynamic Hot-Reloading Architecture                       │
└───────────────────────────────┬─────────────────────────────┘
                                │
        ┌───────────────────────┼───────────────────────┐
        ▼                       ▼                       ▼
 [Balance Dashboard]   [Autonomous EOD Cut-off]   [Executive Mailer]
 (Tailwind / Glass UI) (M-10 & MDR PDF Exporter)  (Thunderbird MAPI)
```

---

## 🚀 Core Systems & Feature Highlights

### 1. ⚖️ Core Financial Balance & Reconciliation Engine (`Balance Engine`)
* **Real-time Dual-Stream Sync:** Sub-second continuous reconciliation between Sybase on-premise database records and Cloud SaaS ledger tables.
* **Smart Anomaly Detection:** Detects room migration anomalies, multi-row split charges, complimentary FOC balances, and generates real-time SQL resolution scripts.
* **Anti Double-Charge Engine:** Halts unauthorized duplicate billing attempts before transactions are posted permanently.

### 2. 🔀 Multi-Way Transaction & Remarks Audit Engine
* **4-Source Cross-Verification:** Harmonizes data across On-Premise DB, Cloud SaaS, digital OTA voucher documents, and freeform text remarks.
* **Unstructured Text Audit:** Automatically parses human-written operational notes (e.g., extra bed, breakfast inclusion, split card/cash payment) and cross-validates against folio totals.

### 3. ⏳ Autonomous EOD Financial Cut-Off & Aging Pipeline (M-10 & MDR)
* **Pre-Flight Cut-Off Check:** Safeguards against premature Day-Close locks by validating that all cash drawers and city ledgers match 100%.
* **Win32 Memory Inspection:** Directly navigates legacy PowerBuilder TreeView controls (`PBTreeView32_100`) via `VirtualAllocEx` and Windows IPC messages.
* **Virtual Subsystem Print Engine:** Orchestrates Headless Chrome CDP (`Page.printToPDF`) and Nitro PDF virtual printer drivers to produce official corporate archival PDFs in 1 click.

### 4. 📬 Executive Reporting Pipeline (`Thunderbird Desktop MAPI`)
* **Multi-Stakeholder Routing:** Automatically packages verified audit PDFs and injects them into desktop email clients, targeted to 9 corporate executive recipients.
* **Human-in-the-Loop Guard:** Provides visual pre-flight inspection before final transmission, preventing unauthorized data leakage.

### 5. ⚡ Dual-Sync Instant High-Concurrency Reservation Engine
* **Sub-5-Second Ingestion:** Parallel injection across on-premise relational tables and cloud REST endpoints without scheduling deadlocks.
* **Atomic Room State Locking:** Preserves housekeeping and front-office room cleanliness states during concurrent booking events.

---

## 💻 Tech Stack & Engineering Specifications

| Category | Technologies & Tools |
| :--- | :--- |
| **Languages & Runtime** | Python 3 (AsyncIO, Threading), JavaScript (ES6+, Node.js), SQL (T-SQL, Sybase, SQLite), PowerShell, VBScript |
| **Databases** | SAP Sybase SQL Anywhere 17, SQLite (Local Cache & In-Memory), Raw ODBC Sockets (`pyodbc`) |
| **Frontend & UI** | Tailwind CSS, HTML5, CSS3 Glassmorphism UI, Vanilla JS DOM, Responsive Bento Grid |
| **Low-Level Automation** | Chrome DevTools Protocol (CDP), Win32 API (`VirtualAllocEx`, `SendMessageW`), Windows Registry Orchestration |
| **Desktop Subsystems** | Virtual PDF Printer Drivers (Nitro PDF), Desktop MAPI Integration (Mozilla Thunderbird) |
| **AI & Orchestration** | Agentic AI Workflow Orchestration, Deterministic Financial Prompt Engineering, Human-in-the-Loop Review Gates |

---

## 🔒 Security & Privacy Notice
All sensitive guest credentials, transactional banking data, and corporate identifiers in this public repository have been **100% sanitized and replaced with synthetic dummy records** in strict compliance with enterprise data privacy standards.

---

## 👨‍💻 Author
**Akhmad Arif Rijaldin, S.Kom.**  
*Senior Full-Stack AI & Systems Integration Engineer*  
* [Portfolio Website](https://arifrijaldin1portofolio.netlify.app/)
* [LinkedIn](https://www.linkedin.com/in/arif-rijaldin-042319163)
* [GitHub Profile](https://github.com/arifrijaldin)
