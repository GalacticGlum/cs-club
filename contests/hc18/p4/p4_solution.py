import sys
raw_input = sys.stdin.readline

class Query(object):
    def __init__(self, left, right, k, index):
        self.left = left
        self.right = right
        self.k = k
        self.index = index

class Entry(object):
    def __init__(self, value, index):
        self.value = value
        self.index = index

n,q = map(int,raw_input().split())
bit = [0]*(n+1)

def update(index, value):
    while index <= n:
        bit[index] += value
        index += index & -index

def query(index):
    result = 0
    while index > 0:
        result += bit[index]
        index -= index & -index

    return result

costs = [int(i) for i in raw_input().split()]
entries = []
for i in range(n):
    entries.append(Entry(costs[i], i))

queries = []
for i in range(q):
    l,r,k = map(int,raw_input().split())
    queries.append(Query(l, r, k, i))

entries.sort(key=lambda x: x.value)
queries.sort(key=lambda x: x.k)

current = 0
results = [0]*q

for i in range(q):
    while current < n and entries[current].value <= queries[i].k:
        update(entries[current].index + 1, 1)
        current += 1
    
    results[queries[i].index] = query(queries[i].right+1) - query(queries[i].left)

for i in range(q):
    print(results[i])