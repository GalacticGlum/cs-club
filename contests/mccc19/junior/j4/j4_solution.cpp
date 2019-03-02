#include <iostream>
typedef unsigned long long ull;
#define MOD 1000000007

int main() {
    std::ios_base::sync_with_stdio(NULL);
    std::cin.tie(0);
    std::cout.tie(0);

    ull a, b;
    std::cin >> a >> b;

    ull d = (b*b)*(b+1)*(b+1) - (a*a)*(a-1)*(a-1);
    std::cout << (d / 4)%MOD << "\n";
}