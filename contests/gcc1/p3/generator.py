import os
from random import randint, random,choices
from zipfile import ZipFile
from string import ascii_lowercase

MAX_COORDINATE = 1000000000
def random_coordinate():
    return (randint(0,MAX_COORDINATE), randint(0,MAX_COORDINATE))

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

zip_name=f'{test_case_prefix}_data.zip'
if os.path.exists(zip_name):
    os.remove(zip_name)

with ZipFile(zip_name,'w') as data_zip:
    n_values = uniform_random_list(min_n,max_n+1,test_cases)

    for i in range(1,test_cases+1):
        n = n_values[i-1]
        coordinates=[random_coordinate() for i in range(n)]
        mean_coordinate = (round(sum(c[0] for c in coordinates)/n,2), round(sum(c[1] for c in coordinates)/n,2))

        in_file_name=f'{test_case_prefix}.{i}.in'
        out_file_name=f'{test_case_prefix}.{i}.out'

        data_zip.writestr(in_file_name,f'{n}\n'+'\n'.join(' '.join(str(i) for i in c) for c in coordinates))
        data_zip.writestr(out_file_name,' '.join(str(i) for i in mean_coordinate))