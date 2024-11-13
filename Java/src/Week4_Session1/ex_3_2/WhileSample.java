package Week4_Session1.ex_3_2;

import java.util.Scanner;

public class WhileSample {
    public static void main(String[] args) {
        int count = 0;
        int sum = 0;
        Scanner sc = new Scanner(System.in);
        System.out.print("정수를 입력하세요 (종료하려면 -1을 입력) : ");

        // 여기서 정수 입력
        int n = sc.nextInt();
        // -1을 입력하면 while문을 벗어난다
        while(n != -1){
            sum += n;
            count++;
            // 정수 입력?
            n = sc.nextInt();
        }
        if(count == 0)
            System.out.print("입력된 수가 없습니다");
        else{
            System.out.println("정수 개수 : " + count + "개");
            System.out.println("입력한 정수의 평균 : " + (double)sum/count);
        }
    }
}
