def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp

ascend = bool(input("Do you want to sort in ascending order? "))
values = [int(i) for i in input().split()]

for i in range(len(values)):
    for j in range(i, len(values)):
        if (ascend and values[i] < values[j]) or (not ascend and values[i] > values[j]):
            swap(values, i, j)

for value in values:
    print(value)
        
