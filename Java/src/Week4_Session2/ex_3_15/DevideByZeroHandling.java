package Week4_Session2.ex_3_15;

import java.util.Scanner;

public class DevideByZeroHandling {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while(true){
            System.out.print("분모를 입력하세요 : ");
            int dividend = scanner.nextInt();
            System.out.print("분자를 입력하세요 : ");
            int divisor = scanner.nextInt();
            try{
                System.out.println(dividend + " / " + divisor + " = 몫 : " + dividend/divisor);
                break;
            }
            catch(ArithmeticException e){
                System.out.println("0으로 나눌 수 없습니다");
            }
        }
        scanner.close();
    }
}
