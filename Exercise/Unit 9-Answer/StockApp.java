/*Write a test program
 that creates a Stock object with the stock symbol ORCL, the name O racle 
 Corporation, and the previous closing price of 34.5. Set a new current price to 
 34.35 and display the price-change percentage
*/
public class StockApp{
	public static void main(String[] args){
		Stock stk = new Stock("ORCL", "0 racle Corporation", 34.5, 34.35);
		System.out.println("Symbol: " + stk.getSymbol());
		System.out.println("Name: " + stk.getName());
		System.out.println("Price-change Percentage is " + stk.getChangePercent() + "%");
	}
}