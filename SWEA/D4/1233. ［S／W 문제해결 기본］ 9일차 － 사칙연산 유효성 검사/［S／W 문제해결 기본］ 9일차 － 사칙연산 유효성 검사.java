import java.io.*;
import java.util.*;

public class Solution {	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		
		for (int tc=1;tc<11;tc++) {
			int answer = 1;	// 계산이 가능하다고 가정
			int N = Integer.parseInt(br.readLine());
			for (int i=1;i<N+1;i++) {
				st = new StringTokenizer(br.readLine());
				int v = Integer.parseInt(st.nextToken());
				String value = st.nextToken();
				if ((isOperator(value) && !st.hasMoreTokens()) || (!isOperator(value) && st.hasMoreTokens()))	// 본인이 연산자인데 자식이 없거나, 본인이 연산자가 아닌 숫자인데 자식이 있다면 계산이 불가능하다
					answer = 0;
			}
			bw.write("#"+tc+" "+answer+"\n");
			bw.flush();
		}
		bw.close();
	}

	private static boolean isOperator(String value) {	// 연산자인지 판단해준다
		String[] operators = {"+","-","*","/"};
		for (String operator : operators)
			if (operator.equals(value))	// ==는 주소값을 비교하고 equals는 내용을 비교한다!
				return true;
		return false;
	}	
}