/*Purpose:
creates two Fan objects. 
Assign maximum speed, radius 10, color yellow, and turn it on to the first object. 
Assign medium speed, radius 5, color blue, and turn it off to the second object. 
Display the objects by invoking their toString method.
*/
public class FanApp{
	public static void main(String[] args){
		Fan fan1 = new Fan();
		fan1.setSpeed(Fan.FAST);
		fan1.setOn(true);
		fan1.setRadius(10);
		fan1.setColor("yellow");
		System.out.println(fan1);
		
		Fan fan2 = new Fan();
		fan2.setSpeed(Fan.MEDIUM);
		fan2.setOn(false);
		fan2.setRadius(5);
		fan2.setColor("blue");
		System.out.println(fan2);
	}
}