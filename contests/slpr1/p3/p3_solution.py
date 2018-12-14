import sys
raw_input = sys.stdin.readline
n,q = map(int, raw_input().split())
d_values=[int(i) for i in raw_input().split()]
p_values=[int(i) for i in raw_input().split()]

d_psa=[0]
p_psa=[0]

for i in range(1,n+1):
    d_psa.append(d_psa[i-1]+d_values[i-1])
    p_psa.append(p_psa[i-1]+p_values[i-1])
    
for i in range(q):
    l,r = map(int,raw_input().split())
    ds = d_psa[r]-d_psa[l-1]
    ps = p_psa[r]- p_psa[l-1]
    
    if ds == ps:
        print 'WOOHOO!'
    else:
        print 'BOOHOO!'
