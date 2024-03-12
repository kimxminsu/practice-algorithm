class Solution {
    public int[] solution(int[] arr, int[][] queries) {
        int[] answer = {};
        for (int i=0; i<queries.length; i++) {
            int temp = 0;
            int change_one = queries[i][0];
            int change_two = queries[i][1];
            temp = arr[change_one];
            arr[change_one] = arr[change_two];
            arr[change_two] = temp;
        }
        return arr;
    }
}