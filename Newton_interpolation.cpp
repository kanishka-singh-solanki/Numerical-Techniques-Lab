#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define loop(lcv, lower, upper) for (ll lcv = lower; lcv < upper; lcv++)
float X[1001], Y[1001], dividedDiff[1001][1001];

int main()
{
    ll n;
    cin >> n;
    loop(i, 0, n)
    {
        cin >> X[i] >> Y[i];
        dividedDiff[i][i] = Y[i];
    }
    loop(k,1,n)
    {
        for(ll i = 0; i + k < n; i++)
        {
            dividedDiff[i][i+k] = (dividedDiff[i+1][i+k] - dividedDiff[i][i+k-1]) / (X[i+k] - X[i]);
        }
    }
    float x;
    cin >> x;
    float ans = dividedDiff[0][0];
    loop(i,1,n)
    {
        float prod = 1;
        loop(j,0,i)
        {
            prod *= (x-X[j]);
        }
        ans += dividedDiff[0][i] * prod;
    }
    cout << ans << endl;
    return 0;
}