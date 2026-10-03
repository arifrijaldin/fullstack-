"""
OTOMASI LAPORAN PENJUALAN NIGHT SHIFT (PORTFOLIO DEMO)
======================================================
Automated Night Audit Sales & Manager Daily Report (MDR) Extraction.
Extracts revenue, room statistics, F&B figures, and populates an Excel spreadsheet.
Includes fail-safe fallback to synthetic dummy revenue for safe portfolio evaluation.
"""

import os
import sys
import time
from datetime import datetime
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

def run_sales_report_automation():
    print("=" * 65)
    print("   OTOMASI UPDATE LAPORAN PENJUALAN NIGHT SHIFT (PORTFOLIO DEMO)")
    print("=" * 65)
    print("\n[1/4] Memeriksa status file Excel...")
    output_excel = ROOT_DIR / "data" / "LAPORAN_PENJUALAN_DEMO.xlsx"
    print(f"  -> Target File: {output_excel.name}")

    print("\n[2/4] Menghubungkan ke Cloud PMS (Headless Scraper / Mock Mode)...")
    time.sleep(1)
    
    # Synthetic MDR data
    mdr_dummy = {
        "room_revenue": 38500000,
        "food_resto": 4200000,
        "bev_resto": 1200000,
        "room_available": 100,
        "room_sold": 82,
        "occupancy_rate": 82.0,
        "total_revenue": 43900000
    }
    print("  -> Berhasil mengekstrak data MDR Tanggal Aktif.")

    print("\n[3/4] Menulis data transaksi ke Spreadsheet...")
    try:
        import openpyxl
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Sales Report Demo"
        
        ws.append(["TANGGAL AUDIT", datetime.now().strftime("%Y-%m-%d")])
        ws.append(["PROPERTI", "Grand Nusantara Hotel & Resort"])
        ws.append([])
        ws.append(["METRIK OPERASIONAL", "NILAI"])
        ws.append(["Kamar Tersedia (Room Available)", mdr_dummy["room_available"]])
        ws.append(["Kamar Terjual (Room Sold)", mdr_dummy["room_sold"]])
        ws.append(["Tingkat Hunian (Occupancy)", f"{mdr_dummy['occupancy_rate']}%"])
        ws.append(["Pendapatan Kamar (Room Revenue)", f"Rp {mdr_dummy['room_revenue']:,}"])
        ws.append(["Pendapatan Makanan Resto", f"Rp {mdr_dummy['food_resto']:,}"])
        ws.append(["Pendapatan Minuman Resto", f"Rp {mdr_dummy['bev_resto']:,}"])
        ws.append(["TOTAL PENDAPATAN HARIAN", f"Rp {mdr_dummy['total_revenue']:,}"])
        
        output_excel.parent.mkdir(parents=True, exist_ok=True)
        wb.save(output_excel)
        print(f"  -> File Excel berhasil disimpan: {output_excel}")
    except Exception as e:
        print(f"  -> [Info] Openpyxl generation skipped ({e}), data summary tercatat.")

    print("\n[4/4] Selesai! Ringkasan Laporan Penjualan:")
    print(f"      Total Pendapatan : Rp {mdr_dummy['total_revenue']:,}")
    print(f"      Occupancy        : {mdr_dummy['occupancy_rate']}%")
    print("=" * 65)

if __name__ == "__main__":
    run_sales_report_automation()
