import java.util.Scanner;

public class Lab5_3 {
	// TODO: You may add check function in the main method to check the input is valid and nonnegative
    // System.out.print("Invalid Input.");
	public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter a sentence:");
        String input = scanner.nextLine();
        String output = reverseWords(input);
        System.out.println("Reversed sentence:");
        System.out.println(output);
    }
	//Don't change the method name, add signature only
	//You may use the methods provided on the second page of pdf
    public static String reverseWords(String sentence) {
  
}
