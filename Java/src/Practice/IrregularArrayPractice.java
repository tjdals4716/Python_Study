package Practice;

public class IrregularArrayPractice {
    public static void main(String[] args) {
        int sum = 0;
        int a[][] = new int[4][];

        a[0] = new int[3];
        a[1] = new int[2];
        a[2] = new int[4];
        a[3] = new int[3];

        for(int row = 0;row < a.length;row++){
            for(int col = 0;col < a[row].length;col++){
                a[row][col] = (row + 1) * 10 + col;
                sum += a[row][col];
                System.out.print(a[row][col] + " ");
            }
            System.out.println();
        }

        int total = 0;
        for (int i = 0; i < a.length; i++) {
            total += a[i].length;
            System.out.println(i + 1 + "번째 열 길이 : " + a[i].length);
        }

        System.out.println("행 길이 : " + a.length);
        System.out.println((double)sum / total);
    }
}
