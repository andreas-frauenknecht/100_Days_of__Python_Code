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

hand_sign = [rock,paper,scissors]
human_choice = int(input("What would you choose? Rock(0), Paper(1) or Scissors(2)"))
computer_choice = random.randint(0,2)
if human_choice > 2 or human_choice < 0:
    print("You entered a wrong number, you loose")
else:
    print("You chose:")
    print(hand_sign[human_choice])
    print ("Computer chose:")
    print(hand_sign[computer_choice])

    if human_choice == 0 and computer_choice == 2:
        print("You win")
    elif computer_choice ==0 and human_choice ==2:
        print("You loose")
    elif computer_choice > human_choice:
        print("You loose")
    elif computer_choice == human_choice:
        print("It was a draw")
    elif human_choice > computer_choice:
        print("You win")
