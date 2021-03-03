#include <cstdint>
using namespace std;

extern "C"  // required when using C++ compiler

int64_t fib(int64_t number)
{
    return (number > 2)? fib(number - 1) + fib(number - 2) : 1;
}
