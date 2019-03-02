from random import randint, random, choice, choices, sample
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
        
        capacity = [randint(0, n) for i in range(4)]
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

        for i in range(n):
            freq=[0]*4
            for j in range(m):
                freq[boxes[j][i]] += 1
                
            max_index=0
            for j in range(4):
                if freq[j]>freq[max_index] and capacity[j] > 0 or freq[j]>=freq[max_index] and capacity[max_index]==0 and capacity[j]>0:
                    max_index=j

            capacity[max_index]-=1
            if capacity[max_index]<0:
                output_file.write('E\n')
            else:
                answer = chr(ord('A') + max_index)
                output_file.write(f'{answer}\n')
            