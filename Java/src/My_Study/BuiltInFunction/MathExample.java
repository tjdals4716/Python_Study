package My_Study.BuiltInFunction;

public class MathExample {
    public static void main(String[] args) {
        int a = -5;
        double b = 2.5;

        // abs() 메서드
        System.out.println("Absolute value of a : " + Math.abs(a));

        // max(), min() 메서드
        System.out.println("Max of 3 and 7 : " + Math.max(3, 7));
        System.out.println("Min of 3 and 7 : " + Math.min(3, 7));

        // pow() 메서드
        System.out.println("2 raised to the power 3 : " + Math.pow(2, 3));

        // sqrt() 메서드
        System.out.println("Square root of 16 : " + Math.sqrt(16));

        // random() 메서드
        System.out.println("Random number between 0 and 1 : " + Math.random());
    }
}

