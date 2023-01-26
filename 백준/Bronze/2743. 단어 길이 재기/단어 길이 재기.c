#include <stdio.h>

int main(void) {
  char word[100];
  int len = 0;
  scanf("%s", word);
  for (int i=0;word[i]!='\0';i++) {
    len++;
  }
  printf("%d", len);
  return 0;
}