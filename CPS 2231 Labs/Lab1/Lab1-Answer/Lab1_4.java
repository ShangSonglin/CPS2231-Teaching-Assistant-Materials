import java.util.Scanner;
public class Lab1_4 {
    /*Purpose: Prompt the user to enter the center x-, y- corrdinates
     * and the width and height of two rectangles. 
     * Determine whether the second rectangle is "inside" the first or "overlaps" with the first or "does not overlap" with the first.
     */
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        // 1.Prompt the user to enter r1's center x-, y- corrdinates, width, and height
        System.out.println("Enter r1's center x-, y-coordinates, width, and height:");
            double x1 = scanner.nextDouble();
            double y1 = scanner.nextDouble();
            double w1 = scanner.nextDouble();
            double h1 = scanner.nextDouble();
        // 2.Prompt the user to enter r2's center x-, y- corrdinates, width, and height
        System.out.println("Enter r2's center x-, y-coordinates, width, and height:");
            double x2 = scanner.nextDouble();
            double y2 = scanner.nextDouble();
            double w2 = scanner.nextDouble();
            double h2 = scanner.nextDouble();
        // 3.Compute the distance between the centers of the two rectangles
        double halfW1 = w1 / 2;
        double halfH1 = h1 / 2;
        double halfW2 = w2 / 2;
        double halfH2 = h2 / 2;

        double left1 = x1 - halfW1;
        double right1 = x1 + halfW1;
        double bottom1 = y1 - halfH1;
        double top1 = y1 + halfH1;

        double left2 = x2 - halfW2;
        double right2 = x2 + halfW2;
        double bottom2 = y2 - halfH2;
        double top2 = y2 + halfH2;
        //  4.Determine whether r2 is inside r1, overlaps with r1, or does not overlap with r1 (*rectangles just touch does not count as overlapping)
        if (left2 >= left1 && right2 <= right1 && bottom2 >= bottom1 && top2 <= top1) {
                System.out.println("r2 is inside r1");
        } else if (right2 <= left1 || left2 >= right1 || top2 <= bottom1 || bottom2 >= top1) {
                System.out.println("r2 does not overlap r1");
        } else {
                System.out.println("r2 overlaps r1");
        }
        scanner.close();
    }
    
}
