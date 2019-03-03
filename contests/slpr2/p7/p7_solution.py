import sys
input=sys.stdin.readline

INF=float('inf')
MAXN=1000
d = [[INF]*MAXN for j in range(MAXN)]

n,m,q=map(int,input().split())
for _ in xrange(m):
    x,y,z=map(int,input().split())
    d[x-1][y-1]=min(d[x-1][y-1],z)
    d[y-1][x-1]=min(d[y-1][x-1],z)
    
for k in xrange(n):
    for i in xrange(n):
        for j in xrange(n):
            if d[i][k] + d[k][j] < d[i][j]:
                d[i][j]=d[i][k] + d[k][j]
                
for i in xrange(q):
    a,b=map(int,input().split())
    if d[a-1][b-1] == INF:
        print(-1)
    else:
        print(d[a-1][b-1])