#include <iostream>
using namespace std;

int main() {
  int N, X, i;
  cin >> N >> X;
  int A[N];
  for (i = 0; i < N; i++)
    cin >> A[i];
  for (i = 0; i < N; i++) {
    if (A[i] < X)
      cout << A[i] << ' ';
  }
}