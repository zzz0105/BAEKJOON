#include <stdio.h>

int main(void) {
  int T, score, combo, i, j;
  char quiz[80];
  scanf("%d", &T);
  for (i = 0; i < T; i++) {
    score = 0;
    combo = 1;
    scanf("%s", quiz);
    for (j = 0; quiz[j] != '\0'; j++) {
      if (quiz[j] == 'O') {
        score += combo;
        combo++;
      } else {
        combo = 1;
      }
    }
    printf("%d\n", score);
  }
  return 0;
}