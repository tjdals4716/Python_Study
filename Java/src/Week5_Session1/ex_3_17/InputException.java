package Week5_Session1.ex_3_17;

import java.util.InputMismatchException;
import java.util.Scanner;

public class InputException {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("정수 3개를 입력하세요");

        int sum = 0;
        int n = 0;

        for(int i = 0;i < 3;i++){
            System.out.print(i + " 번째 입력" + " : ");
            try{
                n = sc.nextInt();
            }
            catch(InputMismatchException e){
                String ex = sc.nextLine(); // 잘못된 값이 들어오면 지워버림
                System.out.println(ex + "은 정수가 아닙니다 다시 입력하세요");
                i--; // 잘못된 값을 미리 감소시킴
                continue; // 잘못된 값은 합이 안되도록 continue 사용
            }
            sum += n;
        }
        System.out.print("합 : " + sum);
        sc.close();
    }
}
