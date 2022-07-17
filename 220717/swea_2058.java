package swea;

import java.util.Scanner;

public class swea_2058 {

	public static void main(String[] args) {
		
		Scanner scan = new Scanner(System.in);
		
		int num = scan.nextInt();
		
		int a = num/1000;
		num = num - a*1000;
		
		int b = num/100;
		num = num - b*100;
		
		int c = num/10;
		num = num - c*10;
		
		int d = num;
		
		int sum = a+b+c+d;
		System.out.println(sum);
		
	}

}
