#include <bits/stdc++.h>
using namespace std;
const int N = 10005;
vector<int> d[N]; // list of tunnel ids from a city
pair<int,int> ab[N];
bool vis[N]; // visited pairs
bool deleted[N];
int n, m, a, b;
int main() {
    scanf("%d%d", &n, &m);
    for (int i=0; i<m; i++) {
        scanf("%d%d", &a, &b);
        ab[i] = {a, b};
        d[a].push_back(i);
    }
    int ans = m;
    for (int i=0; i<m; i++) {
        // For each tunnel, see if there's an alternative path
        memset(vis, 0, sizeof(vis));
        vis[i] = true;
        int from = ab[i].first;
        int to = ab[i].second;
        queue<int> q;
        while(1) {
            printf("i=%d from:%d to:%d\n", i, from, to);
            if (from == to) {
                ans--;
                deleted[i]=true;
                printf("del %d (%d=>%d)\n", i,ab[i].first,ab[i].second);
                break;
            }
            for (auto c:d[from]) {
                int t = ab[c].second;
                if (!deleted[c] && !vis[c]) {
                    q.push(t);
                    vis[c] = true;
                }
            }
            if (q.empty()) break;
            from = q.front(); q.pop();
        }
    }
    printf("%d\n", ans);
}
