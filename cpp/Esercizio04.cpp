/*
Testo esercizio.
Write a program in cpp using the active file to solve this problem:
I have a number N of temperature recordings.
I want to find the max temperature and write a message back to the user.
*/

#include <iostream>
#include <climits>

using namespace std;

int main() {
    int N;
    cout << "Enter the number of temperature recordings: ";
    cin >> N;

    double max_temp = INT_MIN;
    double temp;

    cout << "Enter " << N << " temperature values:" << endl;
    for (int i = 0; i < N; ++i) {
        cout << "Temperature #" << (i+1) << ":" << endl;
        cin >> temp;
        if (temp > max_temp) {
            max_temp = temp;
        }
    }

    cout << "The maximum temperature recorded was: " << max_temp << "°C" << endl;

    return 0;
}