package Practice;

public class MiddleTest4 {
    public static void main(String[] args) {
        int x = 5;
        int y = 6;
        int a = (x > y)?-1:1;
        System.out.println("삼항연산자 결과 : " + a);

        int [] num = {1, 2, 3, 4, 5};
        for(int n : num){
            System.out.print(n + " ");
        }
        System.out.println();
        System.out.println("배열의 길이 : " + num.length);

        System.out.println('a' > 'b');
        System.out.println(3 >= 2);
        System.out.println(-1 < 0);
        System.out.println(3.45 <= 2);
        System.out.println(3 == 2);
        System.out.println(3 != 2);
        System.out.println(!(3 != 2));
        System.out.println((3 > 2) && (3 > 4));
        System.out.println((3 != 2) || (-1 > 0));
        System.out.println((3 != 2) ^ (-1 > 0));

        String [] j = {"2", "3", "dfsdf", "33", "1231", "34", "89"};
        for(int i = 0;i < j.length;i++){
            try{
                int o = Integer.parseInt(j[i]);
                System.out.println("숫자로 변환된 값 : " + o);
            } catch(Exception e){
                System.out.println("변환 불가 : " + e);
            }
        }
    }
}
