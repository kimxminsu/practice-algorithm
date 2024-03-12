class Solution {
    public String solution(int[] numLog) {
        String answer = "";
        for (int i=1; i<numLog.length; i++) {
            int value = numLog[i] - numLog[i-1];
            if (value == 1) {
                answer += "w";
            } else if (value == -1) {
                answer += "s";
            } else if (value == 10) {
                answer += "d";
            } else if (value == -10) {
                answer += "a";
            }
        }
        return answer;
    }
}