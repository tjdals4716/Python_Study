package My_Study.ex_3_12;

public class ReturnArray {
    public static void main(String[] args) {
        for(int j : makeArray()){
            System.out.print(j + " ");
        }
    }

    static int[] makeArray(){
        int i[] = new int[]{
            1, 2, 3, 4
        };
        return i;
    }
}
