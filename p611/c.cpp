#include <bits/stdc++.h>
using namespace std;
char ss[505];
int g[505];
int lr[505][505];
int tb[505][505];
int main() {
    int h,w,r,c,q,r1,c1,r2,c2,x;
    scanf("%d%d", &h, &w);
    for (int r=1;r<=h;r++) {
        scanf("%s", ss);
        for (int c=1;c<=w;c++) {
            x = ss[c-1] == '.';
            lr[r][c] = lr[r-1][c] + lr[r][c-1] - lr[r-1][c-1] + (x & g[c-1]);
            tb[r][c] = tb[r][c-1] + tb[r-1][c] - tb[r-1][c-1] + (x & g[c]);
            g[c] = x;
            }
        }
    scanf("%d", &q);
    while(q--) {
        scanf("%d%d%d%d", &r1, &c1, &r2, &c2);
        printf("%d\n", lr[r2][c2]-lr[r2][c1]-lr[r1-1][c2]+lr[r1-1][c1]+
                       tb[r2][c2]-tb[r2][c1-1]-tb[r1][c2]+tb[r1][c1-1]);
    }
}
