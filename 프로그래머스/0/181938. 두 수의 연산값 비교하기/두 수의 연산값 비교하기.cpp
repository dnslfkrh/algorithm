#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(int a, int b) {
    int answer = 0;
    
    string aPlusB = to_string(a) + to_string(b);
    int ab = 2 * a * b;
    
    if (stoi(aPlusB) >= ab) {
        answer = stoi(aPlusB);
    }
    else {
        answer = ab;
    }
    
    return answer;
}