rounds = int(input())
player_a_points = 100
player_b_points = 100

for i in range(rounds):
    rolls = input().split()

    # convert string to int
    for i in range(len(rolls)):
        rolls[i] = int(rolls[i])

    if rolls[0] > rolls[1]:
        player_b_points -= rolls[0]
    elif rolls[1] > rolls[0]:
        player_a_points -= rolls[1]

print(player_a_points)
print(player_b_points)