# include <stdio.h>

int main(void) {
  // 배열 길이는 상수로 설정해야함
  int A[100][100];
  int B[100][100];
  int N, M, i, j;
  scanf("%d %d", &N, &M);
  for (i=0;i<N;i++) {
    for (j=0;j<M;j++) {
      scanf("%d", &A[i][j]);
    }
  }
  for (i=0;i<N;i++) {
    for (j=0;j<M;j++) {
      scanf("%d", &B[i][j]);
    }
  }
  for (i=0;i<N;i++) {
    for (j=0;j<M;j++) {
      printf("%d ", A[i][j]+B[i][j]);
    }
    printf("\n");
  }  
  return 0;
}