package swea;

import java.util.Scanner;

public class swea_2063 {

	public static void main(String[] args) {
		
		Scanner scan = new Scanner(System.in);

		int N = scan.nextInt();
		int arr[] = new int[N];
		
		for(int i=0; i<N; i++) {
			int num = scan.nextInt();
			arr[i] = num;
			
		}
		for(int j=0; j<arr.length-1; j++) {

			for(int i=0; i<arr.length-1-j; i++) {
				if(arr[i]>arr[i+1]) {
					int sort = arr[i];
					arr[i]=arr[i+1];
					arr[i+1] = sort;
				}
			}
		}
		
		System.out.println(arr[N/2]);
	}

}
