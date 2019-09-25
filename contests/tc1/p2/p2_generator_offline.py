from string import ascii_lowercase
from random import randint, random, choice, choices, sample, seed as reseed

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
        c = randint(1, 10)
        l = randint(1, 10)

        input_file.write(f'{n} {c} {l}\n')
        wordset = [''.join(choices(ascii_lowercase, k=randint(1, 10))) for i in range(max(1000, n))]
        candidate_filenames = sample(wordset, k=c)
        candidate_filenames_set = set(candidate_filenames)
        input_file.write(' '.join(candidate_filenames) + '\n')

        wordset = list(set(wordset) - candidate_filenames_set)
        for i in range(n):
            if random() <= 0.5:
                name = choice(candidate_filenames)
            else:
                name = choice(wordset)

            line_number = l * randint(1, 15)
            if random() <= 0.5:
                line_number += 1

            error = ''.join(choices(ascii_lowercase, k=randint(1,5)))
            input_file.write(f'{name} {line_number} {error}\n')
            if name in candidate_filenames_set and line_number % l == 0:
                output_file.write(f'{name} {line_number} {error}\n')
