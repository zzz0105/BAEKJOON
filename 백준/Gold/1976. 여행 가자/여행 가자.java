import java.io.*;
import java.util.*;

public class Main {
	static int[] rep;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		int N = Integer.parseInt(br.readLine());	// 도시의 개수
		int M = Integer.parseInt(br.readLine());	// 여행 계획에 속한 도시들의 수
		
		rep = new int[N+1];
		for (int i=1;i<N+1;i++) // 초기화
			rep[i] = i;
		
		for (int i=1;i<N+1;i++) {
			st = new StringTokenizer(br.readLine());
			for (int j=1;j<N+1;j++) {
				if (Integer.parseInt(st.nextToken()) == 1)	// i번과 j번 도시가 연결되어 있다면 union
					union(i,j);
			}
		}
		
		String answer = "YES";
		st = new StringTokenizer(br.readLine());
		int start = find(Integer.parseInt(st.nextToken())); 		// 출발지의 대표 노드
		for (int i=1;i<M;i++) {
			if (start != find(Integer.parseInt(st.nextToken()))) {	// 출발지의 대표 노드와 연결되어있는지 확인한다
				answer = "NO";
				break;
			}
		}
		bw.write(answer);
		bw.flush();
		bw.close();
	}

	private static void union(int i, int j) {
		i = find(i);
		j = find(j);
		if (i!=j)
			rep[j] = i;		
	}
	
	private static int find(int i) {
		if (i == rep[i])
			return i;
		return rep[i] = find(rep[i]);
	}
}