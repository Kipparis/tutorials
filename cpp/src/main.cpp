#include <iostream>

#include <string>
#include <vector>

#include <cctype>
#include <sstream>

using namespace std;

int max(int lhs, int rhs);
int min(int lhs, int rhs);

int main(int argc, const char *argv[])
{

  int first = 20, second = 5;
  int inp;

  cin >> inp;

  // store input in smalles variable
  ((first < second) ? first : second) = inp;
  cout << first << " " << second << endl;

  return 0;

}

int max(int lhs, int rhs) {
  return((lhs < rhs) ? rhs : lhs);
}

int min(int lhs, int rhs) {
  return((lhs > rhs) ? rhs : lhs);
}
