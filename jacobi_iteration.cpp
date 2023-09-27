#include <bits/stdc++.h>
using namespace std;

#define ll long long
#define loop(lcv, lower, upper) for (ll lcv = lower; lcv < upper; lcv++)

int main()
{
    ll n;
    cin >> n;
    float A[n][n];
    loop(i, 0, n)
    {
        loop(j, 0, n) cin >> A[i][j];
    }
    float B[n];
    loop(i, 0, n) cin >> B[i];

    float X[n], updatedX[n];
    loop(i, 0, n) X[i] = B[i] / A[i][i];
    float error = 1;
    ll reps = 0;
    while (error > 0.0000001)
    {
        reps++;
        float tolerance = INT64_MIN;
        loop(i, 0, n)
        {
            float val = B[i];
            loop(j, 0, n)
            {
                if (i == j)
                    continue;
                val -= A[i][j] * X[j];
            }
            updatedX[i] = val / A[i][i];
            tolerance = max(tolerance, abs(updatedX[i] - X[i]));
        }
        error = tolerance;
        loop(i, 0, n)
        {
            X[i] = updatedX[i];
            // cout << X[i] << " ";
        }
        // cout << endl;
    }

    cout << "Number of iterations: " << reps << endl;
    loop(i, 0, n) cout << updatedX[i] << " ";

    return 0;
}