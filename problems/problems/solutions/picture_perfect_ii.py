n = int(input())
words = [input() for i in range(n)]

length = len(max(words, key=len))
border = (length + 4) * '*'

print(border)
for word in words:
    print('* ' + word + (length - len(word)) * ' '+ ' *')

print(border)