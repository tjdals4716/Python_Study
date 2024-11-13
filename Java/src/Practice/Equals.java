package Practice;

import java.util.Arrays;

// equals와 ==의 차이
// 비교 대상 :
//        == 연산자: 객체의 참조(메모리 주소)를 비교
//        equals() 메서드: 객체의 내용을 비교
// 사용 범위 :
//        == 연산자: 모든 타입(기본 타입과 참조 타입)에 사용가능
//        equals() 메서드: 객체에만 사용가능
// 오버라이딩:
//        == 연산자: 오버라이딩 불가
//        equals() 메서드: Object 클래스에서 상속받은 메서드로, 클래스에서 재정의 가능
// String 비교 :
//        == 연산자: String 객체의 참조를 비교
//        equals() 메서드: String 클래스에서 재정의되어 문자열의 내용을 비교
// 기본 동작 :
//        == 연산자: 항상 메모리 주소를 비교
//        equals() 메서드: Object 클래스의 기본 구현은 == 연산자와 동일하지만, 많은 클래스(예: String, int 등)에서 내용 비교를 위해 재정의됨
// 결론 : "주소비교"와 "내용비교"의 차이
public class Equals {
    public static void main(String[] args) {
        int [] a = {1, 2, 3};
        int [] b = {1, 2, 3};
        int [] c = {1};
        String [] d = {"ㅁㄴㅇㄹ", "ㅁㄴㅇㄹ", "ㅁㄴㅇㄹ"};
        String [] e = {"ㅁㄴㅇㄹ", "ㅁㄴㅇㄹ", "ㅁㄴㅇㄹ"};
        String [] f = {"ㅁㄴㅇㄹ", "ㅁㄴㅇㄹ"};

        System.out.println(Arrays.equals(a, b)); // T
        System.out.println(Arrays.equals(a, c));
        System.out.println(a == b);
        System.out.println(a == c);
        System.out.println(Arrays.equals(d, e)); // T
        System.out.println(d == e);
        System.out.println(d == f);
        System.out.println(e == f);
        System.out.println(Arrays.equals(e, f));
    }
}
