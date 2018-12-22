from random import randint, random, choice, choices, sample
from string import ascii_lowercase

MAX_WORD_LENGTH = 10

def permute_string(string):
    half_len = len(string)//2
    # 20% chance to add or remove characters
    if random() < 0.2:
        c = randint(-half_len, half_len+1)
        # remove characters
        if c < 0:
            for _ in range(abs(c)):
                i = randint(0,len(string)-1)
                string = string[:i] + string[i+1:]
        # add characters
        elif c > 0:
            for _ in range(c):
                to_add = choice(ascii_lowercase)
                i = randint(0,len(string)-1)
                string = string[:i] + to_add + string[i:]
    else:
        # shuffle n characters
        k = sample(range(len(string)),randint(0,len(string)-1))
        word = list(string)
        for i in k:
            word[i] = choice(ascii_lowercase)

        string = ''.join(word)
    return string

def min3(x, y, z): return min(min(x,y),z)

def min_edit_distance(a, b):
    m, n = len(a), len(b)
    cache = [[0 for j in range(n+1)] for i in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                cache[i][j] = j
            elif j == 0:
                cache[i][j] = i
            elif a[i-1] == b[j-1]:
                cache[i][j] = cache[i-1][j-1]
            else:
                cache[i][j] = 1 + \
                    min3(cache[i][j-1], cache[i-1][j], cache[i-1][j-1])

    return cache[m][n]

def solve(dictionary, message):
    n,m = len(dictionary), len(message)
    result = []

    for i in range(m):
        encrypted_word = message[i]
        min_distance = float('inf')
        
        for j in range(n):
            dict_word = dictionary[j]
            distance = min_edit_distance(encrypted_word, dict_word)
            if distance < min_distance:
                min_distance = distance
                decrypted_word = dict_word

        result.append(decrypted_word)

    return result

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
max_m = int(input('Min M: '))

test_cases = int(input('Test case amount: '))
test_case_prefix = input('Test case file prefix: ')

n_values = uniform_random_list(min_n,max_n+1,test_cases)
m_values = uniform_random_list(min_m,max_m+1,test_cases)
for i in range(1,test_cases+1):
    with open(f'{test_case_prefix}.{i}.in', 'w+') as input_file, \
        open(f'{test_case_prefix}.{i}.out','w+') as output_file:

        n,m = n_values[i-1], m_values[i-1]
        dictionary = [''.join(choices(ascii_lowercase,k=randint(1,MAX_WORD_LENGTH))) for i in range(n)]
        message = [permute_string(choice(dictionary)) for i in range(m)]

        dictionary_str = ' '.join(dictionary)
        message_str = ' '.join(message)
        solution_str = ' '.join(solve(dictionary, message))

        input_file.write(f'{n} {m}\n{dictionary_str}\n{message_str}')
        output_file.write(f'{solution_str}\n')        
            