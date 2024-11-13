package Java_Study.Day7_Study;

import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

//사용자로부터 배열을 입력받아 내림차순으로 정렬하는 프로그램
public class Study3 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        //배열의 크기를 입력
        System.out.printf("배열의 크기를 입력하세요 : ");
        int size = scanner.nextInt();

        //배열을 생성
        Integer[] array = new Integer[size];
        System.out.printf("정수를 입력하세요 : ");
        for(int i = 0;i < size;i++){
            array[i] = scanner.nextInt();
        }

        //Arrays.sort 메서드를 사용하여 배열을 정렬
        //Collections.reverseOrder()는 기본적으로 오름차순으로 정렬되는 배열을 내림차순으로 정렬
        Arrays.sort(array, Collections.reverseOrder());
        //Arrays.toString(array)를 사용하여 배열을 문자열로 변환한 후 정렬된 결과를 출력
        System.out.println("입력한 숫자의 내림차순 정렬 : " + Arrays.toString(array));
        scanner.close();
    }
}
