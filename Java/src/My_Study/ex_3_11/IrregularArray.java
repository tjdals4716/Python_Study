package My_Study.ex_3_11;

public class IrregularArray {
    public static void main(String[] args) {
        int i[][] = new int[4][];

        i[0] = new int[3];
        i[1] = new int[2];
        i[2] = new int[3];
        i[3] = new int[2];

        for(int row = 0;row < i.length;row++){
            for(int col = 0;col < i[row].length;col++){
                i[row][col] = (row + 1) * 10 + col;
                System.out.print(i[row][col] + " ");
            }
            System.out.println();
        }
    }
}
