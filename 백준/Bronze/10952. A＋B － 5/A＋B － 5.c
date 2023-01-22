# include <stdio.h>
// true나 false를 쓰기 위해서는 stdbool.h 헤더 파일이 필요하다

int main(void) {
  int A, B;
  while (1) {
    scanf("%d %d", &A, &B);
    if (A==0 && B==0) {
      break;
    }
    printf("%d\n", A+B);
  }
  return 0;
}