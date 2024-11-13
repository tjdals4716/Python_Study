package My_Study.BuiltInFunction;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class CollectionsExample {
    public static void main(String[] args) {
        List<Integer> list = new ArrayList<>();
        list.add(10);
        list.add(5);
        list.add(20);
        list.add(15);

        // sort() 메서드
        Collections.sort(list);
        System.out.println("Sorted list : " + list);

        // reverse() 메서드
        Collections.reverse(list);
        System.out.println("Reversed list : " + list);

        // shuffle() 메서드
        Collections.shuffle(list);
        System.out.println("Shuffled list : " + list);

        // binarySearch() 메서드
        int index = Collections.binarySearch(list, 15);
        System.out.println("Index of 15 : " + index);
    }
}

