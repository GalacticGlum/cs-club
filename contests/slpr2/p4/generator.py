from random import randint, random, choice, choices, sample
from string import ascii_lowercase
from math import floor

def uniform_random_list(a, b, n):
    x = a
    result = []
    for i in range(n, 0, -1):
        x += (b-x) * (1-pow(random(), 1. / i))
        result.append(int(x))

    return result

min_n = int(input('Min N: '))
max_n = int(input('Max N: '))
min_m = int(input('Min M: '))
max_m = int(input('Max M: '))

test_cases = int(input('Test case amount: '))
test_case_prefix = input('Test case file prefix: ')

n_values = uniform_random_list(min_n,max_n+1,test_cases)
m_values = uniform_random_list(min_m,max_m+1,test_cases)
for i in range(1,test_cases+1):
    with open(f'{test_case_prefix}.{i}.in', 'w+') as input_file, \
        open(f'{test_case_prefix}.{i}.out','w+') as output_file:

        n,m = n_values[i-1],m_values[i-1]
        input_file.write(f'{n} {m}\n')
        
        capacity = []
        for i in range(4):
            c = randint(0, floor(n / randint(1, 10)))
            capacity.append(c)

        capacity_str = ' '.join(str(i) for i in capacity)
        input_file.write(f'{capacity_str}\n')

        boxes = []
        for i in range(m):
            characters=[]
            for j in range(n):
                character = chr(ord('A') + randint(0, 3))
                characters.append(character)

            characters_str = ' '.join(characters)
            input_file.write(f'{characters_str}\n')
            boxes.append([ord(c) - ord('A') for c in characters])

        for student in range(n):
            tally_ho = {0: 0, 1: 0, 2: 0, 3: 0}
            for box in boxes:
                tally_ho[box[student]] += 1

            tally_ho = {k:v for (k,v) in tally_ho.items() if capacity[k] > 0}
            if len(tally_ho) == 0:
                output_file.write('E\n')
            else:
                house = max(tally_ho, key=lambda k: (tally_ho[k], -k))
                r = chr(house + ord("A"))
                output_file.write(f'{r}\n')
                capacity[house] -= 1
            