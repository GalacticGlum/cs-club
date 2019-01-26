n=int(input())
result = True
for i in range(n):
    r, p = map(int,input().split())
    if r != p:
        result=False
        break
print('yes' if result else 'no')