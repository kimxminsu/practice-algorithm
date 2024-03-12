class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = new int[num_list.length + 1];
        for (int i=0; i<num_list.length; i++) {
            answer[i] = num_list[i];
        }
        int len = answer.length;
        if (answer[len-2] > answer[len-3]) {
            answer[len-1] = answer[len-2] - answer[len-3];
        } else {
            answer[len-1] = answer[len-2] * 2;
        }
        return answer;
    }
}