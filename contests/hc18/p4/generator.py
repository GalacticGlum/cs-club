from random import sample, random, randint, choice

def uniform_random_list(a, b, n):
    x = a
    result = []
    for i in range(n, 0, -1):
        x += (b-x) * (1-pow(random(), 1. / i))
        result.append(int(x))

    return result

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

def solve(entries, queries):
    n = len(entries)
    q = len(queries)
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

    entries.sort(key=lambda x: x.value)
    queries.sort(key=lambda x: x.k)

    current = 0
    results = [0]*q

    for i in range(q):
        while current < n and entries[current].value <= queries[i].k:
            update(entries[current].index + 1, 1)
            current += 1
    
        results[queries[i].index] = query(queries[i].right+1) - query(queries[i].left)

    return results

MAX_COST = MAX_K = 10000

min_n = int(input('Min N: '))
max_n = int(input('Max N: '))
min_q = int(input('Min Q: '))
max_q = int(input('Max Q: '))

test_cases = int(input('Test case amount: '))
test_case_prefix = input('Test case file prefix: ')

n_values = uniform_random_list(min_n,max_n+1,test_cases)
q_values = uniform_random_list(min_q,max_q+1,test_cases)
for i in range(1,test_cases+1):
    with open(f'{test_case_prefix}.{i}.in', 'w+') as input_file, \
        open(f'{test_case_prefix}.{i}.out','w+') as output_file:

        n, q = n_values[i-1], q_values[i-1]
        input_file.write(f'{n} {q}\n')

        entries = []
        for j in range(n):
            value = randint(1, MAX_K)
            entries.append(Entry(value, j))

        values_str = ' '.join(str(e.value) for e in entries)
        input_file.write(f'{values_str}\n')

        queries = []
        for j in range(q):
            r = randint(0, n-1)
            l = randint(0, r)
            k = randint(0, MAX_K)
            queries.append(Query(l, r, k, j))
            input_file.write(f'{l} {r} {k}\n')

        results = solve(entries, queries)
        for result in results:
            output_file.write(f'{result}\n')

            