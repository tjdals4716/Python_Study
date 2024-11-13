package Practice;

public class MiddleTest1 {
    public static void main(String[] args) {
        String [] a = {"1", "2", "3.2", "4", "5", "6", "7.4", "8", "9"};
        for(int b = 0;b < a.length;b++) {
            try {
                int j = Integer.parseInt(a[b]);
                System.out.println("출력된 배열 : " + j);

            } catch (Exception e) {
                System.out.println("출력 불가 이유 : " + e);
            }
        }
    }
}
