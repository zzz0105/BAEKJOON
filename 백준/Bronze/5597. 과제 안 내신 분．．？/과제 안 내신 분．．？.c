# include <stdio.h>

int main(void) {
  int s, flag = 2;
  int student[31] = {0, };
  // 배열의 요소를 모두 0으로 초기화
  for (int i=1;i<=28;i++) {
    scanf("%d", &s);
    student[s] = 1;
  }
  for (int i=1;i<=30;i++) {
    if (student[i]==0) {
      printf("%d\n", i);
      flag -= 1;
    }
    if (flag == 0) break;      
  }
  return 0;
}