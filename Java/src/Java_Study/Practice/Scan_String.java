package Java_Study.Practice;

import java.util.Scanner;

//사용자로부터 값을 입력받아 이름과 나이를 출력하는 프로그램
public class Scan_String {
    public static void main(String[] arg){
        //표준 입력 스트림을 사용하여 Scanner 객체를 생성
        Scanner scanner = new Scanner(System.in);

        System.out.printf("이름을 입력하세요 : ");
        String name = scanner.nextLine();

        System.out.printf("나이를 입력하세요 : ");
        int age = scanner.nextInt();

        System.out.printf("안녕하세요 " + name + "님! \n" + "당신의 나이는 " + age + "세 입니다!");
    }
}
