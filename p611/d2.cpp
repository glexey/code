#include<bits/stdc++.h>
using namespace std;
const int N=5005;
char s[N];
int dp[N][N]; // dp[k,len]: number of cuts of string 0..k-1
              // such that last number is of length len
int fs[N][N];
int n;
bool smaller(int l1, int l2, int len) {
    int fd = fs[l1][l2];
    if (fd >= len) return false;
    return s[l1+fd]<s[l2+fd];
}
void inc(int& a, int b) { a = (a+b) % 1000000007; }
int main()
{
    scanf("%d", &n);
    scanf("%s", &s);
    for (int i = n; i >= 0; i--) {
        for (int j = n; j >= 0; j--) {
            if (i == n || j == n) fs[i][j] = 0;
            else if (s[i] == s[j]) fs[i][j] = fs[i + 1][j + 1] + 1;
            else fs[i][j] = 0;
        }
    }
    int ans = 0;
    for (int i=0; i<n; i++) {
        int isum = 0; // accumulate dp[i][1]+dp[i][2]+...
        for (int len=1; len<=n-i; len++) {
            if (i==0) dp[i][len]=1;
            else if (s[i]=='0') dp[i][len]=0;
            else {
                dp[i][len] = isum; // sum( dp[i][1..len-1] )
                int num = (i-len >= 0) ? dp[i-len][len] : 0;
                if (num && smaller(i-len,i,len)) inc(dp[i][len], num);
                inc(isum, num);
            }
        }
        inc(ans, dp[i][n-i]);
    }
    printf("%d\n", ans);
}
