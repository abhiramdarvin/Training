n = int(input("Enter the no. of elements:"))
large = int(input("Enter number:"))
for i in range(n - 1):
    num = int(input("Enter number:"))
    if num > large:
        large = num
print("Largest number:", large)
