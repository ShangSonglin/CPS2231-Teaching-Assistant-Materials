import java.util.Random;
/*Purpose:
creates a Random object with seed 1000 
and displays the first 50 random integers between 0 and 100 using the nextInt(100) method.
*/
public class RandomApp{
	public static void main(String[] args){
		Random rd = new Random();
		rd.setSeed(1000);
		/*What is seed?
		/*If you use the same seed, the sequence of numbers from nextInt() 
		/*(or any other Random method) will always follow the same pattern.
		*/for(int i = 0; i < 50; i++){
			System.out.println(rd.nextInt(100));
		}
	}
}