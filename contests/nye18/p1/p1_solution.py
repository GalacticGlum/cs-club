n=int(input())
values=[int(i) for i in input().split()]
for v in values:
    if v > 20:
        print('yes')
    else:
        print('no')