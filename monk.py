n=int(input("Enter total no. of monkeys:"))
k=int(input("Enter no. of banana monkey can eat:"))
j=int(input("Enter no. of peanut monkey can eat:"))
m=int(input("Enter total no. of banana:"))
p=int(input("Enter total no. of peanut:"))
if(k==0 or j==0):
  print("INVALID INPUT")
else:
  n=n-(m//k+p//j)
  if(m%k!=0 or p%k!=0):
    n=n-1
  print("No. of monkeys in tree:",n)
