#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define loop(lcv, lower, upper) for (ll lcv = lower; lcv < upper; lcv++)
float X[1001], Y[1001];

int main()
{
    ll n;
    cin >> n;
    loop(i, 0, n)
    {
        cin >> X[i] >> Y[i];
    }
    float x;
    cin >> x;
    float ans = 0;
    loop(i,0,n)
    {
        float prod = 1;
        loop(j,0,n)
        {
            if( i == j) continue;
            prod *= (x-X[j]) / (X[i] - X[j]);
        }
        ans += Y[i] * prod;
    }
    cout << ans << endl;
    return 0;
}