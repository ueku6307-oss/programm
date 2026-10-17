#include <iostream>
using namespace std;

int main() {
    long long P;
    cin >> P;

    // Периметр квадрата P = 4a, значит a = P / 4.
    // По условию сторона — натуральное число, т.е. P делится на 4 нацело.
    long long a = P / 4;
    long long S = a * a;  // до (2.5e8)^2 = 6.25e16 — нужен 64-битный тип

    cout << S << endl;
    return 0;
}
