import java.util.Scanner;
public class Lab2_1 {
    // TODO: You may add check function in the main method to check the input is valid
    // System.out.print("Invalid Input.");
    // You are not allowed to use exception handling in this question
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
		 if (!input.hasNextInt()) {
            System.out.println("Invalid Input");
            input.close();
            return;
        }
        System.out.println("Please enter the position you want to find in Fibonacci: ");
        int n = input.nextInt();
        Fibonacci(n);
    }

    // Don't change the method name, add signature only
    // You may copy and paste the output from below directly and change "Li Hua" to your name:
    // System.out.print("After Li Hua's contribution, Fibonacci Series till " + n + " terms: ");
    // And then add the result to the output by using System.out.print() to make sure the output shows in the same line;
    Fibonacci() {
        
    }
}    