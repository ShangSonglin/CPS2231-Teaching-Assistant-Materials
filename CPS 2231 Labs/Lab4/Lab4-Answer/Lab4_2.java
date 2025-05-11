package Lab4;
import java.util.Scanner;
/*Purpose: Count Palindrome Substrings*/
public class Lab4_2 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        String str = input.nextLine();
		if (str == null || str.trim().isEmpty()) {
			System.out.println("0");
			return;
		}
        int count = countPalindromicSubstrings(str);
        System.out.println(count);
    }

    public static int countPalindromicSubstrings(String str) {
        // Base case: if string is empty, return 0
        if (str.isEmpty()) {
            return 0;
        }
        int count = countPalindromesFromStart(str, 0);

        return count + countPalindromicSubstrings(str.substring(1));
    }

    private static int countPalindromesFromStart(String str, int end) {
        // Base case: if end is beyond string length, stop
		if (end >= str.length()){
            return 0;
        }
        int count = isPalindrome(str, 0, end) ? 1 : 0;

        return count + countPalindromesFromStart(str, end + 1);
    }

    private static boolean isPalindrome(String str, int start, int end) {
        if (start >= end) {
            return true;
        }

        if (str.charAt(start) != str.charAt(end)) {
            return false;
        }

        return isPalindrome(str, start + 1, end - 1);
}
}

