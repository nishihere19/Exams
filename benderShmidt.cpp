#include <bits/stdc++.h>
using namespace std;

//Edit this function wrt to question
int calc(int x)
{
    int t;
    t = x * x*(25-(x*x));
    return t;
}

int main()
{
    int limit1, limit2;
    float value1, value2;
    int calc(int x);
    cout << "\n Enter first boundary value x ";
    cin >> limit1;
    cout << "\n Enter first boundary value t ";
    cin >> value1;
    cout << "\n Enter second boundary value x ";
    cin >> limit2;
    cout << "\n Enter second boundary value t ";
    cin >> value2;
    float h;
    cout << "\n Enter the value of h ";
    cin >> h;
    float a;
    cout << "\n Enter the value of a ";
    cin >> a;
    float k = (h * h * a) / 2;
    int m, n;
    m=limit2;
    cout << "\n Enter time limit ";
    cin >> a;
    n = (a / k);
    float arr[n + 2][m + 2] = {0};
    for (int i = 1; i <= m + 1; i++)
    {
        arr[0][i] = limit1 + (h * (i - 1));
    }
    for (int i = 1; i <= n + 1; i++)
    {
        arr[i][0] = (k * (i - 1));
    }
    for (int i = 1; i <= n + 1; i++)
    {
        arr[i][1] = value1;
    }
    for (int i = 0; i <= n + 1; i++)
    {
        arr[i][limit2 + 1] = value2;
    }
    for (int j = 2; j <= m; j++)
    {
        arr[1][j] = calc(arr[0][j]);
    }
    for(int i=2;i<=n+1;i++){
        for(int j=2;j<=m;j++){
            arr[i][j]=(arr[i-1][j-1]+arr[i-1][j+1])/2;
        }
    }
    for (int i = 0; i <= n + 1; i++)
    {
        for (int j = 0; j <= m + 1; j++)
        {
            cout << arr[i][j] << "\t";
        }
        cout << endl;
    }
    return 0;
}