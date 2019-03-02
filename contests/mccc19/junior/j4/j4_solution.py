a, b = map(int, input().split())
d = (b*b)*(b+1)*(b+1) - (a*a)*(a-1)*(a-1)
print((d//4)%1000000007)