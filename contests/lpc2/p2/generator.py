from networkx.generators.random_graphs import erdos_renyi_graph
from random import randint, random
from time import time

min_n = int(input('Min N: '))
max_n = int(input('Max N: '))

test_cases = int(input('Test case amount: '))
test_case_prefix = input('Test case file prefix: ')

for i in range(1,test_cases+1):
    with open(f'{test_case_prefix}.{i}.in', 'w+') as input_file, \
        open(f'{test_case_prefix}.{i}.out','w+') as output_file:

        n = randint(min_n, max_n)
        print(f'Generating test case {i} (n={n})...')
        start_time = time()
        graph = erdos_renyi_graph(n, random() / 2)
        nodes = [randint(-4, 5) for _ in range(n)]

        # guaranteed to create a winnable configuration 35% of the time
        if random() <= 0.35:
            genus = len(graph.edges) - n + 1
            node_sum = sum(nodes)
            if node_sum < genus:
                nodes[randint(0, n - 1)] += genus - node_sum + randint(1, 10)
            
            node_sum = sum(nodes)
            if node_sum < 0:
                nodes[randint(0, n - 1)] += node_sum + randint(1, 10)
      
        print(f'-> Completed generating input data... ({round(time() - start_time, 3)} seconds elapsed)')

        result = sum(nodes) >= len(graph.edges) - n + 1

        print('-> Writing to file...')

        input_file.write('{} {}\n{}\n'.format(n, len(graph.edges), ' '.join(str(value) for value in nodes)))
        for edge in graph.edges:
            input_file.write('{} {}\n'.format(edge[0] + 1, edge[1] + 1))
        
        output_file.write(['false', 'true'][result])