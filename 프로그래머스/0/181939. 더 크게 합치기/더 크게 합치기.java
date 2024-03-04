class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        int a_b = 0;
        int b_a = 0;
        a_b = Integer.parseInt("" + a + b);
        b_a = Integer.parseInt("" + b + a);
        if (a_b < b_a) {
            answer = b_a;
        } else {
            answer = a_b;
        }
        return answer;
    }
}