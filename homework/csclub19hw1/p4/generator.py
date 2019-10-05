from random import randint, random, choice
from string import ascii_uppercase

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
        k = randint(1, 100)
        input_file.write(f'{n} {k}\n')

        tasks = [choice(ascii_uppercase) for _ in range(n)]
        tasks_str = ' '.join(i for i in tasks)
        input_file.write(f'{tasks_str}\n')

        freq = [0]*26
        for task in tasks:
            freq[ord(task) - ord('A')] += 1
            
        freq.sort(reverse=True)
        gaps = k * (freq[0] - 1) 
        total = freq[0] + gaps
        for i in range(1, 26):
            if freq[i] == 0: break
            if gaps >= freq[i]:
                if freq[i] == freq[0]:
                    total += 1
                    gaps -= 1
            
                gaps -= freq[i]
            else:
                total = n
                break
        
        output_file.write(f'{total}\n')

        