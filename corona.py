N = int(input("Enter the size of array:"))
V = list(map(int, input("Enter the elements:").split()))
n = int(input("Enter the no. of spikes:"))
result = []
for x in V:
    result.append(x >> n)
print("Result:",*result)
