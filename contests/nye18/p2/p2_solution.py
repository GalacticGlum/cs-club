n = int(input())
orders = [int(i) for i in input().split()]

freq = [0]*6
for i in range(n):
    o = orders[i]
    freq[o-1] += 1

max_freq = 0
for i in range(6):
    if freq[i] > freq[max_freq]:
        max_freq = i

min_freq = 0
for i in range(6):
    if freq[i] < freq[min_freq]:
        min_freq = i

print(max_freq+1, min_freq+1, sep='\n')
