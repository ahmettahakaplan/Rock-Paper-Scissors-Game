print("Welcome to Rock Paper Scissors Game.")
import random
option = ["Rock","rock","Paper","paper","Scissors","scissors"]
Rock = option[0]
rock = option[1]
Paper = option[2]
paper = option[3]
Scissors = option[4]
scissors = option[5]
print("""
Commands
********
Exit=Exit or exit
Rock=Rock or rock
Paper=Paper or paper
Scissors=Scissors or scissors
Lets Play!
********
""")
while True:
    user_choose = input("Choose:")
    pc_random = random.choice(option)
    if user_choose == "Exit" or user_choose == "exit":
        break
    elif user_choose == Rock or user_choose == rock:
        if pc_random == Rock or pc_random == rock:
            print(f"Draw!\nYour choose:Rock\nComputer Choose:Rock")
        elif pc_random == Scissors or pc_random == scissors:
            print(f"You Won!\nYour Choose:Rock\nComputer Choose:Scissors")
        elif pc_random == Paper or pc_random == paper:
            print(f"You Lost!\nYour Choose:Rock\nComputer Choose:Paper")
    #********************************************************************************************
    elif user_choose == Paper or user_choose == paper:
        if pc_random == Paper or pc_random == paper:
            print(f"Draw!\nYour choose:Paper\nComputer Choose:Paper")
        elif pc_random == Rock or pc_random == rock:
            print(f"You Won!\nYour Choose:Paper\nComputer Choose:Rock")
        elif pc_random == Scissors or pc_random == scissors:
            print(f"You Lost!\nYour Choose:Paper\nComputer Choose:Scissors")
    #*********************************************************************************************
    elif user_choose == Scissors or user_choose == scissors:
        if pc_random == Scissors or pc_random == scissors:
            print(f"Draw!\nYour choose:Scissors\nComputer Choose:Scissors")
        elif pc_random == Paper or pc_random == paper:
            print(f"You Won!\nYour Choose:Scissors\nComputer Choose:Paper")
        elif pc_random == Rock or pc_random == rock:
            print(f"You Lost!\nYour Choose:Scissors\nComputer Choose:Rock")
    elif user_choose != Rock or user_choose != rock or user_choose != Paper or user_choose != paper or user_choose != Scissors or user_choose != scissors or user_choose != "Exit" or user_choose != "exit":
        print("Please Enter a Valid Choose!")








