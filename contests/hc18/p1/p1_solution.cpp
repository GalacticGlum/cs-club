#include <iostream>
#include <cmath>
#include <algorithm>

int main() {
    int n, mx, my;
    std::cin >> n >> mx >> my;

    long long max_value = 0;
    for (int i = 0; i < n; ++i) {
        int x, y, s;
        std::cin >> x >> y >> s;
        long long distance = std::pow(mx-x,2) + std::pow(my-y,2);
        max_value = std::max(max_value, std::abs(distance-s));
    }
    
    std::cout << max_value << "\n";
}