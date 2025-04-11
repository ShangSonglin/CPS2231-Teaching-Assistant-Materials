import java.util.Scanner;
public class Lab1_3 {
    /* Purpose: Prompt the user to enter an integer for today's day of the week
     * and another integer for the number of days after today for a future day
     * and display the future day of the week.
     */

    public static void main(String[] args){
        String[] days = {"Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"};
        //1.Prompt the user to enter an integer for today's day of the week
        Scanner input = new Scanner(System.in);
		System.out.println("Enter the current day:");
        if (!input.hasNextInt()) {
            System.out.println("Invalid Input");
            input.close();
            return;
        }
        int today = input.nextInt();
      
        //2.Prompt the user to enter the number of days after today for a future day
		System.out.println("Enter the day elapsed: ");
        if (!input.hasNextInt()) {
            System.out.println("Invalid Input");
            input.close();
            return;
        }
        int elapsed = input.nextInt();
        
        //3.Display the future day of the week
        if(today >= 0 && today <= 6 && elapsed >= 0){
            int future = (today + elapsed) % 7;//Circular
            System.out.println("Today is " + days[today] + " and the future day is " + days[future]);
        }
        else
			System.out.println("Invalid Input");
        input.close();
    }
   
}
