import os
import time

class FileInvestigator:
    def __init__(self, file_path):
        self.path = file_path

    def run_report(self):
        # Checking if the file even exists on your laptop
        if os.path.exists(self.path):
            size_bytes = os.path.getsize(self.path)
            # Converting bytes to KB for easier reading
            size_kb = size_bytes / 1024
            
            # Getting the creation time and making it readable
            created_time = os.path.getctime(self.path)
            readable_time = time.ctime(created_time)

            print(f"--- File Report: {self.path} ---")
            print(f"Status: Found")
            print(f"File Size: {size_kb:.2f} KB")
            print(f"Created On: {readable_time}")
        else:
            print(f"Alert: The file {self.path} does not exist.")

# --- Execution ---
# You can test this by putting the name of a file you created earlier
# For example: "sales_report.txt" from Day 34
investigator = FileInvestigator("sales_report.txt")
investigator.run_report()
