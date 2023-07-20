import java.io.*;
import java.util.*;

public class Main {

	static int N, M;
	static int[][] graph;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		st = new StringTokenizer(br.readLine());
		N = Integer.parseInt(st.nextToken());
		M = Integer.parseInt(st.nextToken());
		
		graph = new int[N][M];
		for (int i=0;i<N;i++) {
			String str = br.readLine();			
			for (int j=0;j<M;j++) {
				graph[i][j] = Integer.parseInt(str.charAt(j)+"");
			}
		}
		
		bw.write(bfs(0,0)+"");
		bw.flush();
		bw.close();
	}

	private static int bfs(int s, int e) {
		int[][] move = {{-1,0},{0,-1},{1,0},{0,1}};
		Queue<Integer> queueI = new LinkedList<Integer>();
		Queue<Integer> queueJ = new LinkedList<Integer>();
		queueI.add(s);
		queueJ.add(e);
		int[][] visited = new int[N][M];
		visited[s][e] = 1;
		while (!queueI.isEmpty() && !queueJ.isEmpty()) {
			int i = queueI.poll();
			int j = queueJ.poll();
			if (i==N-1 && j==M-1)
				return visited[i][j];
			for (int d=0;d<move.length;d++) {
				int ni = i+move[d][0], nj = j+move[d][1];
				if (inRange(ni,nj) && graph[ni][nj]==1 && visited[ni][nj]==0) {
					visited[ni][nj]  = visited[i][j] + 1;
					queueI.add(ni);
					queueJ.add(nj);					
				}
			}
		}
		return -1;
	}

	private static boolean inRange(int ni, int nj) {
		if (0<=ni && ni<N && 0<=nj && nj<M)
			return true;
		return false;
	}
}