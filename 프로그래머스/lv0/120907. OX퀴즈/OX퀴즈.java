import java.util.*;

class Solution {
    public String[] solution(String[] quiz) {
        String[] answer = new String[quiz.length];
        Arrays.fill(answer, "X");
        
        for (int i=0;i<quiz.length;i++) {
            String[] q = quiz[i].split(" ");
            int X = Integer.parseInt(q[0]);
            int Y = Integer.parseInt(q[2]);
            int Z = Integer.parseInt(q[4]);  

            if ((q[1].equals("+") && X+Y==Z) || (q[1].equals("-") && X-Y==Z))
                answer[i] = "O";
        }
        return answer;
    }
}