from random import randint, random

MAX_VALUE = 1000000

def random_coordinate():
    return randint(0, MAX_VALUE+1), randint(0,MAX_VALUE+1)

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
        mx, my = random_coordinate()
        input_file.write(f'{n}\n{mx} {my}\n')

        max_value = 0

        for j in range(n):
            x, y = random_coordinate()
            s = randint(0, MAX_VALUE+1)

            distance = (mx-x)**2 + (my-y)**2
            max_value = max(max_value, abs(distance-s))

            input_file.write(f'{x} {y} {s}\n')

        output_file.write(f'{max_value}\n')

            