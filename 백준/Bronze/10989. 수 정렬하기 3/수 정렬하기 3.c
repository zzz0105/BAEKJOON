#include <stdio.h>

int main(void) {
  int N, num, i, j;
  scanf("%d", &N);
  int count[10001] = {0, };
  for (i=0;i<N;i++) {
    scanf("%d", &num);
    count[num] += 1;
  }
  for (i=0;i<10001;i++) {
    for (j=0;j<count[i];j++)
      printf("%d\n", i);
  }
  return 0;
}