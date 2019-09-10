from random import randint, random, sample
from uuid import uuid4

test_cases = int(input('Test case amount: '))
test_case_prefix = input('Test case file prefix: ')

for i in range(1,test_cases+1):
    with open(f'{test_case_prefix}.{i}.in', 'w+') as input_file, \
        open(f'{test_case_prefix}.{i}.out','w+') as output_file:

        n = randint(1, 100)
        if n % 2 != 0:
            n += 1
        
        m = randint(1, 100)

        greetings = {uuid4().hex[:6].upper() for i in range(m)}
        input_file.write(f'{n} {m}\n')
        for phrase in greetings:
            input_file.write(f'{phrase}\n')

        count = 0
        used_greetings = set()
        for i in range(n//2):
            person_id = randint(1, n)
            pa = uuid4().hex[:6].upper()
            
            # 50% chance that the phrase is a NEW greeting
            if random() <= 0.5:
                pb = sample(greetings, 1)[0]
                used_greetings.add(pb)

                # 5% chance that the phrase is a NEW greeting but it is said by the same person
                person_id_2 = person_id + (0 if random() <= 0.05 else 1)
                
                if person_id_2 != person_id:
                    greetings.add(pa)
                    used_greetings.add(pa)
            else:
                pb = uuid4().hex[:6].upper()
                person_id_2 = randint(1, n)

            input_file.write(f'{person_id}:{pa}\n{person_id_2}:{pb}\n')
        
        output_file.write(f'{len(used_greetings)}\n')