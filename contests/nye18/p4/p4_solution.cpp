#include <iostream>
#include <string.h>
#include <bitset>
typedef long long ll;

bool digit_in_number(ll digit, ll number)
{
    ll current_digit;
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

#define MAXN 20000001

int main() 
{ 
    ll n;
    int k;
    std::cin >> n >> k;
    
    std::bitset<MAXN> prime;
    prime.set();
    
    for (ll p=2; p*p<=n; p++) 
    { 
        if (prime[p] == true) 
        { 
            for (ll i=p*p; i<=n; i += p)
            {
                prime[i] = false;
            }
        } 
    } 
  
    ll sum = 0;
    for (ll p=2; p<=n; p++)
    {
        if (prime[p] && digit_in_number(k,p))
        {
            sum += p;
        } 
    }
          
    std::cout << sum << "\n";
} 