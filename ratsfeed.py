r = int(input("Enter the no. of rats:"))
unit = int(input("Enter the unit of food each rat consumes:"))
n = int(input("Enter the no. of houses:"))
arr = list(map(int, input("Enter the amount of food present in the each house:").split()))
required = r * unit
total = 0
houses = 0
for food in arr:
    total += food
    houses += 1

    if total >= required:
        break
if total < required:
    print(0)
else:
    print("Minimum no. of houses required to feed all rats:",houses)
