from random import randint, random

def solve(n, k):
    def is_digit_in_number(number, digit):
        current_digit = 0
        while number != 0:
            current_digit = number % 10
            number //= 10

            if current_digit == digit:
                return True

        return False

    prime = [True]*(n+1)
    p = 2
    while p*p <= n:
        if prime[p]:
            for i in range(p*p,n+1,p):
                prime[i]=False
        p += 1

    prime_sum = 0
    for i in range(2,n+1):
        if prime[i] and is_digit_in_number(i,k):
            prime_sum += i

    return prime_sum

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
        k = randint(0,9)
        input_file.write(f'{n} {k}\n')
        
        solution = solve(n, k)
        output_file.write(f'{solution}\n')

        

