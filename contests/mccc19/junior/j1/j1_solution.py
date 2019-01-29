q=int(input())
for i in range(q):
    f1, f2 = map(int,input().split())
    if f2 > f1:
        print('towards')
    elif f2 < f1:
        print('away')
    else:
        print('none')