package My_Study;

import java.util.Scanner;

public class ScannerArray2D {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a, b = 0;

        System.out.print("행 개수를 입력하세요 : ");
        a = sc.nextInt();
        System.out.print("열 개수를 입력하세요 : ");
        b = sc.nextInt();

        int i[][] = new int[a][b];

        System.out.print("총 " + (a * b) + "개의 정수를 입력하세요 (스패이스로 구분 지을 것) : ");

        for(int row = 0;row < i.length;row++){
            for(int col = 0;col < i[row].length;col++){
                i[row][col] = sc.nextInt();
                System.out.print(i[row][col] + " ");
            }

            // 2차원 행렬 줄발꿈 필수!!
            System.out.println();
        }
    }
}
