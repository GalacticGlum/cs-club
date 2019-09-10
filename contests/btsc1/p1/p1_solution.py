n=int(input())
coins=map(int,input().split())

freq={}
for c in coins:
    if c not in freq:
        freq[c] = 0
    freq[c]+=1

remaining = n-max(freq.values())
print('second' if remaining % 2 == 0 else 'first')
print(remaining)