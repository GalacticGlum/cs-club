n=int(input())
for _ in range(n):
    o,x,y=input().split()
    x,y=float(x),float(y)
    if o == 'ADD': print(round(x+y,2))
    if o == 'SUB': print(round(x-y,2))
    if o == 'MUL': print(round(x*y,2))
    if o == 'DIV': print(round(x/y,2))
    if o == 'POW': print(round(x**y,2))