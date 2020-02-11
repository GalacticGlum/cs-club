from random import randint, random
from time import time

min_n = int(input('Min N: '))
max_n = int(input('Max N: '))
k_value = int(input('K value (-1 for default): '))

test_cases = int(input('Test case amount: '))
test_case_prefix = input('Test case file prefix: ')

def bits(binary):
    w = 0
    yield w
    for v in binary:
        w ^= v
        yield w

for i in range(1,test_cases+1):
    with open(f'{test_case_prefix}.{i}.in', 'w+') as input_file, \
        open(f'{test_case_prefix}.{i}.out','w+') as output_file:

        n = randint(min_n, max_n)
        q = randint(min_n, max_n)

        print(f'Generating test case {i} (n={n}, q={q})...')
        start_time = time()
        strain_type = [randint(0, 1) for _ in range(n)]

        c = [[0]*(n+2), [0]*(n+2)]
        for i, v in enumerate(bits(strain_type)):
            for j in range(2):
                c[j][i+1] = c[j][i] + (j==v)

        input_file.write('{} {}\n{}\n'.format(n, q, ''.join(str(v) for v in strain_type)))
        for _ in range(q):
            x = randint(0, n - 2)
            y = randint(x, n - 1)
            k = k_value if k_value != -1 else randint(0, n)
            input_file.write('{} {} {}\n'.format(x, y, k))
            
            y += 2
            result = (y - x) // 2 * ((y - x + 1) // 2) if k else (c[1][y] - c[1][x]) * (c[0][y] - c[0][x])
            output_file.write('{}\n'.format(result))

        print(f'-> Completed generating data... ({round(time() - start_time, 3)} seconds elapsed)')