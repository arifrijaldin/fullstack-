# 🏨 Autonomous Hotel Operations RPA & Reconciliation Platform

[![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![Database](https://img.shields.io/badge/database-Sybase%20SQL%20Anywhere%2017-orange.svg)]()
[![Automation](https://img.shields.io/badge/RPA-Selenium%20Headless-green.svg)]()
[![Architecture](https://img.shields.io/badge/architecture-Event--Driven%20%7C%20Microservices-purple.svg)]()
[![Privacy](https://img.shields.io/badge/data-100%25%20Sanitized%20Dummy-success.svg)]()

> **Production-Grade Enterprise Robotic Process Automation (RPA) & Financial Reconciliation Engine for 24/7 Hotel Front Office Operations.**

---

## 📌 Executive Summary

In high-volume 24/7 hotel operations, manual night audits, channel manager data entry, and room rate reconciliations cause significant human error, operational fatigue, and financial discrepancies.

This project is an **end-to-end autonomous RPA ecosystem** that replaces tedious manual workflows with high-speed, zero-downtime micro-services:
1. **Automated Ingestion Pipeline**: Ingests heterogeneous booking voucher emails (`.eml`) directly from email clients (Mozilla Thunderbird), parses OTA formats (Agoda, Booking.com, Traveloka, MG Bedbank), and inserts them directly into the Property Management System (PMS).
2. **Real-time Financial Reconciliation Bot (`Balance Bot`)**: Synchronizes legacy on-premise PMS databases (**Sybase SQL Anywhere 17**) with Cloud PMS portals (**Selenium Headless Worker**) using an intelligent cross-matching algorithm.
3. **Operations & Audit Desktop Suite**: Standalone desktop applications for Breakfast Audits, Daily Closing Room Reports, Departure Monitors, and WhatsApp Operational Handovers.

---

## 🏗️ System Architecture

```
[OTAs: Agoda, Booking.com, MG Bedbank, Traveloka]
                      │ (Voucher Confirmation Emails)
                      ▼
        [Thunderbird Mailbox (.eml)]
                      │
                      ▼
   ┌─────────────────────────────────────┐
   │    OTA Ingestion Daemon (Python)    │
   │  - Single-Instance Win32 Mutex      │
   │  - Multi-OTA Regex Normalizer       │
   │  - Deduplication (.processed.json)  │
   └──────┬────────────────────────┬─────┘
          │ (Valid Voucher)        │ (Syntax Variance / Anomaly)
          ▼                        ▼
┌──────────────────┐     ┌─────────────────────────────────┐
│ Sybase SQL 17    │     │ Quarantine & Dead-Letter Queue  │
│ On-Premise PMS   │     │ (Automated Daily Error Recap)   │
└─────────┬────────┘     └─────────────────────────────────┘
          │
          │ (Dual-Stream In-House Room Ledger)
          ▼
┌──────────────────────────────────────────────────────────┐
│     Reconciliation Gateway & Audit Engine (Port 8085)    │
│  - Sybase ODBC Integration                               │
│  - Selenium Chrome Scraper (Isolated Browser Profile)    │
│  - Smart Matching: Cross-Room Moves & FOC (Rp 0) Logic   │
└─────────────────────────┬────────────────────────────────┘
                          │
     ┌────────────────────┼────────────────────┐
     ▼                    ▼                    ▼
[Balance Bot UI]  [Breakfast Auditor]  [WhatsApp Dispatcher]
(Desktop WebApp)    (F&B Occupancy)      (Night Handover)
```

---

## 📦 Complete Desktop Applications & Automation Suite

Inside this portfolio, every application can be launched directly via its desktop shortcut (`.lnk`) or launcher (`.bat`):

1. **⚖️ BALANCE (`BALANCE.lnk` / `1_BALANCE_BOT.bat`)**:
   - Dual-channel real-time reconciliation dashboard between Sybase database records and Cloud PMS web data.
   - Intelligent heuristic matching engine: detects room moves (`104 -> 105`), split room rates, multi-row charges, and zero-balance Complimentary / FOC rooms (`SAMA 🎁 FOC`).

2. **🍳 BREAKFAST AUDIT (`BREAKFAST AUDIT.lnk` / `2_BREAKFAST_AUDIT.bat`)**:
   - Automated 3-way meal plan entitlement audit cross-referencing in-house occupancy with restaurant breakfast covers.

3. **💬 DEPARTURE CHAT (`DEPARTURE CHAT.lnk` / `3_DEPARTURE_CHAT.bat`)**:
   - Real-time guest departure operations board with automated WhatsApp handover courtesy dispatching.

4. **📅 RESERVASI MKT (`RESERVASI MKT.lnk` / `4_RESERVASI_MKT.bat`)**:
   - Ultra-modern Flask web portal for internal marketing & sales room allotment bookings with sanitized guest records.

5. **📊 LAPORAN PENJUALAN (`LAPORAN PENJUALAN.lnk` / `5_LAPORAN_PENJUALAN.bat`)**:
   - Automated night-audit Manager Daily Report (MDR) revenue extractor and Excel spreadsheet generator.

6. **🔑 VC KAMAR DAY CLOSE (`VC KAMAR DAY CLOSE.lnk` / `6_VC_KAMAR_DAY_CLOSE.bat`)**:
   - Automated post-day-close room status restoration utility (restores clean VC rooms while strictly preserving dirty, repair, and in-house statuses).

7. **📱 DAILY REPORT WA (`DAILY REPORT WA.lnk` / `7_DAILY_REPORT_WA.bat`)**:
   - Autonomous operational shift handover report generator formatted for WhatsApp group broadcast.

8. **🤖 START BOT RESERVASI (`START BOT RESERVASI.lnk` / `8_START_BOT_RESERVASI.bat`)**:
   - 24/7 autonomous background ingestion daemon: monitors incoming reservation emails (`.eml` / Thunderbird), parses multi-channel OTA schemas (Agoda, Booking, Traveloka, MG Bedbank), and manages dead-letter quarantines.

---

## 💡 Key Engineering Highlights

| Architectural Challenge | Engineering Solution Implemented |
|---|---|
| **Process Collisions** | Win32 Kernel Mutex (`CreateMutexW`) prevents accidental duplicate launches of background daemons. |
| **Silent Crashes in `.pyw`** | Custom `SilumanOutput` sink redirects `sys.stdout` and `sys.stderr` safely to prevent silent Windows termination. |
| **Chrome Zombie Leaks** | Selenium instances utilize isolated temporary profiles (`--user-data-dir`) and `--headless=new` with automated driver disposal. |
| **Legacy DB Constraints** | Direct parameterized ODBC queries with Sybase SQL Anywhere 17 timeout and fallback handlers. |
| **Data Privacy (GDPR/Compliance)** | 100% of guest identities, booking codes, and proprietary hotel credentials are abstracted into environment variables (`.env`) and synthetic test records. |

---

## 🚀 Quickstart & Demonstration

### 1. Clone & Environment Setup
```bash
git clone https://github.com/[your-username]/hotel-rpa-ecosystem.git
cd hotel-rpa-ecosystem

# Copy environment configuration
cp .env.example .env
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
# Or minimal dependencies:
pip install pyodbc selenium python-dotenv
```

### 3. Run Sample Ingestion Pipeline
```bash
# Processes synthetic Agoda voucher in data/dummy_vouchers/
python services/ota_email_pipeline.py
```

### 4. Launch Reconciliation Gateway
```bash
python services/reconciliation_api.py
```
*Open `frontend/audit_dashboard.html` in your browser to view the interactive live reconciliation table.*

---

## 🔒 Privacy & Sanitization Notice
This repository contains **strictly sanitized code and synthetic dummy data** designed for portfolio presentation. All real-world hotel identifiers, guest identities, server IP addresses, and database passwords have been removed to preserve enterprise data confidentiality and privacy regulations.

---

## 👨‍💻 Author
**Hotel Automation & Integration Specialist / Python RPA Developer**  
*Available for Software Engineering, Automation, and Systems Integration Roles.*
