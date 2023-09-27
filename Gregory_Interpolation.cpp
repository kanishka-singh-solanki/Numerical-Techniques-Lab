#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define loop(lcv, lower, upper) for (ll lcv = lower; lcv < upper; lcv++)
float X[1001], Y[1001], Diff[1001][1001];

ll fact(ll n)
{
    if(n == 0) return 1;
    return n * fact(n-1);
}

int main()
{
    ll n;
    cin >> n;
    loop(i, 0, n)
    {
        cin >> X[i] >> Y[i];
        Diff[i][i] = Y[i];
    }
    loop(k,1,n)
    {
        for(ll i = 0; i + k < n; i++)
        {
            Diff[i][i+k] = (Diff[i+1][i+k] - Diff[i][i+k-1]);
        }
    }
    float x;
    cin >> x;
    float h = (X[1] - X[0]);
    float s = (x - X[0])/h;
    float ans = Diff[0][0];
    loop(i,1,n)
    {
        float prod = 1;
        loop(j,0,i)
        {
            prod *= (s-j);
        }
        ans += (Diff[0][i] * prod) / fact(i);
    }
    cout << ans << endl;
    return 0;
}