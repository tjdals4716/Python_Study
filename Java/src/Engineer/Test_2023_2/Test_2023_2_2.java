package Engineer.Test_2023_2;

public class Test_2023_2_2 {
    public static void main(String[] args) {

        String str1 = "Programming";
        String str2 = "Programming";
        String str3 = new String("Programming");

        System.out.println(str1 == str2);
        System.out.println(str1 == str3);
        System.out.println(str1.equals(str3));
        System.out.println(str2.equals(str3));
    }
}
