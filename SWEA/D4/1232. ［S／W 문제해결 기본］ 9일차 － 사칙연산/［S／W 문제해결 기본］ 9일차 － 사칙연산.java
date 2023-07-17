import java.io.*;
import java.util.*;

public class Solution {	
	static class Node {
		String value;	// 노드값
		int left, right;	// 자식노드번호
		
		public Node(String value, int left, int right) {
			super();
			this.value = value;	// 숫자 혹은 연산자
			this.left = left;
			this.right = right;
		}
		public Node(String value) {
			this.value = value;
		}
	}
	static int N;	// 노드 개수
	static int result;	// 계산 결과
	static String[] operators = {"+","-","*","/"};
	static Node[] nodes;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		
		for (int tc=1;tc<11;tc++) {
			N = Integer.parseInt(br.readLine());
			nodes = new Node[N+1];
			for (int i=1;i<N+1;i++) {
				st = new StringTokenizer(br.readLine());
				int v = Integer.parseInt(st.nextToken());
				String value = st.nextToken();
				if (st.hasMoreTokens()) {
					int left = Integer.parseInt(st.nextToken());
					int right = Integer.parseInt(st.nextToken());
					nodes[v] = new Node(value,left,right);					
				} else {
					nodes[v] = new Node(value);	
				}
			}
			
			result = calc(nodes[1]);	// 노드의 주소값이 넘어간다. 타입: 노드. 루트 정점 번호 1
			bw.write("#"+tc+" "+result+"\n");
			bw.flush();
		}
		bw.close();
	}

	private static int calc(Node node) {
		String val = node.value;
		switch (val) {
			case "+":
				return calc(nodes[node.left]) + calc(nodes[node.right]); 
			case "-":
				return calc(nodes[node.left]) - calc(nodes[node.right]);
			case "*":
				return calc(nodes[node.left]) * calc(nodes[node.right]);
			case "/":
				return calc(nodes[node.left]) / calc(nodes[node.right]);
			default:
				return Integer.parseInt(node.value);
		}
	}
}