class Solution {
    public String solution(String code) {
        String answer = "";
        int mode = 0;
        for (int i = 0; i < code.length(); i++) {
            if (code.charAt(i) == '1')  {
                mode = 1 - mode;            //0->1 or 1->0
            } else if (i % 2 == mode) {     //mode==0 && idx%2==0 or mode==1 && idx%2==1
                answer += code.charAt(i);
            }
        }
        return answer.equals("") ? "EMPTY" : answer;
    }
}