import random

# Define the game parameters
POSSIBLE_NUMBERS = list(range(1, 51))
NUM_WINNING_NUMBERS = 6
JACKPOT_PERCENTAGE = 0.5

# Define the player's ticket
player_ticket = set()

# Ask the player to select 6 unique numbers between 1 and 50
while len(player_ticket) < 6:
    selected_number = int(input("Please select a number between 1 and 50: "))
    if selected_number not in player_ticket and selected_number in POSSIBLE_NUMBERS:
        player_ticket.add(selected_number)
    else:
        print("Invalid selection. Please select a number between 1 and 50 that you have not already selected.")

# Draw the winning numbers randomly from the possible numbers
winning_numbers = set(random.sample(POSSIBLE_NUMBERS, NUM_WINNING_NUMBERS))

# Compare the player's ticket to the winning numbers
num_correct_numbers = len(player_ticket.intersection(winning_numbers))

# Calculate the player's prize based on the number of correct numbers
if num_correct_numbers == 6:
    print("Congratulations! You've won the jackpot!")
    # Calculate the jackpot prize based on the total ticket sales
    jackpot_prize = JACKPOT_PERCENTAGE * total_ticket_sales
    print(f"The jackpot prize is ${jackpot_prize:.2f}.")
elif num_correct_numbers > 0:
    print(f"You've correctly guessed {num_correct_numbers} number(s).")
    # Calculate the smaller prize based on the total ticket sales and number of winners
    smaller_prize = (1 - JACKPOT_PERCENTAGE) * total_ticket_sales / num_correct_numbers
    print(f"You've won a prize of ${smaller_prize:.2f}.")
else:
    print("Sorry, you did not win a prize this time.")

