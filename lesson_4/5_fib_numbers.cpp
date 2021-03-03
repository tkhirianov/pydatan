#include <iostream>
#include <vector>
using namespace std;

int64_t final_fibonacci_number = 40;

int64_t fib(int64_t number)
{
    return (number > 2)? fib(number - 1) + fib(number - 2) : 1;
}

int main()
{
    vector<int64_t> tasks;
    for(int i = 0; i < final_fibonacci_number + 1; i++)
        tasks.push_back(i);
    vector<int64_t> answers;
    for(int i = 0; i < final_fibonacci_number + 1; i++)
        answers.push_back(fib(tasks[i]));
    for(auto answer: answers) {
        cout << answer << ' ';
    }
    cout << endl;

    return 0;
}
