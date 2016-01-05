#include <bits/stdc++.h>
using namespace std;
vector<char> s,a,b;
char c;
int main() {
    while ((c=getchar())>40) s.push_back(c);
    for (int i=0; i<=s.size(); i++)
        for (c='a'; c<='z'; c++) {
            a = s; a.insert(a.begin()+i, c);
            b = a; reverse(b.begin(), b.end());
            if (a==b) {
                for (auto x:a) putchar(x);
                putchar('\n');
                exit(0);
            }
        }
    printf("NA\n");
}
