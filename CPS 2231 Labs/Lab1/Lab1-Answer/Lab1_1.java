import java.util.Scanner;
public class Lab1_1 {
    /*Purpose: Defanged IP address replaces every period "." with "[.]"
    Avoid invalid input, in case  255.100.0 can be considered as an invalid IP address
    */
    public static String defangIPaddr(String address) {
    //1. Avoid invalid input
    int dotCount = 0;
    int num = -1; //ensure each part reads as integer
    boolean isValid = true;

    for (int i = 0; i < address.length(); i++) {
        char ch = address.charAt(i);
        if (ch == '.') {
            dotCount++;
            if (dotCount > 3 || num < 0 || num > 255) { //ensure no more than 3 dots
                isValid = false;
                break;
            }
            num = -1;
        } else if (ch >= '0' && ch <= '9') {
            if (num == -1) num = 0; 
                num = num * 10 + (ch - '0'); //read intger bit by bit(char bit to integer bit)
                if (num > 255) { 
                    isValid = false;
                    break;
                }
        } else {
            isValid = false;
            break;
        }
    }

    if (dotCount != 3 || num < 0 || num > 255) { //ensure no less than 3 dots
        isValid = false;
    }

    if (!isValid) { //ensure "." rather than other symbols
        return "Invalid IP address.";
    }
    //2. Create a char array to store the defanged IP address
    char[] tempArray = new char[address.length() + 6];
    int size = 0;
    //3. Loop through the address
    for (int i = 0; i < address.length(); i++) {
    //4. If the character is a period, replace it with "[.]"
        if (address.charAt(i) == '.') {
            tempArray[size++] = '[';
            tempArray[size++] = '.';
            tempArray[size++] = ']';
        } else {
            tempArray[size++] = address.charAt(i);
        }
    }
    //5. Print the defanged IP address
    String result = "";
    for (int i = 0; i < size; i++) {
        result += tempArray[i];
    }
    return result;
}
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine();
        System.out.println(defangIPaddr(input));
        scanner.close();
    }
}
