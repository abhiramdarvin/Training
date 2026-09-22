print("Using Temp")
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
temp=a
a=b
b=temp
print("First number",a)
print("Second number",b)
print("Using ,")
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
a,b=b,a
print("First number",a)
print("Second number",b)
print("Using + and -")
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
a=a+b
b=a-b
a=a-b
print("First number",a)
print("Second number",b)
print("Using ^")
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
a=a^b
b=a^b
a=a^b
print("First number",a)
print("Second number",b)
