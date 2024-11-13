package Java_Study.Practice;

import java.util.Scanner;

//사용자로부터 a까지 입력값을 받아 0부터 a만큼 수를 더하는 연산의 결과를 출력하는 프로그램
public class For2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.printf("1부터 a까지 더하는 연산을 수행합니다. 원하는 a값을 입력하세요 : ");
        int a = scanner.nextInt();
        int sum = 0;

        for(int i = 0;i <= a;i++){
            //~까지 더하고싶다면 +=, ~까지 곱하고싶다면 *= (sum, i 초기값을 0으로하면 0부터 곱해버려 결과가 0이 되버리니 1로 설정해야함)
            sum += i;
        }
        System.out.printf("1부터 %d까지의 합은 " + sum + "입니다.", a);
    }
}
