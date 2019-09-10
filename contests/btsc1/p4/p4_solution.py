r = input()
s = input()

while s.count(r):
    s = s.replace(r, '')

print('true' if not s else 'false')
