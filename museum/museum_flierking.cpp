#include <cstdio>
using namespace std;
int d[4];
char ss[1001];
int aa[1000001];
int ff[1001001] = {};
int li[1000000];
int aans[100000];
int main()
{
    int nans=3;
    int n, m, k;
    scanf("%d %d %d", &n, &m, &k);
    d[0]=-m; d[1]=-1; d[2]=1; d[3]=m;
	for (int i=0;i<n;i++) {
        scanf("%s", ss);
        for (int j=0;j<m;j++) {
            int ii = i*m+j;
            if (ss[j] == '.') 
                aa[ii] = 0;
            else {
                aa[ii] = 3;
                ff[ii-1]++;
                ff[ii+1]++;
                if (i) ff[ii-m]++;
                ff[ii+m]++;
            }
        }
    }
	for (int i=0;i<k;i++)
	{
        int x0, y0;
        scanf("%d %d", &x0, &y0); x0--; y0--;
        long i0 = x0*m+y0;
		if (aa[i0]<4) {
            nans++;
			int st=0, en=0, ans=0;
            li[st] = i0;
			while (st<=en) {
                int j = li[st];
                aa[j] = nans;
                if (ff[j]) {
                    // Something around
                    ans += ff[j];
                    for (int l=0;l<=3;l++) {
                        int ni=j+d[l];
                        if (aa[ni]==0) {
                            li[++en]=ni;
                            aa[ni]=1;
                        }
                    }
                } else {
                    // Nothing around
                    for (int l=0;l<=3;l++) {
                        int ni=j+d[l];
                        if (aa[ni]==0) {
                            li[++en]=ni;
                            aa[ni]=1;
                        }
                    }
                }
                st++;
            }
            printf("%d\n", ans);
            aans[nans] = ans;
        }
        else printf("%d\n", aans[aa[i0]]);
    }
    return 0;
}
