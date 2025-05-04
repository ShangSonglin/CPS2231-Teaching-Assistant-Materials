import java.util.Scanner;
/*Purpose: 
* Write a method named containsBothDigits that takes an integer n 
* and returns true if the number contains both digits 2 and 7, and false otherwise.
*/
public class Lab3_1{
	public static void main(String[] args){
		//1. prompt the user to enter an integer n
		Scanner sc = new Scanner(System.in);
		if (!sc.hasNextInt()) {
				System.out.println("Invalid Input.");
				sc.close();
				return;
			}
		int n = sc.nextInt();
		sc.close();
		//2. call the method and print the result
		System.out.println("After Li Hua's testing, " + n + " contains both 2 and 7, which is " + containsBothDigits(n));
		}
	public static boolean containsBothDigits(int num){
		num = Math.abs(num);
		//use counter to read the occurrence, when counter goes to 2, return	
		int count = 0;
		//use temp to represent each digit
		int temp = 0;
		//1. Read each digit by modular and division operation
		while ( num != 0 ){
		//2. compare the digit in temp, if equal to the particular digit, increment the counter
			temp = num % 10;
			if ( temp == 2 || temp == 7){
				count++;
			}
			if ( count == 2 ){
				return true;
			}
			num = num / 10;
	}
		return false;
}
}