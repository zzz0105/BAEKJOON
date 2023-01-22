# include <stdio.h>

int main(void) {
  int N, answer = 1;
  scanf("%d", &N);
  for (int i=2;i<=N;i++) {
    answer *= i;
  }
  printf("%d", answer);
  return 0;
}