#include <stdio.h>

int main(void) {
  int x, y, w, h, answer;
  scanf("%d %d %d %d", &x, &y, &w, &h);
  answer = x;
  if (answer > y)
    answer = y;
  if (answer > w-x)
    answer = w-x;
  if (answer > h-y)
    answer = h-y;
  printf("%d", answer);
  return 0;
}