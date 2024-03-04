class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        int ab = 0;
        ab = Integer.parseInt("" + a + b);
        if (ab < 2 * a * b) {
            answer = 2 * a * b;
        } else {
            answer = ab;
        }
        return answer;
    }
}