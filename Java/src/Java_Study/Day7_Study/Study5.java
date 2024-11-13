package Java_Study.Day7_Study;

import java.util.Scanner;

//계산기 심화1 - 사용자로부터 두 숫자와 연산자를 입력받아 계산 결과를 출력하는데 값을 잘 못 입력한다면 되돌리는 프로그램
public class Study5 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = 0;
        int b = 0;
        char operator;
        boolean vaildInput;
        double result = 0;

        while (true) {
            System.out.printf("첫 번째 값을 입력하세요 : ");
            String input1 = sc.next();
            System.out.printf("두 번째 값을 입력하세요 : ");
            String input2 = sc.next();

            if (isInteger(input1) && isInteger(input2)) {
                a = Integer.parseInt(input1);
                b = Integer.parseInt(input2);
                break;
            } else {
                System.out.println("옳바른 정수가 입력되지 않았습니다. 정수를 다시 입력하세요");
            }
        }

        while(true) {
            System.out.printf("연산할 연산자를 작성하세요 (+, -, *, /) : ");
            operator = sc.next().charAt(0);

            if(operator == '+' || operator == '-' || operator == '*' || operator == '/'){
                break;
            } else{
                System.out.println("옳바른 연산자가 아닙니다. 연산자를 다시 입력하세요");
            }
        }

        //b값이 0이라면 다시 값을 입력하도록 하는 구문
        while (true) {
            if (operator == '/' && b == 0) {
                System.out.printf("0으로 나눌 수 없습니다. 두 번째 값을 다시 입력하세요 : ");
                String input2 = sc.next();
                if (isInteger(input2)) {
                    b = Integer.parseInt(input2);
                } else {
                    System.out.println("올바른 정수가 입력되지 않았습니다. 정수를 다시 입력하세요");
                }
            } else {
                break;
            }
        }

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
                result = a / b;
                break;
        }
        System.out.printf("연산 결과 : " + result);
        sc.close();
    }

    //입력값이 정수인지 확인하는 메서드
    public static boolean isInteger(String input){
        try{
            Integer.parseInt(input);
        } catch (NumberFormatException e){
            return false;
        }
        return true;
    }
}
