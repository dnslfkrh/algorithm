#include <string>
#include <vector>
#include <iostream>

using namespace std;

string solution(string n_str) {
    string answer = "";
    
    int size = n_str.size();
    int i = 0;
    
    while (i < size && n_str[i] == '0') {
        i++;
    }

    cout << i << endl;
    
    for (i; i < size; i++) {
        answer += n_str[i];
    }

    return answer;
}