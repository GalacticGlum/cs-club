#include <iostream>

int main() {
    std::ios_base::sync_with_stdio(NULL);
    std::cin.tie(0);
    std::cout.tie(0);
    int n;
    std::cin >> n;
    bool res=true;
    for(int i=0; i < n; ++i) {
        int r,p;
        std::cin >> r >> p;
        if(r != p) {
            res=false;
            break;
        }
    }
    std::cout << (res==true?"yes":"no") << "\n";
}