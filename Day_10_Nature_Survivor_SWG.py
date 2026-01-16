# ---------------------------------------------------------
# Project: The Nature Survivor (S-W-G Edition) 🏔️
# Day 10/100: Standard vs. Algorithmic Logic
# ---------------------------------------------------------

import random

def play_survival_game():
    print("--- 🏔️  WELCOME TO THE NATURE SURVIVOR CHALLENGE ---")
    
    # 1. Setup & Choice Generation
    user_map = {"s": 1, "w": -1, "g": 0}
    name_map = {1: "Snake 🐍", -1: "Water 💧", 0: "Gun 🔫"}
    computer = random.choice([-1, 0, 1])
    
    raw_input = input("Enter your choice (S, W, or G): ").strip().lower()
    if raw_input not in user_map:
        print("❌ Invalid Choice!")
        return
    you = user_map[raw_input]

    print(f"\n👤 You: {name_map[you]} | 🤖 Bot: {name_map[computer]}")

    # --- METHOD 1: READABLE LOGIC (Best for Teams) ---
    if computer == you:
        print("🤝 Result: It's a DRAW!")
    else:
        # Standard logic you wrote
        if (computer == -1 and you == 1) or \
           (computer == 1 and you == 0) or \
           (computer == 0 and you == -1):
            print("🏆 Result: YOU WIN!")
        else:
            print("💀 Result: YOU LOSE!")

    # --- METHOD 2: MATHEMATICAL LOGIC (The "Short" Engineer Method) ---
    '''
    PRO LOGIC: Instead of checking 6 conditions, we use (computer - you).
    Based on our mapping (1, -1, 0):
    If (computer - you) is -2 or 1, the player wins.
    This reduces the code significantly!
    '''
    # result = computer - you
    # if (result == -2 or result == 1): print("Math says: You Win!")

if __name__ == "__main__":
    play_survival_game()
