#include <iostream>
#include <string>
#include <vector>

using namespace std;

int solution(vector<int> num_list) {
    int answer = 0;
    int size = num_list.size();
    
    int a = 1;
    int b = 0;
    int c = 0;
    
    for (int i = 0; i < size; i++) {
        a *= num_list[i];
        b += num_list[i];
    }
    
    c = b * b;
    
    cout << a << endl;
    cout << c << endl;
    
    if (a < c) {
        answer = 1;
    } else {
        answer = 0;
    }
    
    return answer;
}