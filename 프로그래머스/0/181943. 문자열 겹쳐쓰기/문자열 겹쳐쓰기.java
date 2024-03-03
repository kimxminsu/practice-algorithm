class Solution {
    public String solution(String my_string, String overwrite_string, int s) {
        String answer = "";
        char[] myArr = my_string.toCharArray();
        char[] overwriteArr = overwrite_string.toCharArray();
        int idx = 0;
        for (int i=s; i<s+overwriteArr.length; i++) {
            myArr[i] = overwriteArr[idx];
            idx++;
        }
        for (int i=0; i<myArr.length; i++) {
            answer += myArr[i];
        }
        return answer;
    }
}