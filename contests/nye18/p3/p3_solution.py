n=int(input())
max_area=0
px=0
py=0
for i in range(n):
    x,y,w,h=map(int,input().split())
    area=w*h
    if area > max_area:
        max_area=area
        px=x
        py=y
    
print(px,py)