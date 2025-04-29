import java.util.Scanner;
/*Purpose: 
* Write a method called encode that takes a string s and an integer n as parameters
* and that returns a new string that scrambles the order of the characters from s in a particular way. 
* The characters should be placed into a grid with n rows and a number of columns determined by the length of the string. 
* The characters are placed into the grid column by column. 
* After filling the grid, the characters should be concatenated by row.
*/
public class Lab3_3{
	public static void main(String[] args){
		//1. prompt the user to enter the encode-need String and an integer n as num of row
		Scanner sc = new Scanner(System.in);
		String str = sc.nextLine();
/*You may assume that the string passed as a parameter is not empty 
* and that the integer passed as a parameter is greater than or equal to 1 and less than the length of the string.
* The string might contain any characters, including spaces. 
*/
		if (str.trim().isEmpty()){
			System.out.println("Invalid Input.");
			return;
		}
		if (!sc.hasNextInt()) {
            System.out.println("Invalid Input.");
            sc.close();
            return;
        }
		int n = sc.nextInt();
		sc.nextLine();  
		sc.close();
		if (n < 1 || n > str.length()){
			System.out.println("Invalid Input.");
			return;
		}
		//2. call the method and return the result
		encode(str, n);
		
	}
	public static void encode(String str, int row){
		int size = str.length();
		int col;
		//Act as index counter, but for moving the index of str because cannot make it into the nested for loop
		int strIndex = 0;
		//1. create an array, find the columns by division
		if (size % row != 0){
			col = size / row + 1;
		}else{
			col = size / row;
		}
		char[][] arr = new char[row][col];
		//for (int i = 0; i < row; i++) {
		//	for (int j = 0; j < col; j++) {
		//		arr[i][j] = ' '; 
		//	}
		//}
		//2. place each character into the grid column by column
		outerloop:
		for (int i = 0; i < col; i++){
			for (int j = 0; j < row; j++){
				if (strIndex == size){
					break outerloop;
				}
				arr[j][i] = str.charAt(strIndex++);
			}
		}
		//print the arr
		for (int i = 0; i < row; i++){
			System.out.print("Row " + (i + 1) + ": ");
			for (int j = 0; j < col; j++){
				System.out.print(arr[i][j] + " ");
			}
			System.out.println();
		}
		//3. read the character row by row
		String encodedStr = "";
		for (int i = 0; i < row; i++){
			for (int j = 0; j < col; j++){
				encodedStr += arr[i][j];
			}
		}
		//4. remove the trailing spaces
		//if (encodedStr.length() > size){
		//	encodedStr = encodedStr.substring(0, size);
		//}
		System.out.println("After Li Hua's testing, Final Encoded String is " + encodedStr);

	}
}