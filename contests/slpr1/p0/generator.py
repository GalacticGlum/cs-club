from numpy.random import randint

# constants
MIN_A = -10
MAX_A = 10
MAX_B = 10
MAX_TESTS = 10000

test_cases = int(input('Test case amount: '))
test_case_prefix = input('Test case file prefix: ')
t_values = sorted([randint(low=1,high=MAX_TESTS+1) for i in range(test_cases)])
for i in range(1,test_cases+1):
    with open(f'{test_case_prefix}.{i}.in', 'w+') as input_file, \
        open(f'{test_case_prefix}.{i}.out','w+') as output_file:

        input_file.write(f'{t_values[i-1]}\n')
        for j in range(t_values[i-1]):
            a = randint(low=MIN_A,high=MAX_A+1)
            b = randint(low=1,high=MAX_B)
            input_file.write(f'{a} {b}\n')
            output_file.write(f'{a**b}\n')