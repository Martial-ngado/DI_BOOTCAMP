# ============================================================
# rock-paper-scissors.py
# Complete Rock, Paper, Scissors game in a single file.
# Contains the Game class + all menu/control functions.
# ============================================================

import random  # Used to randomly select the computer's item


# ════════════════════════════════════════════════════════════
# CLASS: Game
# Handles a single round of Rock, Paper, Scissors
# ════════════════════════════════════════════════════════════

class Game:
    """
    Represents one round of Rock, Paper, Scissors.
    Handles user input, computer selection,
    result logic, and round output.
    """

    # The three valid items a player can choose
    VALID_ITEMS = ["rock", "paper", "scissors"]

    # Win conditions: each key beats its corresponding value
    WIN_CONDITIONS = {
        "rock": "scissors",    # rock crushes scissors
        "scissors": "paper",   # scissors cuts paper
        "paper": "rock",       # paper covers rock
    }

    def get_user_item(self):
        """
        Repeatedly asks the user to select rock, paper, or scissors.
        Loops until a valid choice is entered.
        Returns the validated choice as a lowercase string.
        """
        while True:
            # Get input, strip whitespace, convert to lowercase
            user_input = input("\nYour move — enter rock, paper, or scissors: ").strip().lower()

            if user_input in self.VALID_ITEMS:
                return user_input  # Valid — exit loop
            else:
                print(f"  ❌ '{user_input}' is not valid. Please choose rock, paper, or scissors.")

    def get_computer_item(self):
        """
        Randomly picks rock, paper, or scissors for the computer.
        Uses random.choice() on the VALID_ITEMS list.
        Returns the computer's choice as a string.
        """
        return random.choice(self.VALID_ITEMS)

    def get_game_result(self, user_item, computer_item):
        """
        Compares the two items and returns the round result.

        Parameters:
            user_item     (str): user's choice
            computer_item (str): computer's choice

        Returns:
            'win'  — user beats the computer
            'draw' — both chose the same item
            'loss' — computer beats the user
        """
        if user_item == computer_item:
            return "draw"  # Same item → draw
        elif self.WIN_CONDITIONS[user_item] == computer_item:
            return "win"   # User's item beats computer's item
        else:
            return "loss"  # Computer wins

    def play(self):
        """
        Runs a full single round:
          1. Gets user's item
          2. Gets computer's item
          3. Determines and prints the result
          4. Returns 'win', 'draw', or 'loss'
        """
        user_item     = self.get_user_item()      # Step 1
        computer_item = self.get_computer_item()  # Step 2
        result        = self.get_game_result(user_item, computer_item)  # Step 3

        # Build result message based on outcome
        if result == "win":
            outcome_msg = "🎉 You win!"
        elif result == "draw":
            outcome_msg = "🤝 It's a draw!"
        else:
            outcome_msg = "💻 Computer wins!"

        # Print round summary
        print(f"\n  You selected     : {user_item.capitalize()}")
        print(f"  Computer selected: {computer_item.capitalize()}")
        print(f"  Result           : {outcome_msg}")

        return result  # Step 4 — return result for score tracking


# ════════════════════════════════════════════════════════════
# FUNCTION 1: get_user_menu_choice
# ════════════════════════════════════════════════════════════

def get_user_menu_choice():
    """
    Displays the main menu and returns the user's validated choice.
    Returns None if the input is invalid (loop stays in main()).

    Returns:
        '1' — play a new game
        '2' — show current scores
        'q' — quit
        None — invalid input
    """
    # Print the menu
    print("\n" + "=" * 40)
    print("       🪨  ROCK · PAPER · SCISSORS  ✂️")
    print("=" * 40)
    print("  1 — Play a new game")
    print("  2 — Show current scores")
    print("  q — Quit")
    print("-" * 40)

    # Read and clean the input
    choice = input("  Your choice: ").strip().lower()

    # Validate — only '1', '2', or 'q' are accepted
    if choice not in ["1", "2", "q"]:
        print(f"  ❌ '{choice}' is not valid. Please choose 1, 2, or q.")
        return None

    return choice


# ════════════════════════════════════════════════════════════
# FUNCTION 2: print_results
# ════════════════════════════════════════════════════════════

def print_results(results):
    """
    Prints a formatted summary of all games played.

    Parameters:
        results (dict): {'win': int, 'loss': int, 'draw': int}
    """
    # Calculate total games played
    total = results["win"] + results["loss"] + results["draw"]

    print("\n" + "=" * 40)
    print("         📊  GAME SUMMARY")
    print("=" * 40)
    print(f"  🎮 Total games played : {total}")
    print(f"  🏆 Wins               : {results['win']}")
    print(f"  💻 Losses             : {results['loss']}")
    print(f"  🤝 Draws              : {results['draw']}")

    # Show win rate only if at least one game was played
    if total > 0:
        win_rate = (results["win"] / total) * 100
        print(f"  📈 Win rate           : {win_rate:.1f}%")

    print("=" * 40)
    print("  Thanks for playing! See you next time 👋")
    print("=" * 40 + "\n")


# ════════════════════════════════════════════════════════════
# FUNCTION 3: main
# ════════════════════════════════════════════════════════════

def main():
    """
    Main game loop. Controls the full program flow:
      - Shows the menu repeatedly until the user quits
      - Creates a new Game object for each round
      - Tracks cumulative scores across all rounds
      - Displays the final summary on exit
    """
    # Initialize score tracker — all counts start at 0
    results = {"win": 0, "loss": 0, "draw": 0}

    print("\n  Welcome to Rock, Paper, Scissors! 🎮")

    # ── Main loop — runs until the user types 'q' ──────────
    while True:
        choice = get_user_menu_choice()  # Show menu, get input

        # Invalid input — menu already showed error, try again
        if choice is None:
            continue

        # ── Play a new game ────────────────────────────────
        elif choice == "1":
            game   = Game()        # Create a new Game instance
            result = game.play()   # Run the round, get result
            results[result] += 1   # Increment the right counter

        # ── Show current scores ────────────────────────────
        elif choice == "2":
            total_so_far = sum(results.values())  # Total games played so far

            if total_so_far == 0:
                print("\n  ℹ️  No games played yet. Start playing first!")
            else:
                print_results(results)  # Display mid-session summary

        # ── Quit ───────────────────────────────────────────
        elif choice == "q":
            print_results(results)  # Show final summary
            break                   # Exit the while loop


# ── Entry point ───────────────────────────────────────────────
# Ensures main() only runs when the script is executed directly,
# not when imported as a module elsewhere.
if __name__ == "__main__":
    main()