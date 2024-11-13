package Practice;

public class ArrayPractice {
    public static void main(String[] args) {
        int [][] a = new int[5][];

        a[0] = new int[4];
        a[1] = new int[5];
        a[2] = new int[2];
        a[3] = new int[1];
        a[4] = new int[3];

        for(int row = 0;row < a.length;row++){
            for(int col = 0;col < a[row].length;col++){
                a[row][col] = (row + 1) * 10 + col;
                System.out.print(a[row][col] + " ");
            }
            System.out.println();
        }
    }
}
