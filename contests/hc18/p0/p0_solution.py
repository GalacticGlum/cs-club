n=int(input())
for _ in range(n):
    r,theta = map(int,input().split())
    arc_length = (2*3.14*r*theta)/360
    print(round(arc_length,2))