#include <iostream>

#define PI 3.14

int main() {
    int n;
    std::cin >> n;
    for (int i = 0; i < n; ++i) {
        int r, theta;
        std::cin >> r >> theta;
        float arc_length = (2*PI*r*theta)/360;
        std::cout.precision(2);
        std::cout << std::fixed << arc_length << "\n";
    }
}