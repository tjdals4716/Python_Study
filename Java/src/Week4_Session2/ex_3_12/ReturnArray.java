package Week4_Session2.ex_3_12;

public class ReturnArray {
    static int[] makeArray(){
        int temp[] = new int[4];
        for(int i = 0;i < temp.length;i++) {
            temp[i] = i;
        }
        return temp;
    }

    public static void main(String[] args) {
        int intArarry[];
        intArarry = makeArray();
        for(int i = 0;i < intArarry.length;i++){
            System.out.print(intArarry[i] + " ");
        }
    }
}
