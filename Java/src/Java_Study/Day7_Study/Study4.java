package Java_Study.Day7_Study;

import java.util.Scanner;

//사용자로부터 두 숫자와 연산자를 입력받아 계산 결과를 출력하는 프로그램
public class Study4 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int a, b;

        System.out.printf("첫 번째 값을 입력하세요 : ");
        a = scanner.nextInt();

        System.out.printf("두 번째 값을 입력하세요 : ");
        b = scanner.nextInt();

        System.out.println("연산을 수행할 연산자를 선택하세요 (+, -, *, /): ");
        //연산자도 문자이니 char 타입 사용
        //scanner.next().charAt(0)는 사용자가 입력한 문자열의 첫 번째 문자를 가져오는 방법 => charAt(1)은 두 번째, charAt(2)는 세 번째 ...
        //즉 전체적으로 봤을 때 사용자가 입력한 연산자를 단일 문자로 읽어오는 역할을 함
        char operator = scanner.next().charAt(0);

        //int로 하면 정수를 출력, double로 하면 실수를 출력 => 출력 값이 5라면 int는 5를 출력하고 double은 5.0를 출력함
        double result;
        switch (operator){
            case '+':
                result = a + b;
                break;
            case '-':
                result = a - b;
                break;
            case '*':
                result = a * b;
                break;
            case '/':
                if(b != 0) {
                    result = a / b;
                } else {
                    System.out.printf("0으로 나눌 수 없습니다");
                    scanner.close();
                    return;
                }
                break;
            default:
                System.out.println("잘못된 연산자 입니다");
                scanner.close();
                return;
        }
        System.out.println("계산 결과 : " + result);
        scanner.close();
    }
}
