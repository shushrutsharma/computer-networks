#include<iostream>
using namespace std;

int main ()
{
    int a;
    cout << "enter age : ";
    cin >> a;
    if ( a > 18 ){
        cout << "yay! you are eligible to vote ";

    }
    else {
        cout << "sorry you aren't 18 yet, you can't vote.";
    }
    return 0;
}

