package Java_Study.Practice;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

//리스트를 사용하여 숫자를 저장하고 정렬하는 프로그램
public class Collection {
    public static void main(String[] args) {
        //Scanner 객체를 생성
        Scanner scanner = new Scanner(System.in);
        //ArrayList<> 객체를 생성
        ArrayList<Integer> numbers = new ArrayList<>();

        //if나 while을 스케너 출력문 앞에쓰면 출력문이 반복하여 나오고 뒤에 사용 시 출력문이 한 번만 출력됨
        while(true){
        System.out.printf("숫자를 입력하세요 (끝내려면 -1을 입력하세요) : ");
            int number = scanner.nextInt();
            //만약 number가 -1이라면 break를 사용하여 빠져나옴
            if(number == -1){
                break;
            }
            numbers.add(number);
        }
        //입력한 숫자를 정렬
        Collections.sort(numbers);
        //정렬된 숫자를 출력
        System.out.println("입력한 숫자들을 정렬하였습니다 : " + numbers);
        scanner.close();
    }
}
