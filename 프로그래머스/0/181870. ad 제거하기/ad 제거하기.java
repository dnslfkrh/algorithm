import java.util.ArrayList;
import java.util.List;

class Solution {
    public String[] solution(String[] strArr) {
        List<String> list = new ArrayList<>();
        
        for (int i = 0; i < strArr.length; i++) {
            if (!strArr[i].toLowerCase().contains("ad")) {
                list.add(strArr[i]);
            }
        }
        
        return list.toArray(new String[0]);
        // 리스트.toArray(new String[0]) 리스트를 배열로 변환. 공식처럼 쓰기?
    }
}
