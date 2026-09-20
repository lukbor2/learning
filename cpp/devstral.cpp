#include <iostream>

int main() {
    int num;

    std::cout << "Welcome to my program!\n";
    std::cout << "Please enter an integer: ";

    std::cin >> num;

    std::cout << "You entered: " << num << "\n";
    std::cout << "The square of your number is: " << num * num << "\n";
    std::cout << "The cube of your number is: " << num * num * num << "\n";

    return 0;
}