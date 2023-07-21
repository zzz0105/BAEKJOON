import java.io.*;
import java.util.*;

public class Solution {
	static boolean[] visited;
	static int[] H;
	static int N, B, min_diff;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int T = Integer.parseInt(br.readLine());
		for (int tc=1;tc<T+1;tc++) {
			st = new StringTokenizer(br.readLine());
			N = Integer.parseInt(st.nextToken());	// 점원 수
			B = Integer.parseInt(st.nextToken());	// 선반 높이
			
			visited = new boolean[N];
			H = new int[N];	// 점원의 키
			st = new StringTokenizer(br.readLine());
			for (int i=0;i<N;i++) 
				H[i] = Integer.parseInt(st.nextToken());
			min_diff = 200000;
			backTracking(0, 0);	// (depth, 선택된 점원들의 키 합)
            
			bw.write("#"+tc+" "+min_diff+"\n");
			bw.flush();
		}
		bw.close();
	}
    
	private static void backTracking(int depth, int sum) {
		if (depth==N) {
			if (sum >= B)
				min_diff = Math.min(min_diff, Math.abs(B-sum));
			return;
		}
		visited[depth] = true;
		backTracking(depth+1, sum+H[depth]);
		visited[depth] = false;
		backTracking(depth+1, sum);	
	}
}