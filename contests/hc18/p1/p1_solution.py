n=int(input())
mx,my=map(int,input().split())
max_value=0
for i in range(n):
    x,y,s=map(int,input().split())
    distance=(mx-x)**2+(my-y)**2
    max_value=max(max_value,abs(distance-s))

print(max_value)