package Java_Study.Practice;

import java.util.Scanner;

//사용자로부터 값을 입력받아 그 값의 대소관계와 얼마나 더 큰지 출력하는 프로그램
public class if_else {
    public static void main(String[] arg){
        Scanner scanner = new Scanner(System.in);

        System.out.printf("a값을 입력해주세요 : ");
        int a = scanner.nextInt();

        System.out.printf("b값을 입력해주세요 : ");
        int b = scanner.nextInt();

        if(a < b){
            System.out.printf("b가 a보다 %d만큼 더 큽니다. \n", b - a);
        } else if(a > b) {
            System.out.printf("a가 b보다 %d만큼 더 큽니다. \n", a - b);
        } else {
            System.out.printf("a와 b가 같습니다. \n");
        }

        if(a % 2 == 0){
            System.out.printf("a는 짝수입니다");
        } else if (b % 2 == 0) {
            System.out.printf("b는 짝수입니다");
        } else if (a % 2 != 0){
            System.out.printf("a는 홀수입니다");
        } else if (b % 2 != 0){
            System.out.printf("b는 홀수입니다");
        }
    }
}
