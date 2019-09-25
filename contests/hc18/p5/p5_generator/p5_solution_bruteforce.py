from queue import Queue
MAXN = 100000

edges = {}

n, m = map(int,input().split())
for i in range(n-1):
    u,v = map(int,input().split())
    u-=1
    v-=1
    if u not in edges:
        edges[u] = set()

    if v not in edges:
        edges[v] = set()

    edges[u].add(v)
    edges[v].add(u)

def bfs(u):
    distances = [-1]*n
    queue = Queue()
    queue.put(u)
    distances[u] = 0

    while not queue.empty():
        node = queue.get()
        for v in edges[node]:
            if distances[v] == -1:
                queue.put(v)
                distances[v] = distances[node]+1

    max_distance = 0
    max_distance_node = 0
    for i in range(n):
        if distances[i] > max_distance:
            max_distance = distances[i]
            max_distance_node = i

    return (max_distance_node, max_distance)

for i in range(m):
    x,y = map(int,input().split())
    total_distance = 0

    current_city = (x-1)
    for j in range(y):
        r = bfs(current_city)
        total_distance += r[1]
        current_city = r[0]

    print(total_distance)