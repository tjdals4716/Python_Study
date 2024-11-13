package Engineer.Test_2024_2;

public class Test_2024_2_1 {
    public static void check(int[] x, int[] y) {
        if(x==y) System.out.print("O");
        else System.out.print("N");
    }
    public static void main(String[] args) {
        int a[] = new int[] {1, 2, 3, 4};
        int b[] = new int[] {1, 2, 3, 4};
        int c[] = new int[] {1, 2, 3};
        check(a, b);
        check(b, c);
        check(a, c);
    }
}
