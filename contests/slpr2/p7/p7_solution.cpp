#include<iostream>
#include<algorithm>
#include<fstream>
#include<string>
#include<cstring>
#define INF 0x3f3f3f3f
#define endl "\n"

using namespace std;
const int MAXN = 1000;
int d[MAXN][MAXN];
int N, M, Q;
int main()
{
    ifstream file;
    file.open("p7.2.20.in");
    ofstream ofile;
    ofile.open("p7.2.20.out");

    memset(d, INF, sizeof(d));

    file >> N >> M >> Q;

    int x, y, z;
    while (M--)
    {
        file >> x >> y >> z;
        d[x-1][y-1] = min(d[x-1][y-1], z);
        d[y-1][x-1] = min(d[y-1][x-1], z);
    }

    for (int k = 0; k < N; ++k)
    {
        for (int i = 0; i < N; ++i)
        {
            for (int j = 0; j < N; ++j)
            {
                if (d[i][k] + d[k][j] < d[i][j])
                {
                    d[i][j] = d[i][k] + d[k][j]; 
                }
            }
        }
    }

    int a, b;
    while (Q--)
    {
        file >> a >> b;
        if (d[a-1][b-1] == INF) ofile << -1;
        else ofile << d[a-1][b-1];
        ofile << endl;
    }
    ofile.close();
    file.close();
}