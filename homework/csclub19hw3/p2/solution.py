class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

for ti in range(1, 11):
    with open(f'p1.{ti}.in', 'r') as input_file, open(f'p1.{ti}.out', 'w+') as out_file:
        m = int(input_file.readline())
        connections = {}
        root = None
        for _ in range(m):
            a, b, t = map(lambda v: int(v) if v != 'R' and v != 'L' else v, input_file.readline().split())
            if a not in connections:
                connections[a] = Node(a)
            
            if root is None:
                root = connections[a]

            new_node = Node(b)
            if t == 'L':
                connections[a].left = new_node
            else:
                connections[a].right = new_node

            connections[b] = new_node
        
        # calculate height
        def height(node):
            if node is None: return 0
            left = height(node.left)
            right = height(node.right)
            if left > right: return left + 1
            return right + 1
        
        out_file.write(str(height(root)) + '\n')
