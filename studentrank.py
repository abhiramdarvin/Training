n = int(input("Enter the no. of students:"))
ranks = list(map(int, input("Enter the rank of each student:").split()))
count = 0
previous = float('inf')
for rank in ranks:
    if rank < previous:
        count += 1
        previous = rank
print("No. of rank cut in the list:",count)
