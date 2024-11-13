package My_Study;

import java.util.Random;

public class Array2D {
    public static void main(String[] args) {
        int[][] i = new int[3][];
        i[0] = new int[5];
        i[1] = new int[2];
        i[2] = new int[3];

        // 랜덤한 값을 주려면 Random 객체를 사용해야함
        Random rand = new Random();

        for (int row = 0; row < i.length; row++) {
            for (int col = 0; col < i[row].length; col++) {
                i[row][col] = rand.nextInt(100); // Next ~ : 값을 넣는다라는 의미, ()안에는 범위 지정
                System.out.print(i[row][col] + " ");
            }
            System.out.println();
        }

        System.out.println(i[1].length);
    }
}
