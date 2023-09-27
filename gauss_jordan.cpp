#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define loop(lcv, lower, upper) for (ll lcv = lower; lcv < upper; lcv++)

int main()
{
    ll n;
    cin >> n;
    float a[n][n + 1];
    float I[n];

    loop(i, 0, n)
    {
        loop(j, 0, n + 1) cin >> a[i][j];
    }

    loop(k, 0, n - 1)
    {
        loop(i, k + 1, n)
        {
            for (ll j = n; j >= k; j--)
                a[i][j] -= a[i][k] * a[k][j] / a[k][k];
        }
    }

    for (ll k = n - 1; k > 0; k--)
    {
        for (ll i = k - 1; i >= 0; i--)
        {
            a[i][n] -= a[i][k] * a[k][n] / a[k][k];
            for (ll j = k; j >= 0; j--)
                a[i][j] -= a[i][k] * a[k][j] / a[k][k];
        }
    }

    for (ll k = n - 1; k >= 0; k--)
    {
        I[k] = a[k][n] / a[k][k];
    }

    loop(i, 0, n) cout << I[i] << " ";

    // Equations-
    // 76I1 - 25I2 - 50I3 = 10
    // 25I1 - 56I2 + 1I3 = 0
    // 50I1 + 1I2 - 106I3 = 0

    // Output-
    // I = [0.244934 0.111428 0.116586]

    return 0;
}