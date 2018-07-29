n = int(input())
first_names = input().split(' ')
second_names = input().split(' ')

def check_names():
    for i in range(n):
        if first_names[i] == second_names[i]:
            return False

        for j in range(n):
            has_match = (first_names[j] == first_names[i] and second_names[j] != second_names[i])
            has_reverse_match = (second_names[j] == first_names[i] and first_names[j] != second_names[i])

            if has_match or has_reverse_match:          
                return False

    return True
        
if check_names():
    print("Thank Mr. Lane")
else:
    print("Dammit Mr. Lane")
        