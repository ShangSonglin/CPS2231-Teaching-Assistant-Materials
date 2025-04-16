import java.util.Scanner;
	// TODO: You may add check function in the main method to check the integer input is valid
    // System.out.print("Invalid Input.");
	// You should not modify other parts in main method
	// No StringBuilder (just use `+` for strings)
	// No ArrayList (stick to arrays)
public class Lab3_3{
	public static void main(String[] args){
		Scanner sc = new Scanner(System.in);
		String str = sc.nextLine();
		if (str.trim().isEmpty()){
			System.out.println("Invalid Input.");
			return;
		}
		int n = sc.nextInt();
		sc.nextLine(); 
		sc.close();
		encode(str, n);
		
	}
	// Don't change the method name, add signature only
	// You may copy and paste the output from below directly and change "Li Hua" to your name:
   //System.out.println("After Li Hua's testing, Final Encoded String is " + encodedStr);
	// Before print this line, please print the array in format as well
	public static void encode(String str, int row){
		
	}
}
