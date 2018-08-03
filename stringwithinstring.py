s1 = str(input())
s2 = str(input())


cnt = 0
for i in range(len(s1)):
    if s1[i:].startswith(s2):
        cnt+=1
    #i += x
print (cnt)