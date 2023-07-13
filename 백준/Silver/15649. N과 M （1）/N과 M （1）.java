import java.io.*;
import java.util.*;

public class Main {
	static int N, M;
	static int[] result;
	static boolean[] visited;
    
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		result = new int[M];
		visited = new boolean[N+1];
		recur(0);
		bw.close();	
	}
	
	private static void recur(int depth) throws IOException {
		if (depth == M) {
			printResult();
			return;
		}
		for (int i=1;i<N+1;i++) {
			if (!visited[i]) {
				visited[i] = true;
				result[depth] = i;
				recur(depth+1);
				visited[i] = false;
			}
		}
	}
	
	private static void printResult() throws IOException {
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		for (int i=0;i<M;i++)
			bw.write(result[i]+" ");
		bw.write("\n");
		bw.flush();
	}
}