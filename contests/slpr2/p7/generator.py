import os
import random
import sys

class Graph(object):
    def __init__(self, nodes, edges=None, loops=False, multigraph=False,
                 digraph=False):
        self.nodes = nodes
        if edges:
            self.edges = edges
            self.edge_set = self._compute_edge_set()
        else:
            self.edges = []
            self.edge_set = set()
        self.loops = loops
        self.multigraph = multigraph
        self.digraph = digraph

    def add_edge(self, edge):
        """Add the edge if the graph type allows it."""
        if self.multigraph or edge not in self.edge_set:
            self.edges.append(edge)
            self.edge_set.add(edge)
            if not self.digraph:
                self.edge_set.add(edge[::-1])  # add other direction to set.
            return True
        return False

    def make_random_edge(self):
        """Generate a random edge between any two nodes in the graph."""
        if self.loops:
            # With replacement.
            random_edge = (random.choice(self.nodes), random.choice(self.nodes))
        else:
            # Without replacement.
            random_edge = tuple(random.sample(self.nodes, 2))
        return random_edge

    def add_random_edges(self, total_edges):
        """Add random edges until the number of desired edges is reached."""
        while len(self.edges) < total_edges:
            self.add_edge(self.make_random_edge())

def check_num_edges(nodes, num_edges, loops, multigraph, digraph):
    """Checks that the number of requested edges is acceptable."""
    num_nodes = len(nodes)
    # Check min edges
    min_edges = num_nodes - 1
    if num_edges < min_edges:
        raise ValueError('num_edges less than minimum (%i)' % min_edges)
    # Check max edges
    max_edges = num_nodes * (num_nodes - 1)
    if not digraph:
        max_edges /= 2
    if loops:
        max_edges += num_nodes
    if not multigraph and num_edges > max_edges:
            raise ValueError('num_edges greater than maximum (%i)' % max_edges)

def generate_connected_graph(nodes, num_edges, loops=False, multigraph=False, digraph=False):
    # Algorithm inspiration:
    # https://en.wikipedia.org/wiki/Uniform_spanning_tree#The_uniform_spanning_tree

    # Idea:
    # Create a uniform spanning tree (UST) using a random walk.
    # Add random edges until the number of desired edges is reached.

    check_num_edges(nodes, num_edges, loops, multigraph, digraph)

    # Create two partitions, S and T. Initially store all nodes in S.
    S, T = set(nodes), set()

    # Pick a random node, and mark it as visited and the current node.
    current_node = random.sample(S, 1).pop()
    S.remove(current_node)
    T.add(current_node)

    graph = Graph(nodes, loops=loops, multigraph=multigraph, digraph=digraph)

    # Create a random connected graph.
    while S:
        # Randomly pick the next node from the neighbors of the current node.
        # As we are generating a connected graph, we assume a complete graph.
        neighbor_node = random.sample(nodes, 1).pop()
        # If the new node hasn't been visited, add the edge from current to new.
        if neighbor_node not in T:
            edge = (current_node, neighbor_node)
            graph.add_edge(edge)
            S.remove(neighbor_node)
            T.add(neighbor_node)
        # Set the new node as the current node.
        current_node = neighbor_node

    # Add random edges until the number of desired edges is reached.
    graph.add_random_edges(num_edges)
    return graph

def uniform_random_list(a, b, n):
    x = a
    result = []
    for i in range(n, 0, -1):
        x += (b-x) * (1-pow(random.random(), 1. / i))
        result.append(int(x))

    return result

def display_progress_bar(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush()

min_nm = int(input('Min N (and M): '))
max_nm = int(input('Max N (and M): '))
min_q = int(input('Min Q: '))
max_q = int(input('Max Q: '))
test_cases = int(input('Test case amount: '))
test_case_prefix = input('Test case file prefix: ')

n_values = uniform_random_list(min_nm,max_nm+1,test_cases)
q_values = uniform_random_list(min_q,max_q+1,test_cases)
for i in range(1,test_cases+1):
    with open(f'{test_case_prefix}.{i}.in','w+') as input_file:
        print(f'Generating test case {test_case_prefix}.{i}')

        n = n_values[i-1]
        queries = q_values[i-1]
        m = random.randint(n-1, min(n*(n-1)/2,max_nm))      
        graph = generate_connected_graph(list(range(1,n+1)),m)
        edges=[]

        print('Generating graph...')
        for e in graph.edges:
            p,q = e
            c = random.randint(1,100)
            edges.append((p,q,c))

            display_progress_bar(len(edges), len(graph.edges))
        
        print()

        input_file.write(f'{n} {m} {queries}\n'+'\n'.join(' '.join(str(j) for j in e) for e in edges)+'\n')

        print(f'Generating queries...')
        for i in range(queries):
            a=random.randint(1,n)
            b=random.randint(1,n)
            if a==b:
                if a > 1:
                    a-=1
                else:
                    a+=1
                
            input_file.write(f'{a} {b}\n')
            display_progress_bar(i+1, queries, f'{i+1} / {queries}')

        print()

        # solution = solve(n,m,edges)

        # output_file.write(f'{solution}\n')