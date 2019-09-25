import sys
input=sys.stdin.readline

n, c, l = map(int,input().split())
s = set(input().split())
for i in range(n):
    name, line, error = input().split()
    if name in s and int(line) % l == 0:
        print(name, line, error)