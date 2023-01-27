#include <stdio.h>

long long At(int A, int B) {
  return (A+B)*(A-B);
}

int main(void) {
  int A, B;
  scanf("%d %d", &A, &B);
  printf("%lld", At(A, B));
  return 0;
}