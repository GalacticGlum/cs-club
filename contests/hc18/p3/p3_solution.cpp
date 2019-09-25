#include <iostream>
#include <string>

#define INFINITY 0x3f3f3f3f

int min3(int x, int y, int z) {
    return std::min(std::min(x,y),z);
}

int min_edit_distance(std::string a, std::string b) {
    int m = a.length(), n = b.length();
    int cache[m+1][n+1];

    for(int i = 0; i <= m; ++i) {
        for(int j = 0; j <= n; ++j) {
            if(i == 0) {
                cache[i][j] = j;
            } else if(j == 0) {
                cache[i][j] = i;
            } else if (a[i-1] == b[j-1]) {
                cache[i][j] = cache[i-1][j-1];
            } else {
                cache[i][j] = 1 + min3(cache[i][j-1], cache[i-1][j], cache[i-1][j-1]);
            }
        }
    }

    return cache[m][n];
}

int main() {
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(nullptr);
    std::cout.tie(nullptr);

    int n, m;
    std::cin >> n >> m;

    std::string dictionary[n];
    std::string encrypted[m];

    for (int i = 0; i < n; ++i) {
        std::cin >> dictionary[i];
    }

    for (int i = 0; i < m; ++i) {
        std::cin >> encrypted[i];
    }

    for (int i = 0; i < m; ++i) {
        std::string encrypted_word = encrypted[i];
        int min_distance = INFINITY;
        std::string decrypted_word;

        for (int j = 0; j < n; ++j) {
            int distance = min_edit_distance(encrypted_word, dictionary[j]);
            if (distance < min_distance) {
                min_distance = distance;
                decrypted_word = dictionary[j];
            }
        }

        std::cout << decrypted_word;
        if (i < m) {
            std::cout << " ";
        }
    }
}