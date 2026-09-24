Na=int(input("Enter the no of strong positions on road A:"))
Nb=int(input("Enter the no of strong positions on road B:"))
a=[int(input("Enter the strong positions on road A:")) for i in range(Na)]
b=[int(input("Enter the strong positions on road B:")) for i in range(Nb)]
s=sorted(set(a+b))
print(s)
N=len(s)
if N%2==1:
  print(s[N//2])
else:
  print((s[N//2-1]+s[N//2])/2)
