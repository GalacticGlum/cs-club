time_available = int(input())
s = int(input())
sacrifices = sorted([int(input()) for i in range(s)])

time_taken = 0
for i in range(s):
    time_taken += sacrifices[i]
    if time_taken > time_available:
        print(i)
        break
