import java.util.Scanner;
/*Purpose: 
prompts the user to enter values for a, b, and c 
and displays the result based on the discriminant. 
If the discriminant is positive, display the two roots. 
If the discriminant is 0, display the one root. Otherwise,
display "The equation has no roots."
*/
public class QuadraticEquationApp {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
		//1. prompt to enter double a,b,c
        System.out.print("Enter a, b, c: ");
        double a = input.nextDouble();
        double b = input.nextDouble();
        double c = input.nextDouble();
		//Instantialization
        QuadraticEquation eq = new QuadraticEquation(a, b, c);
		
        double discriminant = eq.getDiscriminant();
        input.close();
		printRoots(eq);
    }
	public static void printRoots(QuadraticEquation eq) {
        double discriminant = eq.getDiscriminant();

        if (discriminant > 0) {
            System.out.println("Root 1 is " + eq.getRoot1());
            System.out.println("Root 2 is " + eq.getRoot2());
        } else if (discriminant == 0) {
            System.out.println("The root is " + eq.getRoot1());
        } else {
            System.out.println("The equation has no real roots.");
        }
	}
}
