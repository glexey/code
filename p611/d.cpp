#include<bits/stdc++.h>
using namespace std;
const int N=5005;
char s[N];
int a[N][N];
int fs[N][N];
int n;
bool bigger(int l1, int r1, int l2, int r2) {
    int len = r1-l1;
    if (len>r2-l2) return true;
    if (len<r2-l2) return false;
    int fd = fs[l1][l2];
    return s[l1+fd]>s[l2+fd];
}
int f(int l, int r, int ml, int mr) {
    int& ans = a[l][mr-ml];
    if (ans > -1) return ans;
    ans = bigger(l,r,ml,mr);
    if (!ans || (r == l)) return ans;
    for (int k=mr-ml; k<r-l; k++) {
        if (s[l+k] == '0') continue;
        if (bigger(l,l+k-1,ml,mr))
            ans = (ans + f(l+k,r,l,l+k-1)) % 1000000007;
    }
    return ans;
}
int main()
{
    memset(a, -1, sizeof(a));
    scanf("%d", &n);
    scanf("%s", &s[1]);
    for (int i = n; i >= 0; i--) {
        for (int j = n; j >= 0; j--) {
            if (i == n || j == n) fs[i][j] = 0;
            else if (s[i] == s[j]) fs[i][j] = fs[i + 1][j + 1] + 1;
            else fs[i][j] = 0;
        }
    }
    s[0] = '0';
    printf("%d\n", f(1,n,0,0));
}
