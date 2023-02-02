#include <stdio.h>

int main(void) {
  int sound[8]={0,}, before, state;
  // ascending, descending, mixed
  for (int i=0;i<8;i++) 
    scanf("%d", &sound[i]);
  for (int j=1;j<8;j++) {
      before = sound[j-1];
      if (before+1==sound[j] && (state==0 || j==1)) 
        state = 0;
      else if (before-1==sound[j] && (state==1 || j==1)) 
        state = 1;
      else {
        state = 2;
        break;
      }
  }
  if (state==0)
    printf("ascending");
  else if (state==1)
    printf("descending");
  else
    printf("mixed");
  return 0;
}