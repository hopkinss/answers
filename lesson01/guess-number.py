import random

target=random.choice(range(1,10))
tries = 0
while True:
    val = input("Enter a number between 1 and 10 or \"Q\" to quit> ")
    if val.upper() == 'Q':
        break
    tries += 1
    val=int(val)
    if val == target:
        print(f"{val} is the number, and it only took you {tries} tries!")
        break;
    if val > target:
        print(f"{val} is too high")
    else:
        print("{} is too low".format(val))
        