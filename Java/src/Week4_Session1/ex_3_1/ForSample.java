package Week4_Session1.ex_3_1;

public class ForSample {
    public static void main(String[] args) {
        int sum = 0;

        for(int i = 0;i <= 10;i++){
            sum += i;
            System.out.print(sum);

            if(i <= 9)
                System.out.print(" + ");
            else {
                System.out.print(" = ");
                System.out.print(sum);
            }
        }
    }
}
