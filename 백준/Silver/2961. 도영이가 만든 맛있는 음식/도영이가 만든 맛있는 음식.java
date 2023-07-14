import java.util.*;
import java.io.*;

public class Main {
	static int N, min_taste;
	static int[] sour, bitter;
	static boolean[] visited;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		N = Integer.parseInt(st.nextToken());
		min_taste = 1000000000;
		sour = new int[N];
		bitter = new int[N];
		visited = new boolean[N];
		
		for (int i=0;i<N;i++) {
			st = new StringTokenizer(br.readLine());
			sour[i] = Integer.parseInt(st.nextToken());
			bitter[i] = Integer.parseInt(st.nextToken());
		}
		bitmask();
		bw.write(min_taste+"");
		bw.flush();
		bw.close();
	}

	private static void bitmask() {
		boolean noChoice = true;
		for (int i=0;i < 1<<N;i++) {
			for (int j=0;j < N;j++) {
				if ((i & 1 << j) != 0) {
					visited[j] = true;
					noChoice = false;
				}
			}
			if (!noChoice)
				makeFood();
			visited = new boolean[N];
		}
	}

	private static void makeFood() {
		int taste_s = 1;
		int taste_b = 0;
		for (int i=0;i<N;i++) {
			if (visited[i]) {
				taste_s *= sour[i];
				taste_b += bitter[i];
			}
		}
		int taste = taste_s-taste_b;
		min_taste = Math.min(min_taste, (taste<0)? taste*(-1) : taste);
	}
}