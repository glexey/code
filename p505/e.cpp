#include <bits/stdc++.h>
using namespace std;
const int N = 100005;
const int M = 5005;
typedef long long ll;
ll h[N], a[N], n,m,k,p, l,r,x, blows[M];

bool win(ll x) {
    memset(blows, 0, sizeof(blows));
    ll earlyfail = 0;
    for (int i=0; i<n; i++)
        earlyfail += max(0ll, (h[i]+m*a[i]-x)/p);
    if (earlyfail > m*k) return false;
    for (int i=0; i<n; i++) {
        if (x < a[i]) return false;
        ll hh = x;
        while(hh-m*a[i] < h[i]) {
            blows[min(m-1, hh/a[i]-1)]++;
            hh += p;
        }
    }
    ll c = 0;
    for (int i=m-1; i>=0; i--)
        c = max(blows[i]+c-k, 0ll);
    return !c;
}

int main() {
    scanf("%d%d%d%d",&n,&m,&k,&p);
    for (int i=0; i<n; i++)
        scanf("%d%d",&h[i],&a[i]);

    l=0; r=(m+1)*1e9;
    while (l<r-1) {
        x = (l+r)/2;
        *(win(x) ? &r : &l) = x;
    }
    printf("%I64d\n", r);
}
