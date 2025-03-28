import java.util.Scanner;
public class Lab1_2{
    /*Purpose: Test Palindrome
     * After converting all uppercase letters into lowercase letters
     * removing all non-alphanumeric characters
     * and comparing the string with its reverse
     * return true if the string is a palindrome or false otherwise
     */
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        while (scanner.hasNextLine()) { // Loop reads multiple lines
            String input = scanner.nextLine();
            System.out.println(isPalindrome(input));
        }
        scanner.close(); 
    }
    public static boolean isPalindrome(String input){
        //1. Store the data in a tempArray
        char[] tempArray = new char[input.length()];
        int size = 0;
        
        for (int i = 0; i < input.length(); i++) {
        //2. Convert all uppercase letters into lowercase letters
        //3. Only read numeric and alphabetic characters: remove all non-alphanumeric characters
            char ch = input.charAt(i);
            if (ch >= 'A' && ch <= 'Z') {
                ch = (char) (ch + 32); // Convert to lowercase
            }
            if ((ch >= 'a' && ch <= 'z') || (ch >= '0' && ch <= '9')) {
                tempArray[size++] = ch; // Add to tempArray if alphanumeric
            }
        }
        //4. Compare the string with its reverse
        for (int i = 0; i < size / 2; i++) {
            if (tempArray[i] != tempArray[size - i - 1]) {
                return false;
            }
        }
        return true;
    }
    
}