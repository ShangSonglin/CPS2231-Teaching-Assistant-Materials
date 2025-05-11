package Lab4_Answer;
import java.util.Scanner;
/*Purpose: Count Character Occurrences*/
public class Lab4_1{
	public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
		String str = input.nextLine();
		if (str == null || str.trim().isEmpty()) {
			System.out.println("0");
			return;
		}
		String charInput = input.nextLine().trim();
		if (charInput.isEmpty()) {
			System.out.println("0");
			return;
		}
		char ch = charInput.charAt(0);
        int count = countChar(str, ch);
        System.out.println(count);
    }
	public static int countChar(String str, char ch){
		//fetch each item
		//compare with the ch
		//return the occurrence after the last comparison
		if (str.isEmpty()) {
            return 0;
        }
		char strCh;
		strCh = str.charAt(0);
		int count = (strCh == ch) ? 1 : 0;
		str = str.substring(1);
		return count + countChar(str, ch);
		
}
}