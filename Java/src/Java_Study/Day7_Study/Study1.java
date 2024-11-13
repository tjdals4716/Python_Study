package Java_Study.Day7_Study;

import java.util.Scanner;

//사용자로부터 값을 반복적으로 받아내 그 값만큼 곱과 합의 결과를 출력하는 프로그램
public class Study1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        //sum 변수를 while 루프안에서 초기화하는 것이아니라 while 루프 밖에서 초기화를 해야함
        int sum = 0;

        while(true){
            System.out.printf("정수를 입력하세요(종료하려면 -1을 입력) : ");
            int numbers = scanner.nextInt();

            if(numbers == -1){
                break;
            }
            sum += numbers;
        }
        System.out.printf("입력한 모든 정수의 합 : " + sum);
        scanner.close();
    }
}
