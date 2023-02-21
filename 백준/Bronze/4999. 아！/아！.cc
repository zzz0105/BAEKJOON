#include <iostream>
using namespace std;
#include <string>

int main() {
  string longSound, doctor;
  cin >> longSound;
  cin >> doctor;
  
  if (longSound.find(doctor)==-1)
    cout << "no";
  else  
    cout << "go";
}