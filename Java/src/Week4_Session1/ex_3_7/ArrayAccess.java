package Week4_Session1.ex_3_7;

import java.util.Scanner;

public class ArrayAccess {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int intArray[] = new int[5];

        int max = 0;
        System.out.print("양수 5개를 입력하세요 : ");
        for(int i = 1; i < 5; i++) {
            intArray[i] = sc.nextInt();
            if(intArray[i] > max) {
                max = intArray[i];
            }
        }
        System.out.print("입력한 수 중 가장 큰 수 : " + max);

        sc.close();
    }
}
