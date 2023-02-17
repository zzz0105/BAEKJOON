#include <iostream>
using namespace std;

int main() {
  int A, B, C, result;
  int nums[10] = {0, };
  cin >> A >> B >> C;
  result = A * B * C;
  while (result!=0) {
    nums[result%10] += 1;
    result /= 10;
  }
  for (int i=0;i<10;i++)
    cout << nums[i] << endl;
  return 0;
}