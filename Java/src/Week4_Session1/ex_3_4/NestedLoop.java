package Week4_Session1.ex_3_4;

public class NestedLoop {
    public static void main(String[] args) {
        for(int j = 1;j < 10;j++){
            for(int i = 1;i < 10;i++){
                // 이 부분만 바꿔줘도 됨
                System.out.print(i + " * " + j + " = " + i * j);
                // 하나씩 탭으로 띄우기
                System.out.print("\t");
            }
            // 한 단이 끝나면 다음 줄로 커서로 이동
            System.out.println();
        }
    }
}
