import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] solution(int n) {
        List<Integer> list = new ArrayList<>();
        while (n != 1) {
            list.add(n);
            n = (n % 2 == 0) ? n / 2 : 3 * n + 1;
        }
        list.add(n);    //1
        
        int[] answer = new int[list.size()];
        for (int i=0; i<list.size(); i++) {
            answer[i] = list.get(i).intValue();
        }
        return answer;
    }
}