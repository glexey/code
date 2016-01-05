#include <bits/stdc++.h>
using namespace std;
const int N = 10005;
vector<int> d[N];
bool vis[N], checked[N];
int n, m, a, b;
int main() {
    scanf("%d%d", &n, &m);
    for (int i=0; i<m; i++) {
        scanf("%d%d", &a, &b);
        d[a].push_back(b);
    }
    int nodes = 0;
    // count number of nodes
    for (int i=1; i<=n; i++)
        nodes += d[a].size() > 0;

    // Check if there are any cycles
    bool no_cycles = true;
    for (int i=1; i<=n && no_cycles; i++) {
        if (checked[i]) continue;
        memset(vis, 0, sizeof(vis));
        queue<int> q;
        q.push(i);
        printf("--i=%d\n", i);
        while(!q.empty()) {
            int j = q.front(); q.pop();
            printf("j=%d vis[j]=%d\n", j, vis[j]);
            checked[j] = true;
            if (vis[j]) { no_cycles = false; break; }
            vis[j] = true;
            for (auto c:d[j]) q.push(c);
        }
    }
    printf("nodes=%d no_cycles=%d\n", nodes, no_cycles);
    printf("%d\n", nodes - no_cycles);
}
