#include <iostream>
#include <string>

#define INFINITY 0x3f3f3f3f;

int min3(int x, int y, int z) {
    return std::min(std::min(x,y),z);
}

int min_edit_distance(std::string a, std::string b, int m=-1, int n=-1) {
    if (m==-1) m = a.length();
    if (n==-1) n = b.length();

    if (m==0) return n;
    if (n==0) return m;
    if (a[m-1] == b[n-1]) return min_edit_distance(a, b, m-1, n-1);
    return 1 + min3(min_edit_distance(a, b, m, n-1),
                    min_edit_distance(a, b, m-1, n),
                    min_edit_distance(a, b, m-1, n-1));
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