n=int(input())
for i in range(n):
    long,lat,k=map(int,input().split())
    print((long+k)**2-k*long, (lat-k)**2+k*(lat-long)**2)