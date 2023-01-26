#include <stdio.h>
#include <string.h>

int main(void) {
  char word[100];
  scanf("%s", word);
  int len = strlen(word);
  printf("%d", len);
  return 0;
}