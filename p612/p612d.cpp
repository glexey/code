#include <bits/stdc++.h>
using namespace std;
typedef pair<int,int> PI;
priority_queue<PI,vector<PI>,greater<PI>> a;
vector<PI> o;
int main() {
    int i,n,k,s,e,m=0;
    scanf("%d%d", &n, &k);
    for(i=0;i<n;++i) {
        scanf("%d%d", &s, &e);
        a.push({s, 0});
        a.push({e, 1});
    }
    while(!a.empty()) {
        auto i = a.top(); a.pop();
        if (i.second) {
            if (m--==k)
                o.push_back(PI(s, i.first));
        } else
            if (++m==k)
                s = i.first;
    }
    printf("%d\n", o.size());
    for(auto i:o)
        printf("%d %d\n", i.first, i.second);

}
