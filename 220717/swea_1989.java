package swea;

import java.util.Scanner;

public class swea_1989 {

	public static void main(String[] args) {
		
		Scanner scan = new Scanner(System.in);
		
		int N = scan.nextInt();
		String voca[] = new String[N];
		
		for(int k=0; k<N; k++) {
			voca[k] = scan.next();
		}
		
		for(int j=0; j<N; j++) {
			
			char split[] = voca[j].toCharArray();		
			int n = split.length;
			int ans = 0;
			
			for(int i=0; i<n; i++) {
				if(split[i] == split[n-1-i]) {
					ans = 1;
				}else {
					ans = 0;
					break;
				}
			}
			
			System.out.printf("#%d %d\n",j+1,ans);
		}
	}
}
