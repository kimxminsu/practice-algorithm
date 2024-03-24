import java.util.List;
import java.util.ArrayList;

class Solution {
    public int[] solution(String[] intStrs, int k, int s, int l) {
        List<Integer> list = new ArrayList<>();
        for (int i=0; i<intStrs.length; i++) {
            int intStrsCut = Integer.parseInt(intStrs[i].substring(s, s + l));
            if (intStrsCut > k) {
                list.add(intStrsCut);
            }
        }
        int[] answer = new int[list.size()];
        for (int i = 0 ; i < list.size() ; i++) 
            answer[i] = list.get(i).intValue();
        return answer;
    }
}