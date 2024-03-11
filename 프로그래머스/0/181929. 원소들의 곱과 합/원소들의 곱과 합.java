class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        int product = 1;
        int sum = 0;
        for (int i=0; i<num_list.length; i++) {
            product *= num_list[i];
            sum += num_list[i];
        }
        if (product < sum*sum) {
            answer = 1;
        }
        return answer;
    }
}