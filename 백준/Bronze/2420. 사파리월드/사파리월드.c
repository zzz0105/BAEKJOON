# include <stdio.h>

int main(void) {
  long N, M, abs;
  scanf("%ld %ld", &N, &M);
  abs = N - M;
  if (abs >= 0) {
    printf("%ld", abs);
  } else {
    printf("%ld", -abs);
  }
  return 0;
}