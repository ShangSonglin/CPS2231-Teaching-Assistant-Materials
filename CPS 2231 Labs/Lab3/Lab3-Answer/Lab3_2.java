import java.util.Scanner;
/*Purpose: 
* Two strings are considered anagrams if they contain the same characters, but the characters may be arranged in a different order. 
* Write a method called areAnagrams and returns true if two strings are anagrams of each other, otherwise false. 
* Treat the input as case-insensitive.
*/
public class Lab3_2{
	public static void main(String[] args){
		//1. prompt the user to enter two strings
		Scanner sc = new Scanner(System.in);
		String temp1 = sc.nextLine();
		String str1 = "";
		//2. data cleaning: only read alpha-numeric characters
		for (int i = 0; i < temp1.length(); i++) {
			char ch = temp1.charAt(i);
			if (Character.isLetter(ch)) {
				str1 += Character.toLowerCase(ch); 
			}
			else if (Character.isDigit(ch)){
				str1 += ch;
			}else{
				continue;
			}
    }	
		String temp2 = sc.nextLine();
		String str2 = "";
		for (int i = 0; i < temp2.length(); i++) {
			char ch = temp2.charAt(i);
			if (Character.isLetter(ch)) {
				str2 += Character.toLowerCase(ch); 
			}
			else if (Character.isDigit(ch)){
				str2 += ch;
			}else{
				continue;
			}
	}	
		sc.close();
		//3. call method and print the result
		System.out.println("After Li Hua's testing, " + str1 + " and " + str2 + " are anagrams, which is " + areAnagrams(str1, str2));
	}
	public static boolean areAnagrams(String str1, String str2){
		//1. Quick: length is not equal will not be anagram after data cleaning
		if (str1.length() != str2.length()){
			return false;
		}
		
		//Initialize size for convenience
		int size  = str1.length();
		//In order to avoid duplicate matching, use boolean array to show the status of already-matched characters
		boolean[] used = new boolean[size]; 
		//2. Compare two string's digit by nested for loop: compare one char in str by traversing the other str
			for (int i = 0; i < size; i++){
				boolean found = false;
				for (int j = 0; j < size; j++){
					if (!used[j] && str1.charAt(i) == str2.charAt(j)){
						used[j] = true;
						found = true;
						break;//skip the inner loop
					}
					}
				if (found == false){
					return false;
				}
				}
			return true;
		// Or you can you int[] array
		// public boolean isAnagram(String s, String t) {
		// if (s.length() != t.length()) return false;
		
		// int[] count = new int[26];  // 统计字母频次，假设只考虑小写字母
		
		// for (int i = 0; i < s.length(); i++) {
		// count[s.charAt(i) - 'a']++;  // s中对应字符计数加一
		// count[t.charAt(i) - 'a']--;  // t中对应字符计数减一
		// }
		
		// // 最后判断每个字母计数是否都为0
		// for (int c : count) {
		// if (c != 0) return false;
		// }
		
		// return true;
}

	}
}

