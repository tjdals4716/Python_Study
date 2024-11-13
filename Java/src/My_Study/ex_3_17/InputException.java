package My_Study.ex_3_17;

import java.util.InputMismatchException;
import java.util.Scanner;

public class InputException {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int sum = 0;
        int n = 0;

        while(true){
            for(int i = 1;i < 4;i++){
                System.out.print(i + "번 째 값 : ");

                try{
                    n = sc.nextInt();
                } catch (InputMismatchException e){
                    String ex = sc.nextLine();
                    System.out.println("'" + ex + "'" + "은 정수가 아닙니다. 다시 입력하세요.");
                    i--;
                    continue;
                }
                sum += n;
            }
            System.out.println("입력한 정수의 합 : " + sum);
            break;
        }
        sc.close();
    }
}
