x=int(input())
t=int(input())
y=int(input())
n = int (input())
print ([ [ i, j, k] for i in range( x + 1) for j in range( t + 1) for k in range(y+1) if ( ( i + j+k) != n )])