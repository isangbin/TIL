package swea;

import java.util.Scanner;

public class swea_1936 {

	public swea_1936() {
		// TODO Auto-generated constructor stub
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int T1;
        int T2;
		T1=sc.nextInt();
        T2=sc.nextInt();
		/*
		   ���� ���� �׽�Ʈ ���̽��� �־����Ƿ�, ������ ó���մϴ�.
		*/

		if(T1==1){
            if(T2==3){
                System.out.println("A");
            }else{
                System.out.println("B");
            }
        }
        else if(T1==2){
            if(T2==1){
                System.out.println("A");
            }else{
                System.out.println("B");
            }
        }else{
            if(T2==2){
                System.out.println("A");
            }else{
                System.out.println("B");
            }

        }
	}

}
