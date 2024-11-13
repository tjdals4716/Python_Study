package Java_Study.Practice;

//1부터 10까지의 합을 출력하는 프로그램
public class For {
    public static void main(String[] args) {
        //합계를 저장할 변수를 초기화, 처음에는 0으로 설정
        int sum = 0;
        for(int i = 1;i < 11;i++){
            //반복문이 실행될 때마다 sum에 현재 i 값을 더하고 그 결과를 sum에 저장
            sum += i;
        }
        System.out.printf("1부터 10까지의 합은 " + sum + "입니다.");
    }
}
