#include <stdio.h>

int main(void) {
  int N, sum=0;
  scanf("%d", &N);
  char num[N];
  scanf("%s", num);
  for (int i=0;i<N;i++) {
    sum += num[i] - '0';
    // 아스키코드 활용
  }
  printf("%d", sum);
  return 0;
}