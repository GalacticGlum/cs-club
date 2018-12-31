def solve(n,m,k,tracks):
    grid_points = 0
    mapper = {}
    for _ in range(k):
        r, c1, c2 = tracks[_]
        if r in mapper:
            mapper[r].append((c1, c2))
        else:
            mapper[r] = [(c1, c2)]
    for k in mapper:
        temp = mapper[k]
        temp.sort()
        begin = temp[0][0]
        end = temp[0][1]
        points = 0
        for i in range(1, len(temp)):
            if temp[i][0] > end:
                points += end - begin + 1
                begin = temp[i][0]
                end = temp[i][1]
            else:
                end = max(end, temp[i][1])
        points += end - begin + 1
        grid_points += points
    return m*n - grid_points  

n,m,k=map(int,input().split())
tracks=[]
for i in range(k):
    r,a,b=map(int,input().split())
    tracks.append((r,a,b))
    
print(solve(n,m,k,tracks))