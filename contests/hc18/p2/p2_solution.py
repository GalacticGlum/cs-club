def print_current_state(start, previous):
    if previous != -1:
        if previous - start == 0:
            print(previous, end=' ')
        elif previous - start == 1:
            print(start, end=' ')
            print(previous, end=' ')
        else:
            print(f'{start}-{previous}', end=' ')

N = int(input())
works = [int(i) for i in input().split()]
works = sorted(works)

start = -1
previous = -1
for work in works:
    if work != previous + 1:
        print_current_state(start, previous)
        start = work
        previous = work
    else:
        previous = work

print_current_state(start, previous)