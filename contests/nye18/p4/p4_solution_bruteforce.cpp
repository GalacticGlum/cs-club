#include <iostream>

bool is_prime(int n) 
{ 
    if (n <= 1) return false; 
    for (int i = 2; i < n; i++)
    {
        if (n % i == 0) return false;
    }
  
    return true; 
}

bool digit_in_number(int digit, int number)
{
    int current_digit;
    while (number != 0)
    {
        current_digit = number % 10;
        number /= 10;
                                       
        if (current_digit == digit)
        {
            return true;
        }
    }
    
    return false;
}

int main() 
{ 
    int n, k;
    std::cin >> n >> k;
    
    int sum = 0;
    for (int i = 2; i <= n; i++) { 
        if (is_prime(i) && digit_in_number(k,i))
        {
            sum +=i;
        } 
    }
    
    std::cout << sum << "\n";
}