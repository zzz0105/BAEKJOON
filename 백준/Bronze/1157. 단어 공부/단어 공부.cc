#include <iostream>
using namespace std;

int main() {
  string word;
  int cnt[26] = {0, }, i, answer=0;
  char answerAlpha;
  bool maxOne=true;
  cin >> word;
  for (i=0;i<word.length();i++) {
    word[i] = toupper(word[i]);
    cnt[word[i]-'A'] += 1;
  }
  for (i=0;i<26;i++) {
    if (answer < cnt[i]) {
      answer = cnt[i];
      answerAlpha = i + 65;
      maxOne = true; 
    }
    else if (answer == cnt[i])
        maxOne = false;
  }
  if (maxOne == false)
    cout << '?';
  else 
    cout << answerAlpha;
}