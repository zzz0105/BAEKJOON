#include <stdio.h>

int main(void) {
  int T, R, len;
  char S[21];
  scanf("%d", &T);
  for (int i=0;i<T;i++) {
    len = 0;
    scanf("%d %s", &R, S);
    for (int p=0;S[p]!='\0';p++)
      len++;
    for (int j=0;j<len;j++) {
      for (int k=0;k<R;k++)
        printf("%c", S[j]);
    }    
    printf("\n");
  } 
  return 0;
}