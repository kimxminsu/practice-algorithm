class Solution {
    public int solution(int n, String control) {
        int answer = n;
        for (int i = 0; i < control.length(); i++) {
            int value = control.charAt(i);
            if (value == 'w')  {
                answer++;
            } else if (value == 's')  {
                answer--;
            } else if (value == 'd')  {
                answer += 10;
            } else if (value == 'a')  {
                answer -= 10;
            }
        }
        return answer;
    }
}