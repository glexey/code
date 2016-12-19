#include <bits/stdc++.h>
using namespace std;
const int N = 200005;
char s[N];
int xd[N];
int xr[N];
int n, nd, nr, id, ir, nnd, nnr;
int main() {
    scanf("%d\n", &n);
    for (int i=0;i<n;i++) {
        scanf("%c", &s[i]);
        if (s[i] == 'R')
            xr[nr++]=i;
        else
            xd[nd++]=i;
    }
    nnd = nd;
    nnr = nr;
    int i = 0;
    int ir= 0;
    int id= 0;
    while (1) {
        if (xr[ir] == i) {
            xd[id] = -1;
            nnd--;
            ir = (ir + 1)%nr;
        } else if (xd[id] == i) {
            xr[ir] = -1;
            nnr--;
            id = (id + 1)%nd;
        }
        if (nnd==0) {
            printf("R\n");
            break;
        }
        if (nnr==0) {
            printf("D\n");
            break;
        }
        for (int j=0; j<n; j++) {
            if (xr[(ir+j)%nr] != -1) {
                ir = (ir+j)%nr;
                break;
            }
        }
        for (int j=0; j<n; j++) {
            if (xd[(id+j)%nd] != -1) {
                id = (id+j)%nd;
                break;
            }
        }
        i = (i+1) % n;
    }
}
