#include <iostream>
using namespace std;

int main() {
  int input, square_sum=0;
  for (int i = 0; i < 5; i++) {
    cin >> input;
    square_sum += input * input;
  }
  cout << square_sum % 10;
}