from numpy.random import randint
from random import random

# constants
MAX_N=1000

test_cases = int(input('Test case amount: '))
test_case_prefix = input('Test case file prefix: ')
n_values = sorted([randint(low=1,high=MAX_N+1) for i in range(test_cases)])
for i in range(1,test_cases+1):
    with open(f'{test_case_prefix}.{i}.in', 'w+') as input_file, \
        open(f'{test_case_prefix}.{i}.out','w+') as output_file:

        purchases=[randint(low=1,high=1001) for j in range(n_values[i-1])]
        state_percent=random()
        account_balance = sum(purchases)

        if 0 <= state_percent <= (1/3):
            account_balance -= randint(low=1,high=1000)
            state='Deficit'
        elif (1/3) < state_percent <= (2/3):
            state='Zero'
        else:
            account_balance += randint(low=1,high=1000)
            state='Surplus'

        input_file.write(f'{account_balance}\n{n_values[i-1]}\n')
        purchases_str = ' '.join(str(i) for i in purchases)
        input_file.write(f'{purchases_str}')

        output_file.write(f'{state}\n{account_balance-sum(purchases)}')