from random import randint, random, choice, choices
from string import ascii_lowercase
from math import floor

PARANTHESES_SET = [('(',')'),('[',']'),('{','}')]

def generate_phrase(length, is_balanced, nesting_factor=0.5):
    if length == 0 or length == 1:
        return choice(choice(PARANTHESES_SET)) if not is_balanced else choice(ascii_lowercase)
    
    inv_nesting_factor = 1 - nesting_factor
    inner = str()
    if length > 3 and inv_nesting_factor > 0:
        max_length = floor((length - 3) * inv_nesting_factor)
        if max_length > 0:
            inner_length = randint(1, max_length)
            if length % 2 != inner_length % 2:
                inner_length -= 1
                    
            inner = ''.join(choices(ascii_lowercase, k=inner_length))
        
    inner += generate_phrase(length - len(inner) - 2, is_balanced)
    
    paranthesis_pair = choice(PARANTHESES_SET)
    return paranthesis_pair[0] + inner + paranthesis_pair[1]
    
def generate_testcase(length, is_balanced):
    if is_balanced and random() <= 0.20:
        return ''.join(choices(ascii_lowercase, k=length))

    return generate_phrase(length-1, is_balanced)

def check_balanced(expr):
    if expr.count('(') == expr.count(')') == expr.count('[') == expr.count(']') == expr.count('{') == expr.count('}') == 0: return True

    stack=[]
    for c in expr:
        if c == '(' or c == '[' or c == '{':
            stack.append(c)
            continue
        
        if len(stack) == 0: return False
        if c == ')':
            c = stack.pop()
            if c == '{' or c == '[': return False
        elif c == '}':
            c = stack.pop()
            if c == '(' or c == '[': return False
        elif c == ']':
            c = stack.pop()
            if c =='(' or c == '{': return False
    return len(stack)==0

def display_progress_bar(count, total, status=''):
    from sys import stdout

    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    stdout.flush()

def uniform_random_list(a, b, n):
    x = a
    result = []
    for i in range(n, 0, -1):
        x += (b-x) * (1-pow(random(), 1. / i))
        result.append(int(x))

    return result

min_n = int(input('Min N: '))
max_n = int(input('Max N: '))
min_w = int(input('Min W: '))
max_w = int(input('Max W: '))
test_cases = int(input('Test case amount: '))
test_case_prefix = input('Test case file prefix: ')
n_values = uniform_random_list(min_n,max_n+1,test_cases)

for i in range(1,test_cases+1):
    with open(f'{test_case_prefix}.{i}.in', 'w+') as input_file, \
        open(f'{test_case_prefix}.{i}.out','w+') as output_file:
        
        n = n_values[i-1]
        w_values = uniform_random_list(min_w, max_w+1, n)

        input_file.write(f'{n}\n')
        for j in range(n):
            w = w_values[j]

            is_balanced = random() >= 0.4
            phrase = generate_testcase(w, is_balanced)
            input_file.write(f'{phrase}\n')
            
            result = 'yes' if check_balanced(phrase) else 'no'
            output_file.write(f'{result}\n')

            display_progress_bar(j, n, f'Generating Testcase {i}')