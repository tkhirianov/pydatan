#include <iostream>
#include <vector>

using namespace std;

int main()
{
    double y = 1/2 + 1/2;
    cout << y << '\n';

    unsigned int x = 9999;
    signed int z = -5;
    if (x > z) {
        cout << "normal\n";
    } else {
        cout << "strange\n";
    }
    unsigned int reveal_z = z;
    cout << reveal_z << '\n';

    return 0;
}
