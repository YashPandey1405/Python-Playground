import random

'''
1 for snake
-1 for water 
0 for gun
'''
computer = random.choice([-1, 0, 1])

youstr = input("Enter your choice (s for Snake, w for Water, g for Gun): ").strip().lower()

youDict = {
    "s": 1, 
    "w": -1, 
    "g": 0
}

reverseDict = {
    1: "Snake", 
    -1: "Water", 
    0: "Gun"
}

if youstr not in youDict:
    print("Invalid choice! Please enter 's', 'w', or 'g'.")
else:
    you = youDict[youstr]
    print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

    if computer == you:
        print("It's a draw!")
    else:
        if (computer - you) == -1 or (computer - you) == 2:
            print("You lose!")
            
        else:
            print("You win!")
