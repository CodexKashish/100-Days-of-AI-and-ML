# ---------------------------------------------------------
# Project: The Innovation Fail-Safe 🛡️
# Day 18/100: File Migration & Backup Automation
# Goal: Automatically create dated backups of your academic leads.
# ---------------------------------------------------------

import shutil
import os
from datetime import datetime

def create_backup():
    print("--- 🛡️  INNOVATION FAIL-SAFE: INITIALIZED ---")
    
    source_file = "academic_leads.txt"
    
    # 1. Check if the original vault exists
    if not os.path.exists(source_file):
        print("⚠️ Source vault not found. Nothing to back up.")
        return

    # 2. Generate a unique filename with today's date
    # This ensures your backups don't overwrite each other!
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_file = f"backup_academic_leads_{timestamp}.txt"

    # 3. The Migration Logic: Copying the file
    try:
        shutil.copy2(source_file, backup_file)
        print(f"✅ Backup created successfully: {backup_file}")
        print("🚀 Your innovation data is now geographically redundant (simulated).")
    except Exception as e:
        print(f"❌ Backup failed: {e}")

if __name__ == "__main__":
    create_backup()
