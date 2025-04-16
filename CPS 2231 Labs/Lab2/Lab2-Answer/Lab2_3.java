import java.util.Scanner;
/*Purpose: 
* Find the Starting Point of a Cycle in an Array Jump Path
* An array records the paths of the maze
* Each element in the array represents the next index to jump to (starting from 0)
* Determine if there is a cycle in the path. 
* If a cycle exists, return the starting index of the cycle; 
* if not, return -1
*/
public class Lab2_3{
	public static int meetNode(int[] nums){
		if (nums.length == 0){
			return -1;
		}
		int slow = 0;
		int fast = 0;
		while (true) {
            // Check if fast or fast's next step goes out of bounds
            if (fast >= nums.length || nums[fast] >= nums.length) {
                return -1;
            }
			slow = nums[slow];
			fast = nums[nums[fast]];
			if (slow == fast){
				return fast;
			}
		}
	}
	
	public static int findCycleStart(int[] nums){
		/*The # of steps from head to the start of the cycle = 
		the # of steps from meeting point to the start of the cycle*/
		int headPointer = 0;
		int meetNode = meetNode(nums);
		if (meetNode == -1){
			return -1;
		}
		while (headPointer != meetNode){
			headPointer = nums[headPointer];
			meetNode = nums[meetNode];
		}
		return headPointer;
		
	}
	
	 public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.nextLine().trim();
        String[] parts = input.split("\\s+");
        int[] nums = new int[parts.length];
        for (int i = 0; i < parts.length; i++) {
            nums[i] = Integer.parseInt(parts[i]);
        }
        int result = findCycleStart(nums);
        System.out.println(result);
    }
}