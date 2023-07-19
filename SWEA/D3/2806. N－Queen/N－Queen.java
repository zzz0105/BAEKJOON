import java.io.*;

public class Solution {
	static boolean[][] board;
	static int N, answer;
	static int[][] move = new int[][]{{-1,0},{-1,-1},{-1,1}};
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int T = Integer.parseInt(br.readLine());
		
		for (int tc=1;tc<T+1;tc++) {
			N = Integer.parseInt(br.readLine());
			board = new boolean[N][N];
			answer = 0;
			backtracking(0);
			bw.write("#"+tc+" "+answer+"\n");
		}
		bw.flush();
		bw.close();
	}
	
	private static void backtracking(int r) {	// 파라미터: 행 번호(r)
		if (r==N) {
			answer += 1;
			return;
		}
		for (int c=0;c<N;c++) {
			if (check(r,c)) {
				board[r][c] = true;
				backtracking(r+1);
				board[r][c] = false;
			}
		}
	}

	private static boolean check(int r, int c) {	// 이전에 놓았던 퀸이 공격할 수 없으면 true
		for (int d=0;d<move.length;d++) {
			int dr = move[d][0], dc = move[d][1];
			for (int m=1;m<N;m++) {
				int nr = r+dr*m, nc = c+dc*m;
				if (!inRange(nr,nc))
					break;
				if (board[nr][nc])
					return false;
			}
		}
		return true;
	}
	
	private static boolean inRange(int r, int c) {	// r과 c가 보드 범위(0~N-1) 안에 있다면 true 반환
		if ((0<=r)&&(r<N) && (0<=c)&&(c<N))
			return true;
		return false;
	}
}