#author : Chit Ko Ko

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

#Write your code below this line 👇

import random

choices = [rock, paper, scissors]

user_input = int(input("What do you choose? Type 0 for rock, 1 for paper, or 2 for scissors: "))
computer_choice = random.randint(0, 2)

print(choices[user_input])
print("Computer choose:")
print(choices[computer_choice])

if user_input == computer_choice:
    print("It's a tie!")
elif user_input == 0 and computer_choice == 2:
    print("You win!")
elif user_input == 1 and computer_choice == 0:
    print("You win!")
elif user_input == 2 and computer_choice == 1:
    print("You win!")
else:
    print("You lose!")

