from random import randint, random

MAX_RADIUS = 10000
MAX_THETA = 360

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

        for j in range(n):
            radius = randint(1, MAX_RADIUS+1)
            theta = randint(0, MAX_THETA+1)

            input_file.write(f'{radius} {theta}\n')
            arc_length = round((2*3.14*radius*theta)/360,2)
            output_file.write(f'{arc_length}\n')
            