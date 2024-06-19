import random

def get_user_choice():
    user_choice = input("Enter your choice (rock, paper, or scissors): ")
    while user_choice.lower() not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        user_choice = input("Enter your choice (rock, paper, or scissors): ")
    return user_choice.lower()

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    user_score = 0
    computer_score = 0
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")
        result = determine_winner(user_choice, computer_choice)
        print(result)
        if 'win' in result:
            user_score += 1
        elif 'tie' not in result:
            computer_score += 1
        print(f"Score - You: {user_score}, Computer: {computer_score}")
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            print("Thanks for playing!")
            break

# Main
print("Let's play Rock-Paper-Scissors!")
play_game()
