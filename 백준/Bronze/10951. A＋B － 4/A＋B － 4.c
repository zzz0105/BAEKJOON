#include <stdio.h>

int main(void) {
  int A, B;
  // EOF: 입력이 없을 때 파일을 종료하기 위해 사용됨
  while (scanf("%d %d", &A, &B)!=EOF) {  
    printf("%d\n", A+B);
  }
  return 0;
}