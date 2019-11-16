from random import randint
from itertools import accumulate

test_cases = int(input('Test case amount: '))
test_case_prefix = input('Test case file prefix: ')

for i in range(1,test_cases+1):
    with open(f'{test_case_prefix}.{i}.in', 'w+') as input_file, \
        open(f'{test_case_prefix}.{i}.out','w+') as output_file:
    
        n,q = randint(1,10000), randint(1,1000000)
        input_file.write(f'{n} {q}\n')
        
        values = []
        psa = [0]
        for i in range(n):
            value = randint(0, 100)
            values.append(value)
            psa.append(psa[i]+value)
            input_file.write(f'{value} ')

        input_file.write('\n')
        for qi in range(q):
            k = randint(0,100)
            r = randint(2, n)
            l = randint(1, r - 1)

            input_file.write(f'{k} {l} {r}\n')  
            result = psa[r] - psa[l-1] - (r-l+1)*k
            output_file.write(f'{result}\n')