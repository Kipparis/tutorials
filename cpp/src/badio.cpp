#include <iostream>

using namespace std;

void usage() {
    cout << "the program is reads and stores input into variable of int type" << endl;
    cout << "---" << endl;
    cout << "enter different strings to see" << endl;
    cout << "which IO bits are set" << endl;
}

int main(int argc, char* argv[]) {
    cout << "running..." << endl;
    usage();
    int number;
    cout << "> ";
    cin >> number;
    while (number != -1) {
        // output IO state bits
        cout << "bad bit:\t" << cin.bad()
            << "\nfail bit:\t" << cin.fail()
            << "\neof bit:\t" << cin.eof()
            << "\ngood bit:\t" << cin.good()
            << "\n";
        cout << "readed number:\t" << number << endl;
        // read input
        cout << "> ";
        cin >> number;
    }
}
