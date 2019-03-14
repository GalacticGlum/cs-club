import sys
input=sys.stdin.readline
n=int(input())
p=[[int(j) for j in input().split()] for i in range(n)]
a=0
for i in range(n):
    x1,y1=p[i]
    x2,y2=p[(i+1)%n]
    a+=(x1*y2)-(y1*x2)
a=abs(a/2)
print(round(a,2))