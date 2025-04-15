import random

def roll_dice(code):
    valid_dice = [3, 4, 6, 8, 10, 12, 20, 100]
    code = code.upper()
    if "D" not in code:
        return "Invalid format! Missing 'D'."
    parts = code.split("D")
    if parts[0] == '':
        num_rolls = 1
    else:
        try:
            num_rolls = int(parts[0])
        except ValueError:
            return "Invalid number of dice."
    modifier = 0
    dice_and_mod = parts[1]
    if '+' in dice_and_mod:
        dice_part, mod_part = dice_and_mod.split('+')
        modifier = int(mod_part)
    elif '-' in dice_and_mod:
        dice_part, mod_part = dice_and_mod.split('-')
        modifier = -int(mod_part)
    else:
        dice_part = dice_and_mod
    try:
        dice_type = int(dice_part)
    except ValueError:
        return "Invalid dice type."
    if dice_type not in valid_dice:
        return f"Invalid dice type D{dice_type}."
    rolls = [random.randint(1, dice_type) for _ in range(num_rolls)]
    total = sum(rolls) + modifier
    return f"Rolls: {rolls}, Modifier: {modifier}, Total: {total}"

print(roll_dice("2D10+10"))
print(roll_dice("D6"))
print(roll_dice("D12-1"))
print(roll_dice("3D8"))
print(roll_dice("2D7"))
