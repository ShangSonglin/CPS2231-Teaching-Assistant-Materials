import java.util.Arrays;

public class Lab6_2 {
    public static void main(String[] args) {
        // Parse input string to array
        int[] arr;
        if (args.length == 0 || args[0].trim().isEmpty()) {
            arr = new int[0];
        } else {
            String[] numbers = args[0].split(" ");
            arr = new int[numbers.length];
            for (int i = 0; i < numbers.length; i++) {
                arr[i] = Integer.parseInt(numbers[i]);
            }
        }

        // Create a copy of the original array for display
        int[] originalArr = Arrays.copyOf(arr, arr.length);
        
        // Use BubbleSort for demonstration
        Sortable sorter = new BubbleSort();
        
        System.out.println("Original array: " + Arrays.toString(originalArr));
        sorter.sort(arr);
        System.out.println("After sorting: " + Arrays.toString(arr));
        System.out.println("Sort validation: " + (isSorted(arr) ? "PASSED" : "FAILED"));
    }

    private static boolean isSorted(int[] arr) {
        for (int i = 0; i < arr.length - 1; i++) {
            if (arr[i] > arr[i + 1]) {
                return false;
            }
        }
        return true;
    }
}

// TODO: Create the Sortable interface here
// The interface should have one method:
// sort(int[] arr) - sorts the array in ascending order
interface Sortable {
    // Your code here
}

// TODO: Create the BubbleSort class here
// The class should implement the Sortable interface
// Implement the bubble sort algorithm in the sort method
class BubbleSort {
    // Your code here
}

// TODO: Create the SelectionSort class here
// The class should implement the Sortable interface
// Implement the selection sort algorithm in the sort method
class SelectionSort {
    // Your code here
} 