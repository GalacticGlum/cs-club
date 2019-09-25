from random import randint

test_cases = int(input('Test case amount: '))
test_case_prefix = input('Test case file prefix: ')
for i in range(1,test_cases+1):
    with open(f'{test_case_prefix}.{i}.in', 'w+') as input_file, \
        open(f'{test_case_prefix}.{i}.out','w+') as output_file:

        k = randint(1,50)
        n = randint(1,50)
        r = randint(1,100)
        input_file.write(f'{k} {n}\n{r}')

        fv = k*((1+r/100)**n-1)/(r/100)
        output_file.write(str(round(fv,2)))