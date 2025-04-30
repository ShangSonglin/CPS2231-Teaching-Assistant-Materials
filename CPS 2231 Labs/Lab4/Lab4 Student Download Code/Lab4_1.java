package Lab4;
import java.util.Scanner;

public class Lab4_1 {

    // TODO: You may add check function in the main method to check the input is valid
    // System.out.print("Invalid Input.");
    // You are not allowed to use exception handling in this question
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String str = input.nextLine();
        char ch = input.next().charAt(0);
        int count = countChar(str, ch);
        System.out.println(count);
    }

    // Don't change the method name, add signature only
    // Recursive method to count occurrences of ch in str
    countChar() {
        
    }
}