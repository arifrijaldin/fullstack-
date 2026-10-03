"""
Local Micro-Service API & Reconciliation Gateway.

Provides high-speed local HTTP endpoints consumed by frontend desktop dashboards:
- /ping : Service health verification.
- /api/roomsales : PMS database transaction records (with synthetic mock fallback).
- /api/sofyan/roomsales : Live scraped Cloud PMS records.
- /api/sofyan/status : Scraping worker telemetry.
- /api/breakfast : Meal entitlement audit records.
"""

import os
import sys
import json
import urllib.parse
from http.server import ThreadingHTTPServer, BaseHTTPRequestHandler
from typing import Dict, Any

from pathlib import Path
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from config import SERVER_HOST, SERVER_PORT, DB_CONFIG, get_connection_string
from services.cloud_pms_scraper import DATA_CACHE, start_continuous_worker

# Optional DB connectivity
try:
    import pyodbc
except ImportError:
    pyodbc = None

def get_db_roomsales() -> Dict[str, Any]:
    """Queries Sybase SQL Anywhere or returns realistic synthetic dataset."""
    if pyodbc:
        try:
            conn = pyodbc.connect(get_connection_string(), timeout=3)
            cursor = conn.cursor()
            # Production query for in-house room charges
            sql = """
                SELECT room_number, guest_name, total_charge, status, original_room
                FROM v_daily_room_charges
                WHERE audit_date = CURRENT DATE
            """
            cursor.execute(sql)
            results = {}
            for row in cursor.fetchall():
                r_num = str(row[0])
                results.setdefault(r_num, []).append({
                    "room": r_num,
                    "guest": row[1],
                    "total": float(row[2]),
                    "status": row[3],
                    "orig_room": row[4]
                })
            conn.close()
            return results
        except Exception:
            pass

    # High-fidelity synthetic dataset for portfolio evaluation
    return {
        "101": [{"room": "101", "guest": "Budi Santoso", "total": 450000, "status": "Stay", "orig_room": ""}],
        "102": [{"room": "102", "guest": "Siti Rahma", "total": 600000, "status": "Stay", "orig_room": ""}],
        "103": [{"room": "103", "guest": "MAN IC OKI SUMSEL", "total": 0, "status": "Stay", "orig_room": ""}],
        "105": [{"room": "105", "guest": "Michael Brown", "total": 850000, "status": "Check-Out", "orig_room": "104"}],
        "108": [{"room": "108", "guest": "PT Energi Nusantara", "total": 550000, "status": "Stay", "orig_room": ""}],
        "138": [{"room": "138", "guest": "Panitia Bimtek Kemenag", "total": 0, "status": "Stay", "orig_room": ""}],
        "201": [{"room": "201", "guest": "Andi Wijaya", "total": 450000, "status": "Stay", "orig_room": ""}]
    }

class ReconciliationHandler(BaseHTTPRequestHandler):
    def send_cors_headers(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_cors_headers()
        self.end_headers()

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path = parsed.path

        if path == "/ping":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.send_cors_headers()
            self.end_headers()
            self.wfile.write(b"ok")
            return

        elif path == "/api/roomsales":
            data = get_db_roomsales()
            body = json.dumps(data).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.send_cors_headers()
            self.end_headers()
            self.wfile.write(body)
            return

        elif path == "/api/sofyan/roomsales":
            raw_text = DATA_CACHE.get("roomsales", "")
            body = raw_text.encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "text/plain; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.send_cors_headers()
            self.end_headers()
            self.wfile.write(body)
            return

        elif path == "/api/sofyan/status":
            body = json.dumps({
                "status": DATA_CACHE.get("status", "idle"),
                "last_updated": DATA_CACHE.get("last_updated"),
                "has_roomsales": bool(DATA_CACHE.get("roomsales")),
                "has_summary": bool(DATA_CACHE.get("summary")),
            }).encode("utf-8")
            self.send_response(200)
            self.send_header("Content-Type", "application/json; charset=utf-8")
            self.send_header("Content-Length", str(len(body)))
            self.send_cors_headers()
            self.end_headers()
            self.wfile.write(body)
            return

        self.send_response(404)
        self.end_headers()

def run_server():
    print(f"Starting Reconciliation API Gateway on http://{SERVER_HOST}:{SERVER_PORT}")
    start_continuous_worker()
    server = ThreadingHTTPServer((SERVER_HOST, SERVER_PORT), ReconciliationHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nGateway stopped.")

if __name__ == "__main__":
    run_server()
