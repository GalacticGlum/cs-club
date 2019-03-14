import os
import random

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

def solve(n, m, edges):
    class MSTGraph: 
        def __init__(self, vertices): 
            self.V = vertices
            self.graph = []  
    
        def add_edge(self, u, v, w): 
            self.graph.append([u,v,w]) 
    
        def find(self, parent, i): 
            if parent[i] == i: return i 
            return self.find(parent, parent[i]) 
    
        def union(self, parent, rank, x, y): 
            xroot = self.find(parent, x) 
            yroot = self.find(parent, y) 

            if rank[xroot] < rank[yroot]: 
                parent[xroot] = yroot 
            elif rank[xroot] > rank[yroot]: 
                parent[yroot] = xroot 
            else : 
                parent[yroot] = xroot 
                rank[xroot] += 1
    
        def find_mst(self): 
            result =[] 
    
            i = 0 
            e = 0 

            self.graph =  sorted(self.graph,key=lambda item: item[2]) 
    
            parent = []
            rank = [] 
    
            for node in range(self.V): 
                parent.append(node) 
                rank.append(0) 
        
            while e < self.V - 1:  
                u,v,w =  self.graph[i] 
                i += 1
                x = self.find(parent, u) 
                y = self.find(parent, v) 

                if x != y: 
                    e += 1    
                    result.append([u,v,w]) 
                    self.union(parent, rank, x, y)             
    
            return result

    mst_graph = MSTGraph(n)
    for e in edges:
        p,q,c = e
        mst_graph.add_edge(p-1,q-1,c)
    
    tree = mst_graph.find_mst()
    total_weight = 0
    for e in tree:
        total_weight+=e[2]
    return total_weight

def uniform_random_list(a, b, n):
    x = a
    result = []
    for i in range(n, 0, -1):
        x += (b-x) * (1-pow(random.random(), 1. / i))
        result.append(int(x))

    return result

min_nm = int(input('Min N (and M): '))
max_nm = int(input('Max N (and M): '))
test_cases = int(input('Test case amount: '))
test_case_prefix = input('Test case file prefix: ')

n_values = uniform_random_list(min_nm,max_nm+1,test_cases)
for i in range(1,test_cases+1):
    with open(f'{test_case_prefix}.{i}.in','w+') as input_file, open(f'{test_case_prefix}.{i}.out', 'w+') as output_file:
        n = n_values[i-1]
        m = random.randint(n-1, min(n*(n-1)/2,max_nm))
        graph = generate_connected_graph(list(range(1,n+1)),m)
        edges=[]
        for e in graph.edges:
            p,q = e
            c = random.randint(1,15)
            edges.append((p,q,c))

        solution = solve(n,m,edges)

        input_file.write(f'{n} {m}\n'+'\n'.join(' '.join(str(j) for j in e) for e in edges))
        output_file.write(f'{solution}\n')