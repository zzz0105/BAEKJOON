#include <iostream>
using namespace std;

int main() {
  string A, B;
  long long answer = 0;
  cin >> A >> B;
  for (int i=0;i<A.length();i++) {
    for (int j=0;j<B.length();j++)
      answer += (A[i]-'0') * (B[j]-'0');
  }
  cout << answer;
}