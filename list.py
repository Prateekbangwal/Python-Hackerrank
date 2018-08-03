num=int(input())
arr = []
for n in range(num):
    x=input().split(" ")
    command = x[0]
    if command == 'append':
        arr.append((x[1]))
    if command == 'print':
        print(arr)
    if command == 'insert':
        arr.insert(int(x[1]),int(x[2]))
        print(arr)
    if command == 'reverse':
        arr.reverse()
        pritn(arr)
    if command == 'pop':
        arr.pop()
        print(arr)
    if command == 'sort':
        arr.sort()
        print(arr)
    if command == 'remove':
        arr.remove(int(x[1]))
    print (arr)

