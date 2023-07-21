import java.io.*;
import java.util.*;

class Node implements Comparable<Node> {
	int from, to, cost;
	
	public Node(int from, int to, int cost) {
		this.from = from;
		this.to = to;
		this.cost = cost;
	}

	@Override
	public int compareTo(Node o) {
		return this.cost - o.cost;
	}
}

public class Main {	
	static int[] parent;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		st = new StringTokenizer(br.readLine());
		int V = Integer.parseInt(st.nextToken());
		int E = Integer.parseInt(st.nextToken());
		parent = new int[V+1];
		for (int i=1;i<V+1;i++)
			parent[i] = i;
		
		Queue<Node> pq = new PriorityQueue<>();
		for (int i=0;i<E;i++) {	// A번 정점과 B번 정점이 가중치 C인 간선으로 연결되어 있다
			st = new StringTokenizer(br.readLine());
			int A = Integer.parseInt(st.nextToken());
			int B = Integer.parseInt(st.nextToken());
			int C = Integer.parseInt(st.nextToken());
			pq.add(new Node(A,B,C));
		}
		
		int total = 0, cnt = 0;
		while (!pq.isEmpty()) {
			Node node = pq.poll();
			int na = find(node.from);
			int nb = find(node.to);
			
			if (find(na)!=find(nb)) {
				total += node.cost;
				union(na,nb);
				cnt += 1;
			}
		}
        
		bw.write(total+"");
		bw.flush();
		bw.close();
	}

	private static void union(int a, int b) {
		a = find(a);
		b = find(b);
		if (a != b)
			parent[b] = a;		
	}
	
	private static int find(int a) {
		if (a==parent[a])
			return a;
		return parent[a] = find(parent[a]);		
	}
}