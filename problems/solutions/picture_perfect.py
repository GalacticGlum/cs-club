n = int(input())

words = []
longest_length = 0

for i in range(n):
    word = input()
    word_length = len(word)

    if word_length > longest_length:
        longest_length = word_length

    words.append(word)

border = '*' * (longest_length + 4) 
print(border)
for word in words:
    print('* ' + word  + ' ' * (longest_length - len(word)) + ' *')

print(border)

