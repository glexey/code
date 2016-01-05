#include <bits/stdc++.h>
using namespace std;
const int N = 30010;
const int P = 500;
int s[N]; // Number of gems on an island
int dp[N][P]; // Number of gems starting with N, step P
int n, first_step, last, step, minstep, maxstep, pos;
int main() {
    scanf("%d%d", &n, &first_step);
    while(n--) {
        scanf("%d", &last);
        s[last]++;
    }
    for (minstep=first_step,pos=first_step; pos<=last && minstep != 1; pos+=--minstep);
    maxstep=minstep+P-1;
    for (pos=last; pos>=first_step; pos--) {
        for (step=minstep; step<=maxstep; step++) {
            int num = 0;
            for (int s=max(1,step-1); s<=step+1; s++)
                if (pos+s<=last)
                    num = max(num, dp[pos+s][s-minstep]);
            dp[pos][step-minstep] = s[pos] + num;
        }
    }
    printf("%d\n", dp[first_step][first_step-minstep]);
}
