#include <iostream>
using namespace std;

int main() {
  int N, i;
  cin >> N;
  
  for (i=1;i<N;i++) {
    int sum = i, num = i;
    while (num!=0) {  //자릿수 합
      sum += num%10;
      num/=10;
    }
    if (sum == N) {
      cout << i;
      exit(0);
    }
  }
  
  cout << 0;
  return 0;
}