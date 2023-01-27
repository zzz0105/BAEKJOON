#include <stdio.h>

long long At(long long A, long long B) {
  return (A+B)*(A-B);
}

int main(void) {
  long long A, B;
  scanf("%lld %lld", &A, &B);
  printf("%lld", At(A, B));
  return 0;
}
