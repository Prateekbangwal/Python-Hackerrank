input()
A = set(map(int, input().split()))

for i in range(int(input())):
    operation = input().split()[0]
    otherSet = set(map(int, input().split()))

    if operation == "update":
        A.update(otherSet)
    elif operation == "intersection_update":
        A.intersection_update(otherSet)
    elif operation == "difference_update":
        A.difference_update(otherSet)
    else: #symmetric_difference_update:
        A.symmetric_difference_update(otherSet)

print (sum(A))