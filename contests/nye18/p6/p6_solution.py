n,m,k=map(int,input().split())

tracks = {}
for _ in range(k):
    r,a,b=map(int,input().split())
    if r not in tracks:
        tracks[r] = []

    tracks[r].append((a, b))

occupied = 0
for k in tracks:
    intervals = tracks[k]
    intervals.sort()

    start = temp[0][0]
    end = temp[0][1]
    points = 0

    for i in range(1, len(intervals)):
        if intervals[i][0] > end:
            points += end - start + 1
            begin = intervals[i][0]
            end = intervals[i][1]
        else:
            end = max(end, intervals[i][1])

    points += end - start + 1
    occupied += points

print(m*n - occupied)  