from random import randint, random, choice, sample

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

min_m = int(input('Min M: '))
max_m = int(input('Max M: '))
test_cases = int(input('Test case amount: '))
test_case_prefix = input('Test case file prefix: ')

for i in range(1,test_cases+1):
    with open(f'{test_case_prefix}.{i}.in', 'w+') as input_file, \
        open(f'{test_case_prefix}.{i}.out','w+') as output_file:

        m = randint(min_m, max_m)
        input_file.write(f'{m}\n')
        
        root = Node(randint(0, 1000000))
        connections = {root.value: root}

        edge_count = 0
        previous_node = None
        available_values = set(range(0, 100))

        while edge_count < m:
            if random() <= 0.5 and previous_node is not None:
                a = previous_node.value
            else:
                a = choice(list(connections.keys()))

            t = choice(['L' if connections[a].left is None else '', 'R' if connections[a].right is None else ''])
            if t == '': continue

            previous_node = Node(sample(available_values, 1)[0])
            available_values.remove(previous_node.value)

            if t == 'L':
                connections[a].left = previous_node
            else:
                connections[a].right = previous_node

            connections[previous_node.value] = previous_node

            input_file.write(f'{a} {previous_node.value} {t}\n')
            edge_count += 1

        def inorder(node, current=list()):
            if node is None: return current

            inorder(node.left, current)
            current.append(node.value)
            inorder(node.right, current)

            return current

        def preorder(node, current=list()):
            if node is None: return current

            current.append(node.value)
            preorder(node.left, current)
            preorder(node.right, current)

            return current

        def postorder(node, current=list()):
            if node is None: return current

            postorder(node.left, current)
            postorder(node.right, current)
            current.append(node.value)

            return current

        output_file.write(' '.join(str(i) for i in preorder(root)) + '\n')        
        output_file.write(' '.join(str(i) for i in inorder(root)) + '\n')        
        output_file.write(' '.join(str(i) for i in postorder(root)))        
    


