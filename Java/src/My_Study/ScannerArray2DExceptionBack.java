package My_Study;

import java.util.Scanner;

public class ScannerArray2DExceptionBack {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int a = 0;
        int b = 0;

        while(true){
            System.out.print("행을 입력하세요 (2 ~ 4 사이값 입력) (-1 입력 시 프로그램 종료) : ");
            a = sc.nextInt();

            if (a > 1 && a < 5) {
                break;
            } else if (a == -1) {
                System.out.println("프로그램을 종료합니다");
                return;
            } else {
                System.out.println("행을 다시 입력하세요");
            }
        }

        while(true){
            System.out.print("열을 입력하세요 (2 ~ 4 사이값 입력) (-1 입력 시 이전으로 돌아감) : ");
            b = sc.nextInt();

            if (b > 1 && b < 5) {
                break;
            } else if (b == -1) {
                System.out.println("행 입력으로 돌아갑니다");
            } else {
                System.out.println("열을 다시 입력하세요");
            }
        }

        System.out.print(a * b + "개 정수를 입력하세요 : ");
        int i[][] = new int[a][b];

        for(int row = 0;row < i.length;row++){
            for(int col = 0;col < i[row].length;col++){
                i[row][col] = sc.nextInt();
                int j = i[row][col];
                System.out.print(j + " ");
            }
            System.out.println();
        }
    }
}
