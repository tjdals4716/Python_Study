package Java_Study.Day7_Study;

import java.util.Scanner;

//사용자로부터 문자를 입력받아 그 문자를 나열한 결과를 출력하는 프로그램
public class Study2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        //결과 문자열을 저장할 StringBuilder 객체를 생성
        StringBuilder builder = new StringBuilder();

        while(true){
            System.out.printf("문자를 입력하세요 (종료하려면 -1을 입력) : ");
            String a = scanner.nextLine();

            //문자열일때는 정수와 다르게 아래 구문인 동등관계를 사용 => "==" 연산자는 객체의 참조를 비교, "equals" 메서드는 객체의 값을 비교
            if(a.equals("-1")){
                break;
            }
            //입력한 문자를 결과 문자열에 추가
            builder.append(a);
        }
        //StringBuilder 클래스의 toString() 메서드를 호출하는 이유는 StringBuilder 객체에 저장된 문자열을 String 형식으로 변환하기 위해서 사용
        System.out.printf("입력한 문자열의 나열 결과 : " + builder.toString());
        scanner.close();
    }
}
