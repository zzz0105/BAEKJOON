#include <iostream>
#include <cmath>
using namespace std;

int main() {
  string colors[10] = {"black","brown","red","orange","yellow","green", "blue","violet","grey","white"}, now;
  int value[3], i, j;
  for (i=0;i<3;i++) {
    cin >> now;
    for (j=0;j<10;j++) {
      if (now==colors[j]) {
        value[i] = j;
        break;
      }
    }
  }
  cout << value[0]*10 + value[1];
  if (value[0]*10 + value[1]!=0) {
    for (i=0;i<value[2];i++) 
      cout << 0; 
  }
}