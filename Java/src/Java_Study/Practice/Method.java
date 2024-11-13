package Java_Study.Practice;

import java.util.Scanner;

//두 숫자를 입력받아 최대공약수를 구하는 프로그램
public class Method {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.printf("첫 번째 값을 입력하세요 : ");
        int a = scanner.nextInt();

        System.out.printf("두 번째 값을 입력하세요 : ");
        int b = scanner.nextInt();

        //최대공약수 계산
        int gcd = findGCD(a, b);

        System.out.printf("입력한 두 값의 최대공약수 : " + gcd);

        scanner.close();
    }

    public static int findGCD(int a, int b){
        //while 루프는 ()일 때 까지 반복, 즉 여기서는 b가 0이 아닐 때까지 반복
        while(b != 0){
            //다음 단계에서 a 값을 b로 대체하기 위해 현재 b 값을 임시 변수 temp에 저장
            int temp = b;
            //a를 b로 나눈 나머지를 b에 저장
            b = a % b;
            //a 값을 temp(원래 b 값)로 대체
            a = temp;
        }
        //최대공약수 반환
        return a;
    }
}
