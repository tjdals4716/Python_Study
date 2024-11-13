package My_Study.BuiltInFunction;

public class SystemExample {
    public static void main(String[] args) {
        // System.out.println() 메서드
        System.out.println("This is a message!");

        // currentTimeMillis() 메서드
        long currentTime = System.currentTimeMillis();
        System.out.println("Current time in milliseconds : " + currentTime);

        // arraycopy() 메서드
        int[] src = {1, 2, 3, 4, 5};
        int[] dest = new int[5];
        System.arraycopy(src, 0, dest, 0, src.length);
        System.out.println("Copied array : ");
        for (int i : dest) {
            System.out.print(i + " ");
        }
    }
}

