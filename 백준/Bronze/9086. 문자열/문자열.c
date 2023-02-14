#include <stdio.h>
#include <string.h>

int main() {
  int T;
  char string[1000];
  scanf("%d", &T);
  for (int i=0;i<T;i++){
    scanf("%s", string);
    printf("%c%c\n", string[0], string[strlen(string)-1]);
  }
  return 0;
}