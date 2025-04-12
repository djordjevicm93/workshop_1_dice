# roll 2D10+20
# xDy+z
# y – type of dice to use (e.g. D6, D10)
# x – number of dice rolled; for a single roll this parameter is omitted
# z – modifier - number to add (or subtract) to the result of the roll (optional)
# D3, D4, D6, D8, D10, D12, D20, D100

from random import randint

dice_types = [3, 4, 6, 8, 10, 12, 20, 100]

def dice(score_of_dice):
    for y in dice_types:
        if y in score_of_dice:
            return randint(int(y))
        else:
            return "Not in dice types. Select right one."
        if x in score_of_dice:
            return sum(x, y)
        else:
            return None
        if z in score_of_dice:
            return score_of_dice + z or score_of_dice - z
        return x + y + z or x + y - z

