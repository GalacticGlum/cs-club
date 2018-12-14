#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <math.h>
#include <stdio.h>
#include <string.h>
using namespace std;
#define MEM(a, b) memset(a, (b), sizeof(a))
#define PI 3.1415926535897932384626433832795
#define endl '\n'
#define exists(s, e) (s.find(e)!=s.end())
#define WHILE(n)
#define pii pair<int,int>
#define pb push_back
#define f first
#define s second
#define scan(x) do{while((x=getchar())<'0'); for(x-='0'; '0'<=(_=getchar()); x=(x<<3)+(x<<1)+_-'0');}while(0)
char _;
typedef long long ll;
typedef long double ld;

const int INF = 0x3f3f3f3f;
#define MAXN 10003
int n,m, dp[MAXN];
vector<pii> a;

int main(){
    cin.sync_with_stdio(0);
    cin.tie(0);
    cin>>m>>n;

    for(int i = 0,x,y; i < n; i++){
        cin>>x>>y;
        a.pb({x,y});
    }
    for(int i = 0 ; i < n; i++){
        for(int j = m; j >= a[i].f; j--){
            dp[j] =  max(dp[j-a[i].f] + a[i].s, dp[j]);
        }
    }
    cout<<dp[m];
}