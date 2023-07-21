import java.io.*;

public class Main {
	static int N;
	static int[] result;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		N = Integer.parseInt(br.readLine());
		result = new int[N];
		backTracking(0);
	}

	private static void backTracking(int depths) {
		if (depths==N) {
			for (int i=0;i<N;i++)
				System.out.print(result[i]);
			System.exit(0);
		}
		for (int num=1;num<4;num++) {
			result[depths] = num;
			if (isGood(depths))
				backTracking(depths+1);
		}
	}

	private static boolean isGood(int idx) {
		for (int len=1;len<(idx+1)/2+1;len++) {
			int sameLen = 0;
			for (int i=0;i<len;i++) {
				if (result[idx-i]!=result[idx-len-i])
					break;
				sameLen += 1;
			}
			if (sameLen==len)
				return false;
		}		
		return true;
	}
}
