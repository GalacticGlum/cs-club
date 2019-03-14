from random import randint, random

test_cases = int(input('Test case amount: '))
test_case_prefix = input('Test case file prefix: ')

for i in range(1,test_cases+1):
    with open(f'{test_case_prefix}.{i}.in', 'w+') as input_file, \
        open(f'{test_case_prefix}.{i}.out','w+') as output_file:

        message = []
        while len(' '.join(message)) <= 1000:
            if random() <= 0.3:
                message.append('dungeons and dragons')
            else:
                message.append('a'* randint(1, 30))

        message = ' '.join(message)
        input_file.write(f'{message}\n')

        s = round(3 * message.count('dungeons and dragons') / len(message.split(' ')), 2)
        output_file.write(f'{s}\n')
