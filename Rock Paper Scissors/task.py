import random

game_choices = []

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

game_choices.extend([rock, paper, scissors])


# compare against
# decide winner

user_selection = int(input("Choose your weapon: 0 - Rock, 1 - Paper, 2 - Scissors!\n"))
cpu_selection = random.choice(game_choices)
cpu_selection_index = game_choices.index(cpu_selection)


# Game Logic
# Rock
if user_selection == cpu_selection:
    print(game_choices[user_selection])
    print("Computer Chose:")
    print(cpu_selection)
    print("It's a tie.")
elif user_selection == 0 and cpu_selection == game_choices[1]:
    print(game_choices[user_selection])
    print("Computer Chose:")
    print(cpu_selection)
    print("You Lose.")
elif user_selection == 0 and cpu_selection == game_choices[2]:
    print(game_choices[user_selection])
    print("Computer Chose:")
    print(cpu_selection)
    print("You Win!")
