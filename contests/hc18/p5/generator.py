from random import sample, random, randint, choice

def uniform_random_list(a, b, n):
    x = a
    result = []
    for i in range(n, 0, -1):
        x += (b-x) * (1-pow(random(), 1. / i))
        result.append(int(x))

    return result

def rand_tree(n):
    tree = [[-1,-1]]
    free_edges = [(0,0),(0,1)]

    while len(tree) < n:
        e = choice(free_edges)
        node, child = e
        k = len(tree)
        tree.append([-1,-1])
        tree[node][child]=k
        free_edges.extend([(k,0),(k,1)])
        free_edges.remove(e)

    return tree

print(rand_tree(4))

# min_n = int(input('Min N: '))
# max_n = int(input('Max N: '))
# min_m = int(input('Min M: '))
# max_m = int(input('Max M: '))
# min_k = int(input("Min K: "))
# max_k = int(input("Max K: "))

# test_cases = int(input('Test case amount: '))
# test_case_prefix = input('Test case file prefix: ')

# n_values = uniform_random_list(min_n,max_n+1,test_cases)
# m_values = uniform_random_list(min_m,max_m+1,test_cases)
# for i in range(1,test_cases+1):
#     with open(f'{test_case_prefix}.{i}.in', 'w+') as input_file, \
#         open(f'{test_case_prefix}.{i}.out','w+') as output_file:

#         n, m = n_values[i-1], m_values[i-1]
#         input_file.write(f'{n} {m}\n')
