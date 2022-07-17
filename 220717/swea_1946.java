package swea;

import java.util.Scanner;

public class swea_1946 {

	public static void main(String[] args) {
		
		Scanner scan = new Scanner(System.in);
		
		int T = scan.nextInt();
		
		for(int l=1; l<=T; l++) {
			
			int N = scan.nextInt();
			String nameArr[] = new String[N];
			int numArr[] = new int[N];
			
			for(int i=0; i<N; i++) {
				String name = scan.next();
				int num = scan.nextInt();
				
				nameArr[i] = name;
				numArr[i] = num;
			}
			
			int x = 0;
			
			System.out.printf("#%d\n",l);
			
			for(int j=0; j<N; j++) {
				
				for(int k=1; k<=numArr[j]; k++) {
					x++;
					System.out.print(nameArr[j]);
					
					if(x%10 ==0) {
						System.out.println();
					}					
				}
			}
			System.out.println();
		}
	}

}
