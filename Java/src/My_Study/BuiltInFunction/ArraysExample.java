package My_Study.BuiltInFunction;

import java.util.Arrays;

public class ArraysExample {
    public static void main(String[] args) {
        int[] array = {5, 2, 8, 1, 9};

        // sort() 메서드
        Arrays.sort(array);
        System.out.println("Sorted array : " + Arrays.toString(array));

        // binarySearch() 메서드
        int index = Arrays.binarySearch(array, 8);
        System.out.println("Index of 8 : " + index);

        // equals() 메서드
        int[] array2 = {1, 2, 3, 4, 5};
        int[] array3 = {1, 2, 3, 4, 5};
        System.out.println("Arrays equal : " + Arrays.equals(array2, array3));

        // fill() 메서드
        Arrays.fill(array, 0);
        System.out.println("Filled array with 0 : " + Arrays.toString(array));

        // copyOf() 메서드
        int[] copiedArray = Arrays.copyOf(array2, 3);
        System.out.println("Copied array : " + Arrays.toString(copiedArray));
    }
}

