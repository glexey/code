#include <bits/stdc++.h>
using namespace std;
const int N = 100005;
vector<int> v[N], u[N], w;
int c[N]; // color 0:white 1:gray 2:black
int d[N]; // discovered
int n, m, a, b, ans;

int dfs(int i) {
    c[i]++; // grey
    for (auto k:v[i]) {
        if (c[k] == 1) return 1; // back edge -> cycle
        if (c[k] == 0 && dfs(k)) return 1;
    }
    c[i]++; // black
    return 0;
}

int main() {
    scanf("%d%d", &n, &m);
    for (int i=0; i<m; i++) {
        scanf("%d%d", &a, &b);
        v[a].push_back(b); // Directed
        u[a].push_back(b); // Undirected
        u[b].push_back(a);
    }

    for (int i=0; i<=n; i++) {
        if (d[i] || !u[i].size()) continue;
        d[i]++;
        // BFS to explore elements in one disjoint set
        w.clear();
        deque<int> q;
        q.push_back(i);
        while(!q.empty()) {
            int j = q.front(); q.pop_front();
            w.push_back(j);
            for (auto k:u[j]) if (!d[k]) {
                q.push_back(k);
                d[k]++;
                ans++;
            }
        }
        // Add one if there's a cycle
        for (auto l:w) {
            if (c[l]) continue;
            if (dfs(l)) {
                ans++;
                break;
            }
        }
    }

    printf("%d\n", ans);
}
