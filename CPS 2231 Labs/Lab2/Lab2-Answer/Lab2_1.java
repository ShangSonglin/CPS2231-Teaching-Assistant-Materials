import java.util.Scanner;
/*Purpose: 
* compute Fibonacci numbers use loops
* and print the first Fibonacci numbers
*/
public class Lab2_1 {
	public static void main(String[] args){
	//1. prompt the user to enter integer index
	//System.out.println("Please enter the position you want to find in Fibonacci:");
	Scanner input = new Scanner(System.in);
	if (!input.hasNextInt()) {
            System.out.println("Invalid Input.");
            input.close();
            return;//stop here, exit this method.
        }
	int n = input.nextInt();
	if (n<= 0) {
            System.out.println("Invalid Input.");
            input.close();
            return;
        }
	//2. call the method and print the result
	Fibonacci(n);
	}
	public static void Fibonacci(int num){
		//1. initialize first two term
		int firstTerm = 1;
		int secondTerm = 1;
		System.out.print("After Li Hua's contribution, Fibonacci Series till " + num + " terms: ");
		//2. next term = previous one + second previous one
		for(int i = 0; i < num; ++i){
			System.out.print(firstTerm + " ");
			int nextTerm = firstTerm + secondTerm;
			firstTerm = secondTerm;
			secondTerm = nextTerm;
		}
	}
}