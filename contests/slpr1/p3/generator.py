from random import random, sample
from numpy.random import randint
from itertools import accumulate
from math import floor

def uniform_random_list(a, b, n):
    x = a
    result = []
    for i in range(n, 0, -1):
        x += (b-x) * (1-pow(random(), 1. / i))
        result.append(int(x))

    return result

class Query():
    def __init__(self, l, r, result):
        self.l = l
        self.r = r
        self.result = result

min_n = int(input('Min N (and Q): '))
max_n = int(input('Max N (and Q): '))
test_cases = int(input('Test case amount: '))
test_case_prefix = input('Test case file prefix: ')

n_values = uniform_random_list(min_n,max_n+1,test_cases)
q_values = uniform_random_list(min_n,max_n+1,test_cases)
for i in range(1,test_cases+1):
    with open(f'{test_case_prefix}.{i}.in', 'w+') as input_file, \
        open(f'{test_case_prefix}.{i}.out','w+') as output_file:

        n, q = n_values[i-1], q_values[i-1]

        input_file.write(f'{n} {q}\n')

        d_values = [randint(1,10001) for i in range(n)]
        d_values_psa = [0] + list(accumulate(d_values))

        mid = floor(n/2)
        p_values = sample(d_values[:mid], mid) + d_values[mid:]
        p_values_psa = [0] + list(accumulate(p_values))

        queries = []

        for j in range(q):
            r = randint(2, n + 1)
            l = randint(1, r)
            ds = d_values_psa[r]-d_values_psa[l-1]
            ps = p_values_psa[r]-p_values_psa[l-1]

            result = 'WOOHOO!' if ds == ps else 'BOOHOO!'
            queries.append(Query(l,r,result))

        d_values_str = ' '.join(str(k) for k in d_values)
        p_values_str = ' '.join(str(k) for k in p_values)

        input_file.write(f'{d_values_str}\n{p_values_str}\n')

        for query in queries:
            input_file.write(f'{query.l} {query.r}\n')
            output_file.write(f'{query.result}\n')
