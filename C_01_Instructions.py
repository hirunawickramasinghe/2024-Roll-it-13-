# checks users enter yes (y) or no (n)
def yes_no(question):
      while True:
        response = input(question).lower()

        # checks user response, question
        #respeats if users don't enter yes / no
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes / no")


def instructions():
    print('''
    
**** Instructions ****

To begin, decide on a score goal (eg: the first one to get a 
score of 50 wins).

For each round of the game, you win points by rolling dice.
The winner of the round is the onw who gets 13 (or slightly less).

If you win the round, then your scire will increase by the 
number of ponts that you earned. If your first roll of two 
dice is a double (eg: both dice show a three), then yore score 
will be DOUBLE the number of points. 

If you lose the round, then you don't get any points.

If you and thye computer tie (eg: you both get a score of 11,
then you will have 11 points added to your score.

yor goal is to try to get the target score before the 
computer.

Good Luck.
    

    ''')

# Main routine
print()
print("🎲🎲 Roll it 13 🎲🎲")
print()

# loop for testing purposes

want_instructions = yes_no("Do you want to read the instructions? ")

# checks users enter yes (y) or no (n)
if want_instructions == "yes":
    instruction()

print("program continues")
