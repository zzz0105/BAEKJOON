#include <stdio.h>

int main(void) {
  int A, B;
  // scanf 함수는 입력의 개수를 반환한다
  while (scanf("%d %d", &A, &B)==2) {  
    printf("%d\n", A+B);
  }
  return 0;
}