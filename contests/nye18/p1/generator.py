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
        values = [randint(1,100) for i in range(n)]
        values_str = ' '.join(str(v) for v in values)

        input_file.write(f'{n}\n{values_str}\n')
        for v in values:
            result = 'yes' if v > 20 else 'no'
            output_file.write(f'{result}\n')
            

            