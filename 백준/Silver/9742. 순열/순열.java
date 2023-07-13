import java.io.*;
import java.util.*;

public class Main {
	static int idx, now;
	static String str, answer;
	static char[] result;
	static boolean[] visited;
    
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		String input;
		
		while((input =br.readLine()) != null) {
			StringTokenizer st = new StringTokenizer(input," ");
			if (!st.hasMoreTokens())
				break;
			str = st.nextToken();
			idx = Integer.parseInt(st.nextToken());
			now = 0;
			result = new char[str.length()];
			Arrays.fill(result, ' ');
			visited = new boolean[str.length()];
			answer = "";
			recur(0);
			answer = (answer.isEmpty())?"No permutation":answer;
			bw.write(str + " " + idx + " = " + answer + "\n");
			bw.flush();
		}
        bw.close();
	}

	private static void recur(int depth) {
		if (!answer.isEmpty())
			return;
		if (depth == str.length()) {
			now += 1;
			if (now == idx)
				answer = new String(result);
			return;
		}
		for (int i=0;i<str.length();i++) {
			if (!visited[i]) {
				visited[i] = true;
				result[depth] = str.charAt(i);
				recur(depth+1);
				visited[i] = false;
			}
		}
	}
}