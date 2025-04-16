import java.util.Scanner;
/* Purpose: 
* create a  Multiplicative Table with the knowledge of array
*/
public class Lab2_2 {
    public static void main(String[] args) {
		//1. prompt the user to enter the num of rows and columns
        Scanner input = new Scanner(System.in);
        //System.out.print("Please enter the row and length for your multiplicative table:");
		 if (!input.hasNextInt()) {
            System.out.println("Invalid Input.");
            input.close();
            return;
        }
        int rows = input.nextInt();
		if (rows <= 0) {
            System.out.println("Invalid Input.");
            input.close();
            return;
        }
		 if (!input.hasNextInt()) {
            System.out.println("Invalid Input.");
            input.close();
            return;
        }
        int cols = input.nextInt();
		if (cols <= 0) {
            System.out.println("Invalid Input.");
            input.close();
            return;
        }
		//2. call the method and print the result
		multiplicativeTable(rows, cols);
    }

    public static void multiplicativeTable(int rows, int cols) {
		//1. create the array
		int[][] table = new int[rows][cols];
		//2. item = row * column
        for (int i = 0; i < rows; i++) {//index start from 0, item start from 1
            for (int j = 0; j < cols; j++) {
				table[i][j] = (i + 1) * (j + 1);               
            }
        }
		System.out.println("Li Hua's multiplicative table is:");
		//3. format the table 
		for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                System.out.printf("%-4d", table[i][j]); // Formatting for alignment
            }
            System.out.println();
        }
    }
}