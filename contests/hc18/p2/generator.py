from random import sample, random

def uniform_random_list(a, b, n):
    x = a
    result = []
    for i in range(n, 0, -1):
        x += (b-x) * (1-pow(random(), 1. / i))
        result.append(int(x))

    return result

def solve(works):
    def get_current_state(start, previous):
        if previous != -1:
            if previous - start == 0:
                return f'{previous}'
            elif previous - start == 1:
                return f'{start} {previous}'
            else:
                return f'{start}-{previous}'

    works = sorted(works)
    start = -1
    previous = -1

    result = []
    for work in works:
        if work != previous + 1:
            r=get_current_state(start, previous)
            if r != None:
                result.append(r)
                
            start = work
            previous = work
        else:
            previous = work
    
    r=get_current_state(start,previous)
    if r != None:
        result.append(r)
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
        values = sample(range(1,max_n+1),n)

        values_str = ' '.join(str(i) for i in values)
        result_str = ' '.join(solve(values))

        input_file.write(f'{n}\n{values_str}\n')
        output_file.write(f'{result_str}\n')


            