import java.io.*;
import java.util.*;

public class Main {
  public static void main(String[] args) throws Exception {
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    StringTokenizer st = new StringTokenizer(br.readLine());
    int N = Integer.parseInt(st.nextToken());
    int M = Integer.parseInt(st.nextToken());

    st = new StringTokenizer(br.readLine());
    long[] S = new long[N+1];
    long[] cnt = new long[M];
    // (a-b)%m = a%m-b%m
    for (int i=1;i<N+1;i++) {
      S[i] = (S[i-1] + Integer.parseInt(st.nextToken()))%M;
      cnt[(int)S[i]]++;
    }

    long answer = cnt[0];  // 구간합이 이미 M으로 나누어떨어지는 경우를 초기값으로 지정
    for (int i=0;i<M;i++) // 나머지 값이 같은 인덱스 중 2개를 뽑는다 (nC2)
      answer += cnt[i]*(cnt[i]-1)/2;
    
    bw.write(answer+"");
    bw.flush();
    bw.close();
  }
}