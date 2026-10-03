"""
PEMULIHAN STATUS KAMAR VC POST DAY CLOSE (PORTFOLIO DEMO)
=========================================================
Automated Room Status Restoration after End of Day (EOD) / Day Close in PMS.
Strict Hospitality Logic:
1. Vacant Clean rooms prior to Day Close -> Restored back to VC VC.
2. Late Check-Out (VD VD) -> Preserved DIRTY (VD VD).
3. Room Move (CR) -> Preserved DIRTY (CR).
4. Out of Order / Under Repair (VR) -> Preserved VR.
5. In-House Occupied rooms (OD/OL) -> Completely untouched.
"""

import sys
import time
from datetime import datetime, timedelta
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

def confirm_user_action():
    try:
        import tkinter as tk
        from tkinter import messagebox
        root = tk.Tk()
        root.withdraw()
        root.attributes('-topmost', True)
        
        msg = (
            "KONFIRMASI PEMULIHAN STATUS KAMAR (PORTFOLIO DEMO)\n"
            "---------------------------------------------------\n"
            "Apakah Anda YAKIN ingin mensimulasikan pemulihan status\n"
            "kamar bersih ke VC VC setelah proses Day Close?\n\n"
            "PENGAMAN STATUS:\n"
            "- Kamar Late Check-Out -> Tetap Kotor (VD)\n"
            "- Kamar Rusak (VR)     -> Tetap Rusak (VR)\n"
            "- Kamar Terisi Tamu    -> Tidak Disentuh\n\n"
            "Klik [Yes] untuk Lanjut, atau [No] untuk Batal."
        )
        ans = messagebox.askyesno("Konfirmasi Post Day Close", msg, parent=root)
        root.destroy()
        return ans
    except Exception:
        return True

def run_restore_rooms():
    print("=" * 65)
    print("   PEMULIHAN STATUS KAMAR VC (POST DAY CLOSE) - PORTFOLIO DEMO")
    print("=" * 65)
    print("\n[1/3] Menampilkan dialog konfirmasi...")
    if not confirm_user_action():
        print("  -> Proses dibatalkan oleh pengguna.")
        return

    print("  -> Konfirmasi diterima. Membaca snapshot kamar H-1...")
    time.sleep(1)

    # Synthetic room matrix
    rooms_snapshot = [
        {"room": "101", "prev_status": "VC", "new_status": "VC VC", "action": "DIPULIHKAN"},
        {"room": "102", "prev_status": "VC", "new_status": "VC VC", "action": "DIPULIHKAN"},
        {"room": "103", "prev_status": "VD", "new_status": "VD VD", "action": "DIABAIKAN (LATE CO)"},
        {"room": "105", "prev_status": "OD", "new_status": "OD",    "action": "TIDAK DISENTUH (IN-HOUSE)"},
        {"room": "108", "prev_status": "VR", "new_status": "VR",    "action": "DIABAIKAN (RUSAK/PERBAIKAN)"},
        {"room": "110", "prev_status": "VC", "new_status": "VC VC", "action": "DIPULIHKAN"},
        {"room": "138", "prev_status": "OD", "new_status": "OD",    "action": "TIDAK DISENTUH (IN-HOUSE)"}
    ]

    print("\n[2/3] Mengeksekusi pemulihan kamar sesuai aturan hotel...")
    restored = 0
    skipped = 0
    for r in rooms_snapshot:
        print(f"  Kamar {r['room']:<4} | Status: {r['prev_status']} -> {r['new_status']:<6} | {r['action']}")
        if r["action"] == "DIPULIHKAN":
            restored += 1
        else:
            skipped += 1

    print("\n[3/3] Selesai! Ringkasan Pemulihan:")
    print(f"      Total Kamar Berhasil Dipulihkan ke VC : {restored} Kamar")
    print(f"      Total Kamar Dijaga Aman (VD/VR/Tamu) : {skipped} Kamar")
    print("=" * 65)

if __name__ == "__main__":
    run_restore_rooms()
