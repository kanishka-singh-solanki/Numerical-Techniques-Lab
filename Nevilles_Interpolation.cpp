#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define loop(lcv, lower, upper) for (ll lcv = lower; lcv < upper; lcv++)
float X[1001], Y[1001];

float P(ll i, ll j, float x)
{
    if (i == j)
        return Y[i];
    ll value = ((X[j] - x) * P(i, j - 1, x) + (x - X[i]) * P(i + 1, j, x)) / (X[j] - X[i]);
    return value;
}

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
    cout << P(0, n -  1, x);
    return 0;
}