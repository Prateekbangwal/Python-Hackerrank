n = int(input())

s = set(map(int,input().split()))

N = int(input())

for i in range(0, N):
    args = input().split()
    command = args[0]
    if command == "discard":
        s.discard(int(args[1]))
    elif command == "remove":
        s.remove(int(args[1]))
    else:
        s.pop()

print (sum(s))