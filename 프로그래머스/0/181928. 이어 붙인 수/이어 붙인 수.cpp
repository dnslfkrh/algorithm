#include <string>
#include <vector>

using namespace std;

int solution(vector<int> num_list) {
    int answer = 0;
    int size = num_list.size();
    string odd = "";
    string even = "";
    
    for (int i = 0; i < size; i++) {
        
        if (num_list[i] % 2 == 0) {
            // 짝수면
            even += to_string(num_list[i]);
        } else {
            // 홀수면
            odd += to_string(num_list[i]);
        }
        
    }
    
    answer = stoi(even) + stoi(odd);
    
    return answer;
}