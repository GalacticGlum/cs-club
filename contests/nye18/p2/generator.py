from random import randint, random

def uniform_random_list(a, b, n):
    x = a
    result = []
    for i in range(n, 0, -1):
        x += (b-x) * (1-pow(random(), 1. / i))
        result.append(int(x))

    return result

min_n = int(input('Min N: '))
max_n = int(input('Max N: '))
test_cases = int(input('Test case amount: '))
test_case_prefix = input('Test case file prefix: ')

n_values = uniform_random_list(min_n,max_n+1,test_cases)
for i in range(1,test_cases+1):
    with open(f'{test_case_prefix}.{i}.in', 'w+') as input_file, \
        open(f'{test_case_prefix}.{i}.out','w+') as output_file:

        n = n_values[i-1]
        input_file.write(f'{n}\n')

        orders = []
        freq = [0]*6
        for i in range(n):
            o = randint(1,6)
            orders.append(o)
            freq[o-1]+=1

        orders_str = ' '.join(str(i) for i in orders)
        input_file.write(f'{orders_str}\n')

        max_freq = 0
        for i in range(6):
            if freq[i] > freq[max_freq]:
                max_freq = i

        min_freq = 0
        for i in range(6):
            if freq[i] < freq[min_freq]:
                min_freq = i

        output_file.write(f'{max_freq+1}\n{min_freq+1}\n')


