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

    vector<vector<float>> L(n, vector<float>(n, 0));
    vector<vector<float>> U(n, vector<float>(n, 0));

    loop(i, 0, n) L[i][i] = 1;

    loop(j, 0, n)
    {
        U[0][j] += A[0][j];
        if (j > 0)
            L[j][0] += A[j][0] / U[0][0];
    }

    loop(i, 1, n)
    {
        loop(j, 1, n)
        {
            if (i <= j)
            {
                U[i][j] += A[i][j];
                loop(k, 0, i) U[i][j] -= L[i][k] * U[k][j];
            }
            else
            {
                L[i][j] += A[i][j];
                loop(k, 0, j) L[i][j] -= L[i][k] * U[k][j];
                L[i][j] /= U[j][j];
            }
        }
    }

    // Substitution
    float Z[n];
    loop(k, 0, n)
    {
        float val = 0;
        loop(j, 0, k + 1) val += L[k][j] * Z[j];
        Z[k] = (B[k] - val) / L[k][k];
    }

    float X[n];
    for (ll k = n - 1; k >= 0; k--)
    {
        float val = 0;
        loop(j, k + 1, n) val += U[k][j] * X[j];
        X[k] = (Z[k] - val) / U[k][k];
    }

    loop(i, 0, n) cout << X[i] << " ";

    // Input-
    // 1x + 1y + 1z = 1
    // 4x + 3y - 1z = 6
    // 3x + 5y + 3z = 4

    // Output-
    // X = [1 0.5 -0.5]
    
    return 0;
}