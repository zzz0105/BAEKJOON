#include <iostream>
using namespace std;

int main() {
  int N, i;
  cin >> N;
  double scores[N], max_score=0, sum=0.0;
  for (i=0;i<N;i++) {
    cin >> scores[i];
    if (scores[i]>max_score)
      max_score = scores[i];
  }
  for (i=0;i<N;i++) 
    sum += scores[i]*100 / max_score;
  cout << sum/N;
}