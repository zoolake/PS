class Solution {
    static int answer = 0;
    static int count = 0;
    static char[] alphabet = {'A','E','I','O','U'};

    public int solution(String word) {
        dfs(word, "", 0);
        return answer;
    }

    private void dfs (String target, String temp, int depth) {
        if(temp.equals(target)) {
            answer = count;
            return;
        }

        if(depth == 5) {
            return;
        }

        for(int i=0; i<5; i++) {
            temp += alphabet[i];
            count++;
            dfs(target, temp, depth+1);
            temp = temp.substring(0, depth);
        }
    }
}
