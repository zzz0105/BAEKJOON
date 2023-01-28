#include <stdio.h>

int main(void) {
  int max_value = 0, max_idx, now;
  for (int i=1;i<10;i++) {
    scanf("%d", &now);
    if (now > max_value) {
      max_value = now;
      max_idx = i;
    }
  }
  printf("%d\n%d", max_value, max_idx);
  return 0;
}