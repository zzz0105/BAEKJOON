# include <stdio.h>

int main(void) {
  long long a, b, c;
  // 입력범위 주의!
  scanf("%lld %lld %lld", &a, &b, &c);
  printf("%lld", a+b+c);
  return 0;
}