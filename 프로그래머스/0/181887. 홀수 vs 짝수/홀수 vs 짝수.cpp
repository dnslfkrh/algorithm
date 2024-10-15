#include <string>
#include <vector>
#include <iostream>

using namespace std;

int solution(vector<int> num_list) {
    int answer = 0;
    int oddSum = 0;
    int evenSum = 0;
    
    for (int i = 0; i < num_list.size(); i++) {
        
        if ((i + 1) % 2 == 0) {
            evenSum += num_list[i];
        } else {
            oddSum += num_list[i];
        }
        
    }
    
    cout << evenSum << endl;
    cout << oddSum << endl;
    
    if (evenSum > oddSum) {
        answer = evenSum;
    } else if (evenSum < oddSum) {
        answer = oddSum;
    } else {
        answer = oddSum;
    }
    
    return answer;
}