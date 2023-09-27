#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define loop(lcv, lower, upper) for (ll lcv = lower; lcv < upper; lcv++)
double X[1001], Y[1001], inverseDividedDiff[1001][1001];

int main()
{
    ll n;
    cin >> n;
    loop(i, 0, n)
    {
        cin >> X[i] >> Y[i];
    }
    loop(i,1,n)
    {
        inverseDividedDiff[0][i] = (X[i] - X[0]) / (Y[i] - Y[0]);
    }
    loop(i,1,n)
    {
        loop(j,1,n)
        {
            if(i < j)
                inverseDividedDiff[i][j] = (X[j] - X[i]) / (inverseDividedDiff[i-1][j] - inverseDividedDiff[i-1][i]);
        }
    }
    
    double x;
    cin >> x;
    double y = inverseDividedDiff[n-2][n-1];
    for(ll i = n - 2; i > 0; i--)
    {
        y = (x-X[i])/y + inverseDividedDiff[i-1][i];
    }
    y = Y[0] + (x-X[0])/y;
    cout << y;
    return 0;
}