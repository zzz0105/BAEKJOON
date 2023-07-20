import java.io.*;
import java.util.*;

public class Main {
	static int[] rep;
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st;
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		
		st = new StringTokenizer(br.readLine());
		int n = Integer.parseInt(st.nextToken());
		int m = Integer.parseInt(st.nextToken());
		
		rep = new int[n+1];
		for (int i=0;i<n+1;i++)
			rep[i] = i;
		
		for (int i=0;i<m;i++) {
			st = new StringTokenizer(br.readLine());
			int opr = Integer.parseInt(st.nextToken());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());
			
			if (opr==0)	// 0: union
				union(a,b);
			else 		// 1: find
				bw.write(check(a,b)? "YES\n":"NO\n");
			bw.flush();
		}
		bw.close();
	}

	private static void union(int a, int b) {
		a = find(a);
		b = find(b);				
		if (a!=b)
			rep[b] = a;
	}

	private static int find(int a) {
		if (a==rep[a])
			return a;
		return rep[a] = find(rep[a]);
	}
	
	private static boolean check(int a, int b) {
		if (find(a) == find(b))
			return true;
		return false;
	}
}