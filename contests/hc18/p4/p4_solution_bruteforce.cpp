#include <iostream>
#include <vector>
#include <string.h>
#include <algorithm>
#define MAXN 1000001

int main() {
    int n, q;
    std::cin >> n >> q;

    std::vector<int> values;
    for (int i = 0; i < n; ++i) {
        int v;
        std::cin >> v;
        values.push_back(v);
    }

    for (int i = 0; i < q; ++i) {
        int l, r, k;
        std::cin >> l >> r >> k;
        int count = 0;
        for (int j = l; j <= r; ++j) {
            if(values[j] <= k) {
                count+=1;
            }
        }

        std::cout << count  << "\n";
    }  
}