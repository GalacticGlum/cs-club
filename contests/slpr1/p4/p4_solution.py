k,n=map(int,input().split())
cache=[0]*(10000+3)
for i in range(n):
    c,s = map(int,input().split())
    j=k
    while j >= c:
        cache[j]=max(cache[j-c]+s,cache[j])
        j-=1
        
print(cache[k])