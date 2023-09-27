#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define loop(lcv, lower, upper) for (ll lcv = lower; lcv < upper; lcv++)

int main()
{
    ll n;
    cin >> n;
    float a[n][n + 1];
    float x[n];
    loop(i, 0, n)
    {
        loop(j, 0, n + 1) cin >> a[i][j];
    }

    loop(k, 0, n - 1)
    {
        ll l = k;
        float curr = a[k][k];
        loop(q, k + 1, n)
        {
            if (a[q][k] > curr)
            {
                curr = a[q][k];
                l = q;
            }
        }

        loop(q, 0, n + 1) swap(a[k][q], a[l][q]);

        loop(i, k + 1, n)
        {
            for (ll j = n; j >= k; j--)
                a[i][j] -= a[i][k] * a[k][j] / a[k][k];
        }
    }

    for (ll k = n - 1; k >= 0; k--)
    {
        float val = 0;
        loop(j, k + 1, n) val += a[k][j] * x[j];
        x[k] = (a[k][n] - val) / a[k][k];
    }
    loop(i, 0, n) cout << x[i] << " ";

    // Input-
    // 0x + 2y + 1z = -8
    // 1x - 2y - 3z = 0
    // -1x + 1y + 2z = 3

    // Output-
    // X = [-4 -5 2]

    return 0;
}