#include <bits/stdc++.h>
using namespace std;

#define INT_MAX __INT_MAX__
#define INT_MIN (-INT_MAX - 1)
#define ll long long int
#define pii pair<int, int>
#define vi vector<ll>
#define all(x) x.begin(), x.end()
#define flus       \
    fflush(stdin); \
    fflush(stdout);
#define F first
#define S second
#define inf 1e9
#define mod 1000000007
#define N 200100

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string s;
    int n;
    cin >> n;
    int i = 0;
    while (i < n)
    {
        cin >> s;
        if (s.length() > 10)
        {
            cout << s[0] << s.length() - 2 << s[s.length() - 1] << "\n";
            cout << s[s.length() - 1] << "\n";
        }
        else
        {
            cout << s << "\n";
        }
        i++;
    }
    return 0;
}