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

#Write your code below this line 👇
game_images = [rock, paper, scissors]

choice = int(input("What do you choose? \n 0 - rock \n 1 - paper \n 2 - scissors \n"))

if choice >= 3 or choice < 0:
    print("Wrong entry!")
else:  
    print(game_images[choice])

    computer_choice = random.randint(0, 2)
    print(f"Computer chose:")
    print(game_images[computer_choice])


    if choice == 0 and computer_choice == 2:
        print("You won!")
    elif choice == 1 and computer_choice == 0:
        print("You won!")
    elif choice == 2 and computer_choice == 1:
        print("You won!")
    elif choice == 0 and computer_choice == 1:
        print("Computer won!")
    elif choice == 1 and computer_choice == 2:
        print("Computer won!")
    elif choice == 2 and computer_choice == 0:
        print("Computer won!")
    elif computer_choice == choice:
        print("It's a draw. Nobody wins.")
