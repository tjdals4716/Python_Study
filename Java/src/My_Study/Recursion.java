package My_Study;

// 재귀 함수란 함수가 자기 자신을 호출하는 방식을 말함
public class Recursion{
    // 재귀 함수로 팩토리얼 계산
    public static int factorial(int n) {
        if (n == 1) {
            // 종료 조건 : n이 1이면 1을 반환
            return 1;
        } else {
            // n * (n-1)! 재귀 호출
            return n * factorial(n - 1);
        }
    }

    public static void main(String[] args) {
        int number = 5;
        int result = factorial(number);
        System.out.println(number + "의 팩토리얼: " + result);
    }
}