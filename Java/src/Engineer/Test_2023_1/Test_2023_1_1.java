package Engineer.Test_2023_1;

public class Test_2023_1_1 {
    public static void main(String[] args) {
        int a = 10;
        Static.b = 0;
        Static st = new Static();

        System.out.println(Static.b++);
        System.out.println(st.b);
        System.out.println(a);
        System.out.println(st.a);
    }
}

class Static{
    public int a = 20;
    static int b = 0;
}
