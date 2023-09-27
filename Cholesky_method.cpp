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

    vector<vector<float>> L(n, vector<float>(n, 0));
    vector<vector<float>> U(n, vector<float>(n, 0));
    vector<vector<float>> T(n, vector<float>(n, 0));

    loop(i, 0, n)
    {
        loop(j, 0, n)
        {
            if (i == j)
            {
                T[i][j] += A[i][j];
                loop(k, 0, i) T[i][j] -= T[k][i] * T[k][j];
                T[i][j] = sqrt(T[i][j]);
            }
            else if (i < j)
            {
                T[i][j] += A[i][j];
                loop(k, 0, i) T[i][j] -= T[k][i] * T[k][j];
                T[i][j] /= T[i][i];
            }
            else
                T[i][j] = T[j][i];
        }
    }

    loop(i, 0, n)
    {
        loop(j, 0, n)
        {
            if (i < j)
                U[i][j] = T[i][j];
            else if (i > j)
                L[i][j] = T[i][j];
            else
            {
                U[i][j] = T[i][j];
                L[i][j] = T[i][j];
            }
        }
    }

    cout << endl;
    loop(i,0,n)
    {
        loop(j,0,n) cout << L[i][j] << " ";
        cout << endl;
    }
    cout << endl;
    loop(i,0,n)
    {
        loop(j,0,n) cout << U[i][j] << " ";
        cout << endl;
    }
    return 0;
}
