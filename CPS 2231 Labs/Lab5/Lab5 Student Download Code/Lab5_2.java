import java.util.Scanner;
import java.math.BigInteger;

public class Lab5_2 {
	// TODO: You may add check function in the main method to check the input is valid and nonnegative
    // System.out.print("Invalid Input.");
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = input.nextInt();
        input.close();
        BigInteger factorial = calculateFactorial(n);
        System.out.println(factorial);
    }
	//Don't change the method name, add signature only
	//You may use the methods provided on the second page of pdf
    calculateFactorial() {
    }