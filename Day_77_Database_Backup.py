import shutil
import os
from datetime import datetime

original_db = "campus.db"
backup_folder = "db_backups"

if not os.path.exists(backup_folder):
    os.makedirs(backup_folder)

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
backup_name = f"backup_campus_{timestamp}.db"

shutil.copy2(original_db, os.path.join(backup_folder, backup_name))

print("--- Day 77: Backup Successful ---")
print(f"New Backup Created: {backup_name}")
print(f"Location: {backup_folder}/")
