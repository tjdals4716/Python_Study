package Java_Study.Practice;

import java.util.Scanner;

//사용자로부터 정수를 입력받아 나누기를 수행하는 프로그램 (0으로 나누는 경우 예외 처리)
public class Exception_Test {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        try {
            System.out.printf("정수를 입력해주세요 : ");
            int a = scanner.nextInt();

            System.out.printf("정수를 입력하세요 : ");
            int b = scanner.nextInt();

            int division = a / b;
            System.out.printf("a와 b를 나눈 결과 : " + division);
            //ArithmeticException은 산술 연산에서 발생하는 예외
        } catch (ArithmeticException e){
            System.out.printf("0으로 나눌 수 없습니다");
            //Exception은 모든 종류의 예외를 포괄, 즉 이 코드에서는 ArithmeticException을 제외한 다른 예외가 발생한 것을 처리
        } catch (Exception e){
            System.out.printf("잘못된 입력입니다");
            //finally는 예외 발생 여부와 상관없이 항상 실행
        } finally {
            scanner.close();
        }
    }
}
