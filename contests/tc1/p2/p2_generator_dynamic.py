from __future__ import print_function
from sys import stderr, argv
from string import ascii_lowercase
from random import randint, random, choice, sample, seed as random_seed
input=raw_input

seed, min_n, max_n = map(int, argv[1:])
random_seed(seed)

n = randint(min_n, max_n)
c = randint(1, 10)
l = randint(1, 10)
print('{0} {1} {2}'.format(n,c,l))

def random_string(length):
    return ''.join([choice(ascii_lowercase) for i in xrange(length)])

wordset = [random_string(randint(1,10)) for i in range(max(1000, n))]
candidate_file_names = sample(wordset, k=c)
candidate_file_names_set = set(candidate_file_names)

print(' '.join(candidate_file_names))

wordset = list(set(wordset) - candidate_file_names_set)
for i in range(n):
    if random() <= 0.5:
        name = choice(candidate_file_names)
    else:
        name = choice(wordset)

    line_number = l * randint(1, 15)
    if random() <= 0.5:
        line_number += 1
    
    error = random_string(randint(1,5))
    print('{0} {1} {2}'.format(name, line_number, error))

    if name in candidate_file_names_set and line_number % l == 0:
        print('{0} {1} {2}'.format(name, line_number, error), file=stderr)
