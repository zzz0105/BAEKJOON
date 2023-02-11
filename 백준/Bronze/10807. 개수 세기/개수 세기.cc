#include <iostream>
using namespace std;

int main() {
  int N, i, v, answer = 0;
  cin >> N;
  int nums[N + 1];
  for (i = 0; i < N; i++)
    cin >> nums[i];
  cin >> v;
  for (i = 0; i < N; i++) {
    if (nums[i] == v)
      answer += 1;
  }
  cout << answer;
  return 0;
}