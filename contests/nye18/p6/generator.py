from random import randint, random

def solve(n,m,k,tracks):
    grid_points = 0
    mapper = {}
    for _ in range(k):
        r, c1, c2 = tracks[_]
        if r in mapper:
            mapper[r].append((c1, c2))
        else:
            mapper[r] = [(c1, c2)]
    for k in mapper:
        temp = mapper[k]
        temp.sort()
        begin = temp[0][0]
        end = temp[0][1]
        points = 0
        for i in range(1, len(temp)):
            if temp[i][0] > end:
                points += end - begin + 1
                begin = temp[i][0]
                end = temp[i][1]
            else:
                end = max(end, temp[i][1])
        points += end - begin + 1
        grid_points += points
    return m*n - grid_points  

def uniform_random_list(a, b, n):
    x = a
    result = []
    for i in range(n, 0, -1):
        x += (b-x) * (1-pow(random(), 1. / i))
        result.append(int(x))

    return result

min_n = int(input('Min N: '))
max_n = int(input('Max N: '))
min_k = int(input('Min K: '))
max_k = int(input('Max K: '))
test_cases = int(input('Test case amount: '))
test_case_prefix = input('Test case file prefix: ')

n_values = uniform_random_list(min_n,max_n+1,test_cases)
m_values = uniform_random_list(min_n,max_n+1,test_cases)
k_values = uniform_random_list(min_k,max_k+1,test_cases)

for i in range(1,test_cases+1):
    with open(f'{test_case_prefix}.{i}.in', 'w+') as input_file, \
        open(f'{test_case_prefix}.{i}.out','w+') as output_file:

        n,m,k = n_values[i-1], m_values[i-1], k_values[i-1]
        input_file.write(f'{n} {m} {k}\n')
        tracks = []
        for i in range(k):
            r = randint(1,n)
            b = randint(1,m)
            a = randint(1,b)

            input_file.write(f'{r} {a} {b}\n')
            tracks.append((r,a,b))

        solution = solve(n,m,k,tracks)
        output_file.write(f'{solution}\n')

        
