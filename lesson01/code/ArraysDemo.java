import java.util.ArrayList;
import java.util.Arrays;

public class ArraysDemo {
    static int linearSearch(int[] a, int target) {
        for (int i = 0; i < a.length; i++) {
            if (a[i] == target) return i;
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] arr = {10, 20, 30, 40, 50};

        // 1. Access by index: O(1)
        System.out.println(arr[3]);                 // 40

        // 2. Linear search: O(n)
        System.out.println(linearSearch(arr, 40));  // 3

        // Fixed-size int[] cannot grow, so use ArrayList for the rest
        ArrayList<Integer> list = new ArrayList<>(Arrays.asList(10, 20, 30, 40, 50));

        // 3. Insert 25 at index 2: O(n)
        list.add(2, 25);
        System.out.println(list);   // [10, 20, 25, 30, 40, 50]

        // 4. Delete the element at index 2: O(n)
        list.remove(2);
        System.out.println(list);   // [10, 20, 30, 40, 50]

        // 5. Append at the end: O(1) amortized
        list.add(60);
        System.out.println(list);   // [10, 20, 30, 40, 50, 60]
    }
}
