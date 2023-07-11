import java.io.*;
import java.util.*;

public class Main {
	public static void main (String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	StringTokenizer st;
    	BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		int N = Integer.parseInt(br.readLine());
		
		int start = 1, end = 1, sum = 1, cnt = 0;	// 한 줄에 여러 변수 선언 및 할당하기
		while (start<=end) {
			if (sum == N) {
				cnt++;
			}
			if (sum > N) {
				sum -= start;
				start++;
			} else if (sum <= N) {
				end++;
				sum += end;
			}
		}
		bw.write(cnt+"");
		bw.flush();
		bw.close();
	}
}