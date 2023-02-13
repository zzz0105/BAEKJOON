#include <stdio.h>

int main() {
  char names[100];
  int i, order[26];
  for (i=0;i<26;i++) 
    order[i] = -1;
  scanf("%s", names);
  for (i=0;names[i]!='\0';i++) {
    if (order[names[i]-'a']==-1)
      order[names[i]-'a']=i;
  }
  for (i=0;i<26;i++)
    printf("%d ",order[i]);
}