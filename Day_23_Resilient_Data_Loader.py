# ---------------------------------------------------------
# Project: The Infinite Resilience Loop 🔄
# Day 23/100: Combining Loops with Error Handling
# Goal: Create a system that retries until a valid file is found.
# ---------------------------------------------------------

import time

def resilient_loader():
    print("--- 🔄 RESILIENT DATA LOADER: ACTIVE ---")
    
    while True:
        try:
            filename = input("📂 Enter the vault filename to load (e.g., academic_leads.txt): ").strip()
            
            # Trying to open the file
            with open(filename, "r") as vault:
                content = vault.readlines()
                print(f"✅ Success! {len(content)} leads loaded from '{filename}'.")
                break  # Exit the loop only when successful!

        except FileNotFoundError:
            print(f"❌ '{filename}' not found. Let's try again in 2 seconds...")
            time.sleep(2) # Adding a small pause for a professional feel
            print("--- REBOOTING SEARCH ---")
            
        except Exception as e:
            print(f"⚠️ Unexpected error: {e}")
            break # Exit on serious unknown errors

if __name__ == "__main__":
    resilient_loader()
    print("\n🚀 Day 23 Complete: System never quits.")
