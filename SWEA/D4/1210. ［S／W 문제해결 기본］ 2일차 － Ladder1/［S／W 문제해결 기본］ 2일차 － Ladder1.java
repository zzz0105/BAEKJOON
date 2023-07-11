import java.io.*;
import java.util.*;

public class Solution {
    public static void main(String[] args) throws IOException {
    	BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    	StringTokenizer st;
    	BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    	for (int t=1;t<11;t++) {
			// 정보 입력하고 지금 위치(2) 저장
    		int tc = Integer.parseInt(br.readLine());
    		int[][] ladder = new int[100][100];
    		int target = -1;
    		for (int r=0;r<100;r++) {
    			st = new StringTokenizer(br.readLine());
    			for (int c=0;c<100;c++) {
    				ladder[r][c] = Integer.parseInt(st.nextToken());
    				if (r==99 && ladder[r][c]==2) {
    					target = c;
    				}
    			}
    		}
    		
    		int now_c = target;
    		for (int r=98;r>-1;r--) {   
    			boolean isMoved = false;
				while (now_c>0 && ladder[r][now_c-1]==1) {	// 좌측에 가로선이 있다면 
					now_c--;
					isMoved = true;
				}	 
				while (!isMoved && now_c<99 && ladder[r][now_c+1]==1) {	// 좌측으로 움직이지 않았고 우측에 가로선이 있다면 
					now_c++;
				}
    		}    		
    		bw.write("#" + tc + " " + now_c + '\n');
    		bw.flush();
    	}
    	bw.close();
    }
}