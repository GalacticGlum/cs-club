n, m = map(int, input().split())
greetings = set(input().strip() for i in range(m))

def read_phrase(line):
    pid, phrase = line.split(':')
    return int(pid), phrase.strip()

phrases=[input() for i in range(n)]
used_greetings = set()
i=0
while i < n:
    pid_a, phrase_a = read_phrase(phrases[i])
    if phrase_a in greetings:
        used_greetings.add(phrase_a)
    elif i < n - 1:
        pid_b, phrase_b = read_phrase(phrases[i+1])
        if pid_a != pid_b:
            if phrase_b in greetings:
                used_greetings.add(phrase_b)            
                used_greetings.add(phrase_a)
                greetings.add(phrase_a)

    i += 1

print(len(used_greetings))