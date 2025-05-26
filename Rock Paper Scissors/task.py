import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_choices = []
game_choices.extend([rock, paper, scissors])

user_score = 0
cpu_score = 0

while user_score or cpu_score < 3:
    print(f"User Score: {user_score}. CPU score: {cpu_score}.")
    user_selection = int(input("Choose your weapon: 0 - Rock, 1 - Paper, 2 - Scissors!\n"))
    cpu_selection = random.choice(game_choices)
    cpu_selection_index = game_choices.index(cpu_selection)

    # Game Logic
    # Tie Game
    if user_selection == cpu_selection_index:
        print(game_choices[user_selection])
        print("Computer Chose:")
        print(cpu_selection)
        print("It's a tie.")

    # Rock Conditions
    if user_selection == 0 and cpu_selection_index == 1:
        print(game_choices[user_selection])
        print("Computer Chose:")
        print(cpu_selection)
        print("You Lose.")
        cpu_score +=1
    elif user_selection == 0 and cpu_selection_index == 2:
        print(game_choices[user_selection])
        print("Computer Chose:")
        print(cpu_selection)
        print("You Win!")
        user_score += 1

    # Paper Conditions
    if user_selection == 1 and cpu_selection_index == 2:
        print(game_choices[user_selection])
        print("Computer Chose:")
        print(cpu_selection)
        print("You Lose.")
        cpu_score += 1
    elif user_selection == 1 and cpu_selection_index == 0:
        print(game_choices[user_selection])
        print("Computer Chose:")
        print(cpu_selection)
        print("You Win!")
        user_score += 1

    #Scissor Conditions
    if user_selection == 2 and cpu_selection_index == 0:
        print(game_choices[user_selection])
        print("Computer Chose:")
        print(cpu_selection)
        print("You Lose.")
        cpu_score += 1
    elif user_selection == 2 and cpu_selection_index == 1:
        print(game_choices[user_selection])
        print("Computer Chose:")
        print(cpu_selection)
        print("You Win!")
        user_score += 1

if user_score == 3:
    print(f"You won: {user_score} - {cpu_score}.")
else:
    print(f"You lost: {user_score}- {cpu_score}.")