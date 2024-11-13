package Week6_Session1.ex_4_12;

import java.util.Scanner;

class CurrencyConverter {
    private static double rate;
    public static double toDollar(double won) {
        return won / rate;
    }

    public static double toKWR(double dollar) {
        return dollar * rate;
    }

    public static void setRate(double r) {
        rate = r;
    }
}

public class StaticMember{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("환율(1달러) : ");
        double rate = sc.nextDouble();
        CurrencyConverter.setRate(rate);
        System.out.println("백만원 $ : " + CurrencyConverter.toDollar(1000000));
        System.out.println("$ 100 : " + CurrencyConverter.toKWR(100));
        sc.close();
    }
}

