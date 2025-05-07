import java.util.Scanner;

public class Lab5_1 {
	// TODO: You may add check function in the main method to check the first input is valid
    // System.out.print("Invalid Input.");
	  public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter the first integer: ");
        String firstInput = input.next();
		System.out.print("Enter the second value (might be invalid): ");
        String secondInput = input.next();
		observeWrapper(firstInput, secondInput);
        input.close();
    }
	
	//Don't change the method name, add signature only
	//You may use the methods provided on the second page of pdf
	/*To print the result, you may use following structure
	System.out.println("Integer Object: " );
	System.out.println("Primitive int value (after unboxing): ");
	System.out.println("Integer Object + 5 = ");
	try {
            System.out.println("Integer Object (this line might not be reached): " + integerObject);
        } catch (NumberFormatException e) {
        }
	*/
    observeWrapper() {

    }

}
