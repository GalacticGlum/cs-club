def min3(x, y, z): return min(min(x, y), z)

def min_edit_distance(a, b):
    m, n = len(a), len(b)
    cache = [[0 for j in range(n+1)] for i in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0:
                cache[i][j] = j
            elif j == 0:
                cache[i][j] = i
            elif a[i-1] == b[j-1]:
                cache[i][j] = cache[i-1][j-1]
            else:
                cache[i][j] = 1 + \
                    min3(cache[i][j-1], cache[i-1][j], cache[i-1][j-1])

    return cache[m][n]

n, m = map(int,input().split())
dictionary = input().split()
message = input().split()

for i in range(m):
    encrypted_word = message[i]
    min_distance = float('inf')
    for j in range(n):
        dict_word = dictionary[j]
        distance = min_edit_distance(encrypted_word, dict_word)
        if distance < min_distance:
            min_distance = distance
            decrypted_word = dict_word

    print(decrypted_word, end='')
    if i < m:
        print(' ', end='')