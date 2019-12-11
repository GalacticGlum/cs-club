from random import randint, random, sample
from collections import deque
from time import time
import sympy

max_q = int(input('Max Q: '))

test_cases = int(input('Test case amount: '))
test_case_prefix = input('Test case file prefix: ')

class Vector3(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    @classmethod
    def dot(cls, u, v):
        return u.x * v.x + u.y * v.y + u.z * v.z

    @classmethod
    def cross(cls, u, v):
        return cls(u.y * v.z - u.z * v.y,
                   u.z * v.x - u.x * v.z,
                   u.x * v.y - u.y * v.x)

    @classmethod
    def random(cls):
        return cls(randint(-1000000, 1000000), randint(-1000000, 1000000), randint(-1000000, 1000000))    

    @classmethod
    def difference(cls, u, v):
        return Vector3(u.x - v.x, u.y - v.y, u.z - v.z)

    def __str__(self):
        return '({}, {}, {})'.format(self.x, self.y, self.z)

    def __repr__(self): return self.__str__()

unit_slopes = set()

def generate_road():
    while True:
        a, b = Vector3.random(), Vector3.random()
        m = Vector3.difference(a, b)
        magnitude = sympy.simplify(sympy.sqrt(sympy.Pow(m.x, 2) + sympy.Pow(m.y, 2) + sympy.Pow(m.z, 2)))
        m_hat = (m.x / magnitude, m.y / magnitude, m.z / magnitude)

        has_finished = m_hat not in unit_slopes
        unit_slopes.add(m_hat)

        if has_finished:
            return a, b, m

for i in range(1,test_cases+1):
    with open(f'{test_case_prefix}.{i}.in', 'w+') as input_file, \
        open(f'{test_case_prefix}.{i}.out','w+') as output_file:

        n = randint(1, 1000)
        q = randint(1, max_q)
        print(f'Generating test case {i} (n={n}, q={q})...')
        input_file.write('{} {}\n'.format(n, q))
        start_time = time()

        roads = []
        perpendicular_roads = {}
        invalid_roads = {}

        i = 0
        while i < n:
            a1, b1, m1 = generate_road()

            roads.append((a1, b1, m1))
            input_file.write('{} {} {} {} {} {}\n'.format(a1.x, a1.y, a1.z, b1.x, b1.y, b1.z))

            if i < n -1:
                # 30% chance for the lines to be perpendicular...
                if random() <= 0.3:
                    c = Vector3.random()
                    # n is the vector normal to AB
                    normal = Vector3.cross(m1, c)
                    
                    t = (lambda x: 1 if x == 0 else x)(randint(-100, 100))
                    a2 = Vector3(a1.x + m1.x * t, a1.y + m1.y * t, a1.z + m1.z * t)

                    s = (lambda x: 1 if x == 0 else x)(randint(-100, 100))
                    b2 = Vector3(a2.x + normal.x * s, a2.y + normal.y * s, a2.z + normal.z * s)

                    m2 = Vector3.difference(a2, b2)
                    roads.append((a2, b2, m2))
                    input_file.write('{} {} {} {} {} {}\n'.format(a2.x, a2.y, a2.z, b2.x, b2.y, b2.z))
                    
                    if m1 not in perpendicular_roads:
                        perpendicular_roads[m1] = []

                    perpendicular_roads[m1].append(len(roads) - 1)

                    if m2 not in perpendicular_roads:
                        perpendicular_roads[m2] = []
                    
                    perpendicular_roads[m2].append(len(roads) - 2)          
                    i += 1
                # 30% chance for the lines to intersect in any way
                elif 0.3 < random() <= 0.6:
                    t = (lambda x: 1 if x == 0 else x)(randint(-100, 100))
                    a2 = Vector3(a1.x + m1.x * t, a1.y + m1.y * t, a1.z + m1.z * t)
                    b2 = Vector3.random()

                    m2 = Vector3.difference(a2, b2)
                    roads.append((a2, b2, m2))
                    input_file.write('{} {} {} {} {} {}\n'.format(a2.x, a2.y, a2.z, b2.x, b2.y, b2.z))

                    if i not in invalid_roads:
                        invalid_roads[i] = []

                    invalid_roads[i].append(i + 1)

                    if (i + 1) not in invalid_roads:
                        invalid_roads[i + 1] = []

                    invalid_roads[i + 1].append(i)
                    i += 1

            i += 1

        index_choices = set(range(len(roads)))
        for _ in range(q):
            i, = sample(index_choices, 1)
            a1, b1, m1 = roads[i]

            if random() <= 0.60 and i in invalid_roads:
                j, = sample(invalid_roads[i], 1)
            elif 0.60 < random() <= 0.80 and m1 in perpendicular_roads:
                j, = sample(perpendicular_roads[m1], 1)
            else:
                j, = sample(index_choices - {i}, 1)

            input_file.write('{} {}\n'.format(i + 1, j + 1))    
            a2, b2, m2 = roads[j]

            if m1.x == m2.x and m1.y == m2.y and m1.z == m2.z:
                output_file.write('none\n')
            elif Vector3.dot(Vector3.cross(m1, m2), Vector3.difference(a1, a2)) != 0:
                output_file.write('none\n')
            else:
                d = Vector3.dot(m1, m2)
                output_file.write(('valid' if d == 0 else 'invalid') + '\n')

        print(f'-> Completed generating data... ({round(time() - start_time, 3)} seconds elapsed)')