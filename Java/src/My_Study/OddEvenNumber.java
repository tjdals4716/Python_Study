package My_Study;

// a % 2 == 0 → a는 짝수
// a % 2 == 1 → a는 홀수
// a % 6 == 0 → a는 6의 배수이면서 짝수 (6은 2로 나누어 떨어지니)
// a % 9 == 1 → a는 9의 배수이면서 짝수이면서 홀수
// 홀수는 대체적으로 나누어 떨어지지않아 웬만하면 짝수나 홀수의 결과가 나옴
// 반면에 짝수는 2로 모두 나뉘어 떨어지니 모두 짝수의 결과가 나옴
public class OddEvenNumber {
    public static void main(String[] args) {
        int a = 7;

        if (a % 2 == 1) {
            System.out.println(a + "은(는) 홀수입니다.");
        } else {
            System.out.println(a + "은(는) 짝수입니다.");
        }
    }
}

