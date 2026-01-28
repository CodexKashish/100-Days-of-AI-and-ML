# ---------------------------------------------------------
# Project: The Bulletproof Innovation Search 🛡️
# Day 22/100: Advanced Error Handling (Try/Except)
# Goal: Make sure the program never crashes, even if files are missing.
# ---------------------------------------------------------

def safe_search():
    print("--- 🛡️  BULLETPROOF SEARCH: ACTIVE ---")
    
    # We 'TRY' the code that might cause a problem
    try:
        filename = "academic_leads.txt"
        query = input("🔍 Search for a University: ").strip().lower()

        with open(filename, "r") as vault:
            found = False
            for line in vault:
                if query in line.lower():
                    print(f"✨ Match Found: {line.strip()}")
                    found = True
            
            if not found:
                print("⚠️ No matches found.")

    # We 'EXCEPT' (catch) the error if the file is missing
    except FileNotFoundError:
        print("❌ ERROR: The vault file is missing! Please create a lead first.")
    
    # We 'EXCEPT' any other weird technical problems
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")
    
    # This runs no matter what!
    finally:
        print("\n🚀 System check complete. Staying resilient.")

if __name__ == "__main__":
    safe_search()
