def solve(n, k):
    def is_digit_in_number(number, digit):
        current_digit = 0
        while number != 0:
            current_digit = number % 10
            number //= 10

            if current_digit == digit:
                return True

        return False

    prime = [True]*(n+1)
    p = 2
    while p*p <= n:
        if prime[p]:
            for i in range(p*p,n+1,p):
                prime[i]=False
        p += 1

    prime_sum = 0
    for i in range(2,n+1):
        if prime[i] and is_digit_in_number(i,k):
            prime_sum += i

    return prime_sum

n,k=map(int,input().split())
print(solve(n,k))