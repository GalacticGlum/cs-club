#include <iostream>
#include <vector>
#include <string.h>
#include <algorithm>
#define MAXN 1000001

struct query_t {
    int l, r, k, index;
};

struct entry_t {
    int v, index;
};

int bit[MAXN];
int n;

bool entry_cmp(entry_t a, entry_t b) {
    return a.v < b.v;
}

bool query_cmp(query_t a, query_t b) {
    return a.k < b.k;
}

void update(int index, int value) {
    for(;index<=n; index += index&-index){
        bit[index]+=value;
    }
}

int query(int index) {
    int r = 0;
    for(;index > 0; index-=index&-index) {
        r += bit[index];
    }
    return r;
}

int main() {
    int q;
    std::cin >> n >> q;

    memset(bit, 0, sizeof(bit));

    std::vector<entry_t> entries;
    std::vector<query_t> queries;

    for (int i = 0; i < n; ++i) {
        int v;
        std::cin >> v;
        entries.push_back({v,i});
    }

    for (int i = 0; i < q; ++i) {
        int l, r, k;
        std::cin >> l >> r >> k;
        queries.push_back({l,r,k,i});
    }

    std::sort(entries.begin(), entries.end(), entry_cmp);
    std::sort(queries.begin(), queries.end(), query_cmp);

    int current = 0;
    std::vector<int> result(q);

    for (int i = 0; i < q; ++i) {
        while(current < n && entries[current].v <= queries[i].k) {
            update(entries[current].index+1,1);
            current++;
        }

        result[queries[i].index]=query(queries[i].r+1)-query(queries[i].l);
    }

    for (auto& r : result) {
        std::cout << r << "\n";
    }
}