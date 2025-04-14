/*Write a test program
 that creates two Rectangle objects—one with width 4 and height 40, 
 and the other with width 3.5 and height 35.9. 
 Display the width, height, area, and perimeter of each rectangle in this order.
*/
public class RectangleApp{
	public static void main(String[] args){
		Rectangle rct1 = new Rectangle(4, 40);
		System.out.println("Width is " + rct1.getWidth());
		System.out.println("Height is " + rct1.getHeight());
		System.out.println("Area is " + rct1.getArea());
		System.out.println("Perimeter is " + rct1.getPerimeter());
		Rectangle rct2 = new Rectangle(3.5, 35.9);
		System.out.println("Width is " + rct2.getWidth());
		System.out.println("Height is " + rct2.getHeight());
		System.out.println("Area is " + rct2.getArea());
		System.out.println("Perimeter is " + rct2.getPerimeter());
		
	}
}