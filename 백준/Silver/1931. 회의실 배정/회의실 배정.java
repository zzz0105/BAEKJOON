import java.io.*;
import java.util.*;

public class Main {

	static class Meeting {
		int start, end;	// 시작시간, 종료시간
		
		public Meeting(int start, int end) {
			this.start = start;
			this.end = end;
		}	
	}
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		StringTokenizer st;
		
		int N = Integer.parseInt(br.readLine());
		Meeting[] meetings = new Meeting[N];
		for (int i=0;i<N;i++) {
			st = new StringTokenizer(br.readLine());
			int start = Integer.parseInt(st.nextToken());
			int end = Integer.parseInt(st.nextToken());
			meetings[i] = new Meeting(start,end);
		}
		
		Arrays.sort(meetings, (m1,m2) -> {return Integer.compare(m1.start,m2.start);});
		Arrays.sort(meetings, (m1,m2) -> {return Integer.compare(m1.end,m2.end);});
		// 종료 시간 순으로 정렬하되 종료시간이 같은 경우 시작 시간 순으로 정렬
		
		int now = 0, answer = 0;
		for (int i=0;i<N;i++) {
			if (now <= meetings[i].start) {
				now = meetings[i].end;
				answer += 1;
			}
		}
        
		bw.write(answer+"");
		bw.flush();
		bw.close();
	}
}