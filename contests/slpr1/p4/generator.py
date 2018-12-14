from random import random, sample
from numpy.random import randint
from math import floor

def get_max(k, n, costs, satisfactions,max_n):
    cache = [0]*(max_n+3)
    for i in range(n):
        j=k
        while j >= costs[i]:
            cache[j]=max(cache[j-costs[i]]+satisfactions[i],cache[j])
            j-=1

    return cache[k]

def uniform_random_list(a, b, n):
    x = a
    result = []
    for i in range(n, 0, -1):
        x += (b-x) * (1-pow(random(), 1.0 / i))
        result.append(int(x))

    return result

min_n = int(input('Min N (and K): '))
max_n = int(input('Max N (and K): '))
test_cases = int(input('Test case amount: '))
test_case_prefix = input('Test case file prefix: ')

MIN_COST=1
MAX_COST=max_n

MIN_SATISFACTION=-100
MAX_SATISFACTION=1000

n_values = uniform_random_list(min_n,max_n+1,test_cases)
k_values = uniform_random_list(min_n,max_n+1,test_cases)
for i in range(1,test_cases+1):
    with open(f'{test_case_prefix}.{i}.in', 'w+') as input_file, \
        open(f'{test_case_prefix}.{i}.out','w+') as output_file:

        k, n = k_values[i-1], n_values[i-1]
        input_file.write(f'{k} {n}\n')

        costs = []
        satisfactions = []
        for j in range(n):
            cost = randint(MIN_COST, MAX_COST)
            satisfaction = randint(MIN_SATISFACTION, MAX_SATISFACTION)

            costs.append(cost)
            satisfactions.append(satisfaction)

            input_file.write(f'{cost} {satisfaction}\n')

        max_satisfaction = get_max(k, n, costs, satisfactions, max_n)
        output_file.write(f'{max_satisfaction}\n')