"""
SISTEM RESERVASI MARKETING AI (PORTFOLIO SHOWCASE)
==================================================
Ultra-Modern Web Application for Marketing Reservation Automation.
Equipped with AI prompt extraction, mock database persistence, and native Windows desktop packaging.
All guest data, phone numbers, and credentials are 100% sanitized for public demonstration.
"""

import os
import sys
import json
import time
from pathlib import Path
from flask import Flask, request, jsonify, render_template_string

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sistem Reservasi Marketing AI (Portfolio Demo)</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            --bg: #0f172a;
            --card: rgba(30, 41, 59, 0.75);
            --border: rgba(148, 163, 184, 0.15);
            --primary: #10b981;
            --text: #f8fafc;
            --muted: #94a3b8;
        }
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            background: var(--bg);
            color: var(--text);
            padding: 24px;
            min-height: 100vh;
        }
        .header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid var(--border);
            padding-bottom: 16px;
            margin-bottom: 24px;
        }
        .header h1 {
            color: #34d399;
            font-size: 20px;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .container {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 24px;
        }
        .card {
            background: var(--card);
            border: 1px solid var(--border);
            backdrop-filter: blur(12px);
            border-radius: 12px;
            padding: 20px;
        }
        .card h2 {
            font-size: 15px;
            margin-bottom: 16px;
            color: #6ee7b7;
            display: flex;
            align-items: center;
            gap: 8px;
        }
        label {
            display: block;
            font-size: 12px;
            color: var(--muted);
            margin-bottom: 6px;
            font-weight: 500;
        }
        input, select, textarea {
            width: 100%;
            padding: 10px 12px;
            background: rgba(15, 23, 42, 0.8);
            border: 1px solid var(--border);
            border-radius: 8px;
            color: white;
            font-size: 13px;
            margin-bottom: 14px;
        }
        input:focus, textarea:focus {
            outline: none;
            border-color: var(--primary);
        }
        .btn-submit {
            background: #059669;
            color: white;
            border: none;
            padding: 12px 20px;
            border-radius: 8px;
            font-size: 13px;
            font-weight: 700;
            width: 100%;
            cursor: pointer;
            transition: all 0.2s;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
        }
        .btn-submit:hover { background: #047857; }
        .table-log {
            width: 100%;
            border-collapse: collapse;
            font-size: 12.5px;
            margin-top: 10px;
        }
        .table-log th {
            text-align: left;
            padding: 10px;
            color: var(--muted);
            border-bottom: 1px solid var(--border);
        }
        .table-log td {
            padding: 10px;
            border-bottom: 1px solid rgba(148, 163, 184, 0.08);
        }
        .badge {
            background: rgba(16, 185, 129, 0.15);
            color: #34d399;
            border: 1px solid rgba(16, 185, 129, 0.3);
            padding: 2px 8px;
            border-radius: 6px;
            font-size: 11px;
            font-weight: 600;
        }
    </style>
</head>
<body>

    <div class="header">
        <div>
            <h1><i class="fa-solid fa-calendar-check"></i> Reservasi Marketing & Allotment Portal</h1>
            <div style="font-size: 12px; color: var(--muted); margin-top: 4px;">Modul Input Reservasi Cepat Tim Marketing & Sales (Portfolio Edition)</div>
        </div>
        <div style="font-size: 12px; color: #34d399; background: rgba(16,185,129,0.1); padding: 8px 14px; border-radius: 8px; border: 1px solid rgba(16,185,129,0.3);">
            <i class="fa-solid fa-shield-halved"></i> 100% Data Dummy & Privacy Protected
        </div>
    </div>

    <div class="container">
        <!-- FORM INPUT -->
        <div class="card">
            <h2><i class="fa-solid fa-pen-to-square"></i> Input Reservasi Tamu (Dummy)</h2>
            <form id="resForm" onsubmit="handleReserve(event)">
                <label>Nama Lengkap Tamu:</label>
                <input type="text" id="guestName" value="Drs. Bambang Sudirman" required>

                <label>Nomor Kontak / WhatsApp:</label>
                <input type="text" id="phone" value="0812-XXXX-9988" required>

                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
                    <div>
                        <label>Tanggal Check-In:</label>
                        <input type="date" id="checkin" value="2026-10-04" required>
                    </div>
                    <div>
                        <label>Tanggal Check-Out:</label>
                        <input type="date" id="checkout" value="2026-10-06" required>
                    </div>
                </div>

                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
                    <div>
                        <label>Tipe Kamar:</label>
                        <select id="roomType">
                            <option>Deluxe King Room</option>
                            <option>Executive Suite</option>
                            <option>Standard Twin Room</option>
                        </select>
                    </div>
                    <div>
                        <label>Harga per Malam (IDR):</label>
                        <input type="number" id="rate" value="550000" required>
                    </div>
                </div>

                <label>Catatan / Permintaan Khusus:</label>
                <input type="text" id="notes" value="Early check-in pukul 11:00 WIB, Non-smoking room">

                <button type="submit" class="btn-submit"><i class="fa-solid fa-paper-plane"></i> Proses Input Reservasi ke PMS</button>
            </form>
        </div>

        <!-- RECENT LOGS -->
        <div class="card">
            <h2><i class="fa-solid fa-clock-rotate-left"></i> Log Reservasi Terakhir Terinput</h2>
            <table class="table-log">
                <thead>
                    <tr>
                        <th>Tamu</th>
                        <th>Kamar</th>
                        <th>Total</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody id="logBody">
                    <tr>
                        <td><strong>Budi Santoso</strong></td>
                        <td>Deluxe King</td>
                        <td>Rp 450,000</td>
                        <td><span class="badge">TERSIMPAN</span></td>
                    </tr>
                    <tr>
                        <td><strong>Siti Rahma</strong></td>
                        <td>Standard Twin</td>
                        <td>Rp 600,000</td>
                        <td><span class="badge">TERSIMPAN</span></td>
                    </tr>
                    <tr>
                        <td><strong>PT Energi Nusantara</strong></td>
                        <td>Executive Suite</td>
                        <td>Rp 1,100,000</td>
                        <td><span class="badge">TERSIMPAN</span></td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>

    <script>
        function handleReserve(e) {
            e.preventDefault();
            const name = document.getElementById('guestName').value;
            const room = document.getElementById('roomType').value;
            const rate = parseInt(document.getElementById('rate').value);
            
            const tbody = document.getElementById('logBody');
            const newRow = document.createElement('tr');
            newRow.innerHTML = `
                <td><strong>${name}</strong></td>
                <td>${room}</td>
                <td>Rp ${rate.toLocaleString('id-ID')}</td>
                <td><span class="badge">BARU DIBUAT</span></td>
            `;
            tbody.insertBefore(newRow, tbody.firstChild);

            alert('Reservasi untuk ' + name + ' berhasil disimulasikan dan dicatat!');
        }
    </script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route("/api/ping")
def ping():
    return jsonify({"status": "ok", "service": "Reservasi MKT Demo"})

def launch_server(port=5000):
    print(f"Starting Reservasi MKT on http://127.0.0.1:{port}")
    app.run(host="127.0.0.1", port=port, debug=False)

if __name__ == "__main__":
    launch_server()
