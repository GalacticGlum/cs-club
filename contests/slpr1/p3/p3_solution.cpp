#include <iostream>
#include <vector>

typedef unsigned long long ull;

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(NULL);
    
    int n, q;
    std::cin >> n >> q;
    
    int d_psa[1000000];
    int p_psa[1000000];

    for (int i = 1; i <= n; ++i) {
        int x;
        std::cin >> x;
        d_psa[i]=d_psa[i-1]+x;
    }
    
    for (int i = 1; i <= n; ++i) {
        int x;
        std::cin >> x;
        p_psa[i]=p_psa[i-1]+x;
    }

    for (int i = 0; i < q; ++i) {
        int l, r;
        std::cin >> l >> r;

        ull ds = d_psa[r]-d_psa[l-1];
        ull ps = p_psa[r]-p_psa[l-1];

        if (ds==ps) {
            std::cout << "WOOHOO!\n";
        } else {
            std::cout << "BOOHOO!\n";
        }
    }
}