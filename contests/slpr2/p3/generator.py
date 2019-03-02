from random import randint, random, choice, choices, sample
from string import ascii_lowercase

def uniform_random_list(a, b, n):
    x = a
    result = []
    for i in range(n, 0, -1):
        x += (b-x) * (1-pow(random(), 1. / i))
        result.append(int(x))

    return result

def solve(word):
    word=[c for c in word]
    for i in range(0,n-1,2):
        if n%2!=0 and i==n-2: continue
        word[i],word[i+1]=word[i+1],word[i]
        
    return ''.join(chr(ord('a') + (ord('z')-ord(c))) for c in word)

min_t = int(input('Min T: '))
max_t = int(input('Max T: '))

test_cases = int(input('Test case amount: '))
test_case_prefix = input('Test case file prefix: ')

t_values = uniform_random_list(min_t,max_t+1,test_cases)
for i in range(1,test_cases+1):
    with open(f'{test_case_prefix}.{i}.in', 'w+') as input_file, \
        open(f'{test_case_prefix}.{i}.out','w+') as output_file:

        t = t_values[i-1]
        input_file.write(f'{t}\n')

        messages = [''.join(choices(ascii_lowercase,k=randint(1,100))) for i in range(t)]
        for j in range(t):
            n=len(messages[j])
            input_file.write(f'{n} {messages[j]}\n')
            output_file.write(f'{solve(messages[j])}\n')