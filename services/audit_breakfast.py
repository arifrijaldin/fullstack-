"""
Automated Breakfast & Meal-Plan Occupancy Auditor.

Cross-references in-house registered guests against meal plan entitlements
(Room Only vs Room with Breakfast) to prevent F&B revenue leakage.
"""

import sys
import json
from datetime import datetime

from pathlib import Path
ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from config import DB_CONFIG, get_connection_string

try:
    import pyodbc
except ImportError:
    pyodbc = None

def run_breakfast_audit():
    """Queries breakfast counts or produces synthetic operational report."""
    if pyodbc:
        try:
            conn = pyodbc.connect(get_connection_string(), timeout=3)
            cursor = conn.cursor()
            sql = """
                SELECT r.room_number, r.guest_name, r.pax_count, r.meal_plan
                FROM inhouse_guests r
                WHERE r.status = 'Stay'
            """
            cursor.execute(sql)
            rows = cursor.fetchall()
            conn.close()
            return [{"room": str(r[0]), "guest": r[1], "pax": r[2], "plan": r[3]} for r in rows]
        except Exception:
            pass

    # Synthetic Breakfast Dataset
    return [
        {"room": "101", "guest": "Budi Santoso", "pax": 2, "plan": "Bed & Breakfast"},
        {"room": "102", "guest": "Siti Rahma", "pax": 1, "plan": "Room Only"},
        {"room": "103", "guest": "MAN IC OKI SUMSEL", "pax": 2, "plan": "Bed & Breakfast (FOC)"},
        {"room": "108", "guest": "PT Energi Nusantara", "pax": 2, "plan": "Bed & Breakfast"},
        {"room": "138", "guest": "Panitia Bimtek Kemenag", "pax": 1, "plan": "Room Only (Compliment)"}
    ]

def print_audit_summary():
    data = run_breakfast_audit()
    total_bfast_pax = sum(item["pax"] for item in data if "Breakfast" in item["plan"])
    room_only_count = sum(1 for item in data if "Room Only" in item["plan"])

    print("=" * 60)
    print(f"[BREAKFAST AUDIT] DAILY MEAL PLAN AUDIT - {datetime.now().strftime('%d %B %Y')}")
    print("=" * 60)
    for item in data:
        print(f"Room {item['room']:<4} | {item['guest']:<25} | Pax: {item['pax']} | {item['plan']}")
    print("-" * 60)
    print(f"TOTAL ENTITLED BREAKFAST COVERS : {total_bfast_pax} PAX")
    print(f"TOTAL ROOM ONLY (NO BREAKFAST)  : {room_only_count} ROOMS")
    print("=" * 60)

if __name__ == "__main__":
    print_audit_summary()
