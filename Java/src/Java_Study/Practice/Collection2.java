package Java_Study.Practice;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

//리스트를 사용하여 문자열을 저장하고 정렬하는 프로그램
public class Collection2 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        ArrayList<String> list = new ArrayList<>();

        while(true){
            System.out.printf("문자를 입력해주세요 (그만하려면 -1을 입력) : ");
            String massage = scanner.nextLine();
            if(massage.equals("-1")){
                break;
            }
            list.add(massage);
        }
        Collections.sort(list);
        System.out.printf("입력한 문자의 정렬입니다 : " + list);
        scanner.close();
    }
}