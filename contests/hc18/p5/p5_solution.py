MAXN = 100000

edges = [[] for i in range(MAXN)]
s = [0]*MAXN
ss = [0]*MAXN
far = [0]*MAXN

def dfs(u, p):
    global s, ss

    for v in edges[u]:
        if v != p:
            dfs(v,u)
            if s[v]+1 > ss[u]:
                ss[u] = s[v]+1
                if ss[u] > s[u]:
                    ss[u],s[u]=s[u],ss[u]

def dfs2(u,p,k):
    global far
    far[u]=max(s[u],k)
    for v in edges[u]:
        if v!=p:      
            dfs2(v,u,max(ss[u] if s[v]+1 == s[u] else s[u], k)+1)

n, m = map(int,input().split())
for i in range(n-1):
    u,v = map(int,input().split())
    u-=1
    v-=1
    edges[u].append(v)
    edges[v].append(u)

dfs(0,-1)
dfs2(0,-1,0)

diameter = max(far)
while m:
    x,y =map(int,input().split())
    print((y-1)*diameter+far[x-1])
    m-=1