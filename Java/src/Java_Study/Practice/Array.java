package Java_Study.Practice;

import java.util.Scanner;

//사용자로부터 5개의 숫자를 입력받아 배열에 저장하고 그 숫자들의 평균을 계산하는 프로그램
public class Array {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int[] number = new int[5];
        int sum = 0;

        for(int i = 0;i < 5;i++){
            System.out.printf("숫자 다섯 개를 입력하세요 : ");
            number[i] = scanner.nextInt();
            sum += number[i];
        }

        //sum을 실수형(double)으로 형변환, 정수형 변수를 실수형 변수로 변환하여 나눗셈 연산에서 실수형 결과를 얻기 위함
        //numbers.length는 배열 numbers의 길이(배열에 저장된 요소의 개수)를 나타냄. 여기서는 5개
        double average = (double) sum / number.length;

        System.out.printf("입력한 값들의 평균 : " + average);

        //Scanner 객체를 사용한 후에 이를 닫기 위해 호출하는 메서드, 메모리 누수와 같은 자원 낭비를 방지
        scanner.close();
    }
}
