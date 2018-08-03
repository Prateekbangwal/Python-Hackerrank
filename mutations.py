s=input()
in_str_ar=input().strip().split()
pos=int(in_str_ar[0])
c=in_str_ar[1]
final_str=s[:pos]+c+s[pos+1:]
print (final_str)