#include <cstdio>

int main() {
    int n, m;
    int v[300005];
    scanf("%d %d", &n, &m);
    for (int i=0; i<n; i++)
        scanf("%d", &v[i]);
    int l=0,r=0,s=0,ans=0;
    while (r < n) {
        s += v[r];
        while (s > m) {
            s -= v[l];
            l += 1;
            if (l > r) {
                r = l-1;
                break;
            }
        }
        r += 1;
        if (s > ans) ans = s;
        if (ans == m) break;
    }
    printf("%d\n", ans);
}
