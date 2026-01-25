# ---------------------------------------------------------
# Project: The Automated Workspace Architect 🏗️
# Day 19/100: Directory Management & File Sorting
# Goal: Automatically organize backups into an Archive folder.
# ---------------------------------------------------------

import os
import shutil

def organize_workspace():
    print("--- 🏗️  WORKSPACE ARCHITECT: INITIALIZED ---")
    
    archive_folder = "Innovation_Archives"
    
    # 1. Create the Archive folder if it doesn't exist
    if not os.path.exists(archive_folder):
        os.makedirs(archive_folder)
        print(f"📁 Created new directory: {archive_folder}")

    # 2. Identify all backup files
    # We look for files starting with 'backup_' and ending in '.txt'
    count = 0
    for filename in os.listdir("."):
        if filename.startswith("backup_") and filename.endswith(".txt"):
            # 3. Move the file into the Archive folder
            source_path = filename
            destination_path = os.path.join(archive_folder, filename)
            
            shutil.move(source_path, destination_path)
            print(f"📦 Moved: {filename} -> {archive_folder}/")
            count += 1

    if count > 0:
        print(f"\n✅ Success: {count} backup(s) organized.")
    else:
        print("\n✨ Workspace is already clean!")

if __name__ == "__main__":
    organize_workspace()
