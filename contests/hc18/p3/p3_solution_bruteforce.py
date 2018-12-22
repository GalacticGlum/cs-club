def min3(x, y, z): return min(min(x, y), z)

def min_edit_distance(a, b, m=-1, n=-1):
    if m == -1:
        m = len(a)

    if n == -1:
        n = len(b)

    if m == 0: return n
    if n == 0: return m
    if a[m-1] == b[n-1]: return min_edit_distance(a, b, m-1, n-1)
    return 1 + min3(min_edit_distance(a,b,m,n-1),min_edit_distance(a,b,m-1,n),
        min_edit_distance(a,b,m-1,n-1))

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