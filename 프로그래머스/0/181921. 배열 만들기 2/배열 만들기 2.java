import java.util.List;
import java.util.ArrayList;

class Solution {
    public int[] solution(int l, int r) {
        List<Integer> list = new ArrayList<>();
        for (int i=1; Integer.parseInt(Integer.toBinaryString(i)) * 5 <= r; i++) {
            int value = Integer.parseInt(Integer.toBinaryString(i)) * 5;
            if (value >= l) list.add(value);
        }
        int[] answer = (list.size() > 0) ? new int[list.size()] : new int[]{-1};
        for (int i=0; i<list.size(); i++) {
            answer[i] = list.get(i).intValue();
        }
        return answer;
    }
}