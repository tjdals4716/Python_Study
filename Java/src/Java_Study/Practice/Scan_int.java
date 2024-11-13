package Java_Study.Practice;

import java.util.Scanner;

//사용자로부터 두 입력값을 받아 덧셈 결과를 출력하는 프로그램
public class Scan_int {
    public static void main(String[] arg){
        //System.in은 표준 입력 스트림을 사용하여 사용자로부터 입력을 받기 위함
        Scanner scanner = new Scanner(System.in);

        System.out.printf("a를 입력하세요 : ");
        int a = scanner.nextInt();

        System.out.printf("b를 입력하세요 : ");
        int b = scanner.nextInt();

        int sum = a + b;

        System.out.printf("a + b = " + sum);
    }
}
