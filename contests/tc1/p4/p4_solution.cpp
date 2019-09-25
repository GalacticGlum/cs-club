#include <iostream>
#include <cmath>
#include<iomanip>
typedef long long ll;
struct point {
    ll x, y;
};

int main() {
    std::iostream::ios_base::sync_with_stdio(NULL);
    std::cin.tie(0);
    std::cout.tie(0);
    ll n;
    std::cin >> n;
    point p[n];
    for(ll i = 0; i < n; ++i){
        ll x, y;
        std::cin >> x >> y;
        p[i]={x,y};
    }
    double area=0;
    for (ll i = 0; i < n; ++i){
        point p1 = p[i];
        point p2 = p[(i+1)%n];
        area+=(p1.x*p2.y)-(p1.y*p2.x);
    }
    area=std::fabs(area/2);
    std::cout << std::setprecision(2) << std::fixed << area << "\n";
}