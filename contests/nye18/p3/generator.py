from random import randint, random

def random_ordered_pair(minv=1):
    return randint(minv, 10000), randint(minv, 10000)

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

        max_area = 0
        loc = ()
        for i in range(n):
            x,y = random_ordered_pair()
            w,h = random_ordered_pair()

            input_file.write(f'{x} {y} {w} {h}\n')
            area = w*h
            if area > max_area:
                max_area = area
                loc = (x,y)

        output_file.write(f'{loc[0]} {loc[1]}\n')

