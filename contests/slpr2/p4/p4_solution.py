N, M = [int(i) for i in input().split()]
C = [int(i) for i in input().split()]
boxes = []
for i in range(M):
    boxes.append([ord(house) - ord("A") for house in input().split()])

for student in range(N):
    tally_ho = {0: 0, 1: 0, 2: 0, 3: 0}
    for box in boxes:
        tally_ho[box[student]] += 1

    tally_ho = {k:v for (k,v) in tally_ho.items() if C[k] > 0}
    if len(tally_ho) == 0:
        print("E")
    else:
        house = max(tally_ho, key=lambda k: (tally_ho[k], -k))
        print(chr(house + ord("A")))
        C[house] -= 1