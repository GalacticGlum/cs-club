import os
from random import randint, random,choices
from zipfile import ZipFile
from string import ascii_lowercase

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
        dictionary = [''.join(choices(ascii_lowercase,k=randint(1,15))) for i in range(n)]
        
        in_file_name=f'{test_case_prefix}.{i}.in'
        out_file_name=f'{test_case_prefix}.{i}.out'

        data_zip.writestr(in_file_name,f'{n}\n'+' '.join(dictionary))
        data_zip.writestr(out_file_name,str(sum(word.count('a') for word in dictionary)))