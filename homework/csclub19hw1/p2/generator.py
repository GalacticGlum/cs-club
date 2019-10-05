from random import randint, random
from string import ascii_lowercase

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
m_values = uniform_random_list(min_n,max_n+1,test_cases)
for i in range(1,test_cases+1):
    with open(f'{test_case_prefix}.{i}.in', 'w+') as input_file, \
        open(f'{test_case_prefix}.{i}.out','w+') as output_file:

        n,m = n_values[i-1],m_values[i-1]
        input_file.write(f'{n} {m}\n')

        r = [randint(0, 10**4) for _ in range(n)]
        t = [randint(0, 10**4) for _ in range(m)]

        r_str = ' '.join(str(v) for v in r)
        t_str = ' '.join(str(v) for v in t)
        input_file.write(f'{r_str}\n{t_str}\n')

        r.sort()
        t.sort()

        count = 0
        index = 0
        for j in range(m):
            if index < n and t[j] >= r[index]:
                count += 1
                index += 1
        
        output_file.write(f'{count}\n')
        