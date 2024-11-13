package Practice;

import java.util.Scanner;

public class MiddleTest2 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int [] a = new int[3];
        int sum = 0;
        int b = 0;
        for(int i = 0;i < a.length;i++){
            try{
                System.out.print("정수 세개를 입력하세요 : ");
                b = sc.nextInt();
            } catch(Exception e){
                String ex = sc.nextLine();
                System.out.println("입력한 것은 정수가 아님 : " + ex);
                i--;
                continue;
            }
            sum += b;
        }
        System.out.print("입력한 수의 합 : " + sum);
        sc.close();
    }
}
