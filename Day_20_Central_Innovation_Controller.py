# ---------------------------------------------------------
# Project: The Central Innovation Controller 🎮
# Day 20/100: Script Integration & Workflow Automation
# Goal: Run a complete data protection and organization cycle.
# ---------------------------------------------------------

import os
import shutil
from datetime import datetime

# --- Module 1: The Fail-Safe (from Day 18) ---
def run_backup(source_file):
    if not os.path.exists(source_file):
        return None
    
    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    backup_name = f"backup_academic_leads_{timestamp}.txt"
    shutil.copy2(source_file, backup_name)
    return backup_name

# --- Module 2: The Architect (from Day 19) ---
def run_organization(archive_dir):
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)
    
    moved_count = 0
    for file in os.listdir("."):
        if file.startswith("backup_") and file.endswith(".txt"):
            shutil.move(file, os.path.join(archive_dir, file))
            moved_count += 1
    return moved_count

# --- Master Execution ---
def automate_workflow():
    print("--- 🛠️  CENTRAL CONTROLLER: STARTING WORKFLOW ---")
    
    vault_file = "academic_leads.txt"
    archive_folder = "Innovation_Archives"

    # Step 1: Backup
    new_backup = run_backup(vault_file)
    if new_backup:
        print(f"🛡️ Step 1: Secure backup created ({new_backup})")
    else:
        print("❌ Step 1: Source vault missing. Workflow aborted.")
        return

    # Step 2: Organize
    count = run_organization(archive_folder)
    print(f"📁 Step 2: Workspace organized. {count} files migrated to archives.")
    
    print("\n✅ WORKFLOW COMPLETE: Your innovation data is safe and organized!")

if __name__ == "__main__":
    automate_workflow()
