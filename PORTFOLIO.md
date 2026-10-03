# 💼 Technical Engineering Portfolio
## Akhmad Arif Rijaldin, S.Kom.
**AI & Automation Systems Engineer | Intelligent RPA & Systems Integration Specialist**  
📍 Jakarta, Indonesia &bull; 🌐 [LinkedIn](https://linkedin.com/in/arifrijaldin) &bull; 🐙 [GitHub](https://github.com/arifrijaldin)

---

## 👨‍💻 About Me

Sarjana Teknik Informatika (S.Kom) dari Universitas Indraprasta PGRI dengan spesialisasi pada **Rekayasa Otomasi Berbasis AI (AI & RPA Engineering)**, integrasi multi-sistem enterprise, serta pengembangan **Autonomous Agentic Workflows**. 

Berpengalaman merancang dan mengimplementasikan sistem otomasi operasional 24/7 di industri *hospitality* dan perbankan yang menghubungkan basis data relasional on-premise (**Sybase SQL Anywhere 17 ODBC**), scraping cloud web via **Selenium Headless**, pemrosesan dokumen/voucher email otomatis, sistem mitigasi kegagalan mandiri (*Dead-Letter Queue*), serta rekonsiliasi finansial nir-selisih (*Zero-Leakage Balancing*).

---

## 🛠️ Core Competencies & Tech Stack

| Domain | Technologies & Frameworks |
|---|---|
| **Core Languages** | Python 3 (Advanced), JavaScript (ES6+), SQL, HTML5/CSS3, Batch Scripts, PowerShell |
| **Automation & RPA** | Selenium WebDriver, Chrome Headless Orchestration, Event-Driven Daemons, Win32 Named Mutex, Regex Tokenizers |
| **Databases & Middleware** | Sybase SQL Anywhere 17 (ODBC), SQLite, MySQL, RESTful Micro-services (ThreadingHTTPServer, Flask) |
| **AI & Modern Tools** | Autonomous Agentic Workflows, LLM APIs (Gemini, OpenAI), Prompt Engineering, AI-Assisted Engineering (Antigravity, Cursor, Copilot) |
| **Engineering Practices** | Clean Architecture, Dead-Letter Queue (DLQ), Defensive Programming, GDPR/Data Sanitization, Excel/Spreadsheet Engine (`openpyxl`) |

---

## 🚀 Featured Project: Autonomous Hotel Operations RPA & Reconciliation Suite

Sistem otomasi terintegrasi berskala produksi yang dirancang untuk mengeliminasi beban manual Front Office, Night Audit, dan Tim Sales di operasional hotel 24 jam.

```
[OTAs: Agoda, Booking.com, Traveloka, MG Bedbank]
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

### 📦 8 Sistem Otomasi yang Dikembangkan:

#### 1. 🤖 START BOT RESERVASI (Autonomous OTA Ingestion Daemon)
- **Fungsi:** Daemon background yang memantau folder mailbox Thunderbird secara realtime, mengekstrak voucher lintas platform OTA (Agoda, Booking.com, Traveloka, MG Bedbank), dan menginput reservasi ke database Sybase SQL Anywhere 17.
- **Inovasi Teknis:** Dilengkapi **Dead-Letter Queue** (`GAGAL_RESERVASI`) untuk mengkarantina anomali format baru tanpa kehilangan data, serta **Win32 Named Mutex** untuk mencegah bentrok proses.

#### 2. ⚖️ BALANCE BOT (Dual-Stream Financial Reconciliation Engine)
- **Fungsi:** Mesin rekonsiliasi audit realtime yang mencocokkan transaksi kamar di Database Internal (MISS / Sybase) dengan Cloud Web PMS.
- **Inovasi Teknis:** Algoritma pencocokan heuristik yang mampu mengenali tamu pindah kamar fisik (`104 -> 105`), penggabungan multi-transaksi split-rate, dan validasi kamar gratis (*Compliment/FOC Rp 0*) tanpa menandainya sebagai selisih rugi.

#### 3. 🍳 BREAKFAST AUDIT (3-Way Meal Plan Balancing)
- **Fungsi:** Mengaudit hak makan sarapan (*Bed & Breakfast* vs *Room Only*) tamu terisi (*In-House*) setiap subuh.
- **Inovasi Teknis:** Mencegah kebocoran pendapatan F&B dengan memvalidasi manifest kamar sebelum restoran beroperasi, menyelamatkan jutaan rupiah per bulan dari konsumsi tanpa tagihan.

#### 4. 💬 DEPARTURE CHAT BOT (Guest Courtesy & WhatsApp Dispatcher)
- **Fungsi:** Papan kontrol live keberangkatan tamu harian dengan tombol pengiriman pesan WhatsApp cepat (pengingat jam check-out, konfirmasi late check-out, atau ucapan terima kasih).

#### 5. 📅 PORTAL RESERVASI MARKETING (Flask Sales Allotment Web)
- **Fungsi:** Aplikasi web modern ringan untuk tim sales/marketing hotel menginput kuota kamar pesanan grup/korporat secara instan dan tersinkronisasi ke sistem pusat.

#### 6. 📊 LAPORAN PENJUALAN OTOMATIS (MDR Excel Generator)
- **Fungsi:** Mengekstrak rekapitulasi omset harian (Kamar, Restoran, Laundry, Minibar, Occupancy, ADR) langsung ke template spreadsheet Excel resmi tanpa ketik manual.

#### 7. 🔑 VC KAMAR DAY CLOSE (Post-EOD Room Recovery Guard)
- **Fungsi:** Memulihkan status fisik kamar bersih menjadi *Vacant Clean (VC)* pasca proses Day Close harian PMS, dengan proteksi ketat agar kamar rusak (*VR*) dan kamar kotor (*VD*) tetap terkunci.

#### 8. 📱 DAILY REPORT WA GENERATOR (Shift Handover Broadcaster)
- **Fungsi:** Mengompilasi seluruh data performa hotel dalam 24 jam menjadi format serah terima shift WhatsApp profesional dengan 1-klik salin ke clipboard untuk broadcast ke grup manajemen hotel.

---

## 📈 Key Engineering Achievements & ROI

| Metrik Evaluasi | Sebelum Otomasi | Dengan Sistem Otomasi | Dampak Bisnis |
|---|---|---|---|
| **Waktu Night Audit** | 2.5 – 3 Jam / malam | **< 10 Detik** | Efisiensi waktu **99.2%** |
| **Input Voucher OTA** | 10 – 15 menit per voucher | **Otonom (0 Detik)** | Nol antrean check-in tertunda |
| **Akurasi Finansial** | Rawan salah ketik kasir | **100% Cocok (0 Selisih)** | Zero human-error audit |
| **Proteksi F&B** | Pengecekan kupon manual | **Validasi Otomatis Subuh** | Menghilangkan kebocoran konsumsi sarapan |
| **System Uptime** | Sering crash jika dibuka dobel | **24/7 Stabil** | Proteksi Win32 Mutex & Headless Isolation |

---

## 🖥️ Live Presentation & Interactive Demos

Ekosistem ini dilengkapi dengan antarmuka interaktif:
* **Interactive Architecture Slider:** `frontend/arsitektur_flow_sistem.html` (Presentasi alur sistem 8 slide dengan estetika Canva, gradasi visual, dan visualisasi interaktif).
* **Live Bot Typing Simulation:** `frontend/live_bot_reservasi.html` (Simulasi pengetikan otomatis dan injeksi database).
* **Audit Dashboard:** `frontend/audit_dashboard.html` (Monitoring rekonsiliasi dua arah).

---

## 🔒 Security, Compliance & Data Privacy

* Seluruh data yang ditampilkan dalam repositori ini adalah **data sintetis (100% dummy/sanitized)**.
* Identitas tamu, nomor kontak, serta kata sandi database asli telah diabstraksi penuh ke dalam environment variables (`.env`).
* Tidak ada data rahasia hotel maupun data pribadi yang disimpan di dalam source code publik.

---

## 📬 Contact & Professional Inquiries

* **Developer:** Akhmad Arif Rijaldin, S.Kom.
* **LinkedIn:** [linkedin.com/in/arifrijaldin](https://linkedin.com/in/arifrijaldin)
* **GitHub:** [github.com/arifrijaldin](https://github.com/arifrijaldin)
* **Lokasi:** Jakarta, Indonesia
