import random


class DiceRoller:
    def __init__(self, dice, roller, roll, count):
        self.dice = dice
        self.roller = roller
        self.roll = roll
        self.count = count

    def check_input(self):
        self.roll = True
        self.count = 0
        while self.roll:
            if self.count == 0:
                self.roller = input("Would you like to roll? Press y/n ")
            else:
                self.roller = input("Would you like to roll again? Press y/n ")
            if self.roller == "y":
                my_dice.roll_dice()
                self.count += 1
            elif self.roller == "n":
                print("Okay, goodbye.")
                self.roll = False
            else:
                print("ERROR, invalid input. Try again.")

    def roll_dice(self):
        self.dice = str(random.randint(1, 6))
        print('The roll is ' + self.dice)


my_dice = DiceRoller(1, "", True, 0)
my_dice.check_input()
