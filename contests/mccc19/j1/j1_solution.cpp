#include <iostream>
typedef long long ll;

int main() {
    std::ios_base::sync_with_stdio(NULL);
    std::cout.tie(0);
    std::cin.tie(0);

    ll q;
    std::cin >> q;
    for(ll i = 0; i < q; ++i) {
        ll f1,f2;
        std::cin >> f1 >> f2;
        if(f2 > f1) {
            std::cout << "towards\n"; 
        } else if(f2 < f1) {
            std::cout << "away\n";
        } else {
            std::cout << "none\n";
        }
    }    
}