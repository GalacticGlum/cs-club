n,q = map(int,input().split())
costs = [int(i) for i in input().split()]

for i in range(q):
    l,r,k = map(int,input().split())
    count = 0
    for j in range(l, r+1):
        if costs[j]<=k:
            count+=1

    print(count)