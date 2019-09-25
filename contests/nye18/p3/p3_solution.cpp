#include <iostream>

int main() {
    int n;
    std::cin >> n;
    
    int max_area=0;
    int px,py;
    for (int i = 0; i < n; ++i) {
        int x,y,w,h;
        std::cin >> x >> y >> w >> h;
        int area = w*h;
        if (area > max_area) {
            max_area = area;
            px=x;
            py=y;
        }
    }
    
    std::cout << px << " " << py << "\n";
}