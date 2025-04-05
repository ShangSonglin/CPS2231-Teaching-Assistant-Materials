import java.util.Scanner;
import java.util.Arrays;
public class Lab2_3{
    // In this question, you don't need to consider the input validation.
    // Don't change the main method.
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine().trim();
        String[] parts = input.split("\\s+");
        int[] nums = new int[parts.length];
        for (int i = 0; i < parts.length; i++) {
            nums[i] = Integer.parseInt(parts[i]);
        }
        int result = findCycleStart(nums);
        System.out.println(result);
    }

    // You are not allowed to use anything you haven't learned in CPS 1231 and CPS 2231.
	findCycleStart() {
    
    
    
    }
}