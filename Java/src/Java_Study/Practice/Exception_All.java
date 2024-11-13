package Java_Study.Practice;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.util.InputMismatchException;
import java.util.Scanner;

//Exception 관련 코드 모음
public class Exception_All {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        try {
            //정수 입력
            System.out.print("첫 번째 정수를 입력해주세요: ");
            int a = scanner.nextInt();

            System.out.print("두 번째 정수를 입력해주세요: ");
            int b = scanner.nextInt();

            //나누기 연산
            int division = a / b;
            System.out.printf("a와 b를 나눈 결과: %d\n", division);

            //배열 예제
            int[] array = new int[5];
            System.out.print("배열의 인덱스를 입력해주세요 (0-4): ");
            int index = scanner.nextInt();
            array[index] = 100; // 인덱스가 잘못될 경우 예외 발생
            System.out.printf("배열의 %d번째 요소에 100을 저장했습니다.\n", index);

            //파일 읽기
            System.out.print("파일 이름을 입력하세요: ");
            String filename = scanner.next();
            File file = new File(filename);
            FileInputStream fileInputStream = new FileInputStream(file);
            int data;
            while ((data = fileInputStream.read()) != -1) {
                System.out.print((char) data);
            }
            fileInputStream.close();

            //데이터베이스 연결 (예시로 SQLite 사용)
            try {
                Connection connection = DriverManager.getConnection("jdbc:sqlite:sample.db");
                //데이터베이스 작업 수행
                connection.close();
            } catch (SQLException e) {
                throw new SQLException("데이터베이스 연결 오류: " + e.getMessage());
            }

            //클래스 로딩
            try {
                Class.forName("com.example.NonExistingClass");
            } catch (ClassNotFoundException e) {
                throw new ClassNotFoundException("클래스를 찾을 수 없습니다: " + e.getMessage());
            }

            //스레드 인터럽트
            Thread thread = new Thread(() -> {
                try {
                    Thread.sleep(1000);
                } catch (InterruptedException e) {
                    System.out.println("스레드가 인터럽트되었습니다.");
                }
            });
            thread.start();
            thread.interrupt();

            //문자열을 숫자로 변환
            System.out.print("숫자로 변환할 문자열을 입력하세요: ");
            String numberString = scanner.next();
            int number = Integer.parseInt(numberString);
            System.out.printf("변환된 숫자: %d\n", number);

            //NullPointerException 예제
            String nullString = null;
            //NullPointerException 발생
            System.out.println(nullString.length());

        } catch (ArithmeticException e) {
            System.out.println("0으로 나눌 수 없습니다");
        } catch (InputMismatchException e) {
            System.out.println("잘못된 입력입니다. 정수를 입력해주세요.");
            //잘못된 입력을 소비하여 무한 루프 방지
            scanner.next();
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("배열의 인덱스가 잘못되었습니다. 0에서 4 사이의 값을 입력해주세요.");
        } catch (FileNotFoundException e) {
            System.out.println("파일을 찾을 수 없습니다");
        } catch (IOException e) {
            System.out.println("파일을 읽는 도중 오류가 발생했습니다: " + e.getMessage());
        } catch (SQLException e) {
            System.out.println("데이터베이스 오류: " + e.getMessage());
        } catch (ClassNotFoundException e) {
//            System.out.println("클래스를 찾을 수 없습니다: " + e.getMessage());
//        } catch (InterruptedException e) {
            System.out.println("스레드가 인터럽트되었습니다.");
        } catch (NumberFormatException e) {
            System.out.println("잘못된 형식입니다. 숫자를 입력해주세요.");
        } catch (NullPointerException e) {
            System.out.println("널 값을 참조하려고 했습니다.");
        } catch (IllegalArgumentException e) {
            System.out.println("잘못된 인수가 전달되었습니다: " + e.getMessage());
        } catch (IllegalStateException e) {
            System.out.println("잘못된 상태입니다: " + e.getMessage());
        } catch (Exception e) {
            System.out.println("예기치 않은 오류가 발생했습니다: " + e.getMessage());
        } finally {
            scanner.close();
        }
    }
}
