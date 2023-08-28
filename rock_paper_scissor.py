import random 

game_image = ["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
]

user_choice=int(input("write 0 to choose rock, 1 to paper, 2 to scissor.  "))
print()
print("Your choice")
print(game_image[user_choice])


computer_choice = random.randint(0,len(game_image)-1)
print("Computer choice")
print(game_image[computer_choice])


# 0-stone
# 1-paper
# 2-scissor

if user_choice == computer_choice:
    print("game draw")
else:
    if user_choice >= 3 or user_choice < 0:
        print("Invalid type. You loose the game")
    elif user_choice == 0 and computer_choice == 2:
            print("You win the game")
    elif user_choice == 1 and computer_choice == 0:
            print("You win the game")
    elif user_choice == 2 and computer_choice == 1:
            print("You win the game")
    else:
        print("Computer win the game")

