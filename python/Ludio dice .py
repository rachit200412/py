import random 

while True:
    input("Press Enter to roll the Ludo dice (or Ctrl+C to quit)...")
    dice = random.randint(1, 6)
    print(f"🎲 You rolled: {dice}")