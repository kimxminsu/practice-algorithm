class Solution {
    public String solution(String my_string, int[][] queries) {
        String answer = "";
        char[] chars = my_string.toCharArray();
        for (int i=0; i<queries.length; i++) {
            for (int j=0; j<(queries[i][1] - queries[i][0] + 1) / 2; j++) {
                char temp = chars[queries[i][0]+j];
                chars[queries[i][0]+j] = chars[queries[i][1]-j];
                chars[queries[i][1]-j] = temp;
            }
        }
        answer = String.valueOf(chars);
        return answer;
    }
}