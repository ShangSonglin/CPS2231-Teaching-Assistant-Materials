public class Stock{
	String symbol;
	String name;
	double previousClosingPrice;
	double currentPrice;
	public Stock(){}
	public Stock(String symbol, String name, double previousClosingPrice, double currentPrice){
		this.symbol = symbol;
		this.name = name;
		this.previousClosingPrice = previousClosingPrice;
		this.currentPrice = currentPrice;
	}
	public double getChangePercent(){
		return ((currentPrice - previousClosingPrice) / previousClosingPrice) * 100 ;
	}
	
	public void setSymbol(String symbol){
		this.symbol = symbol;		
	}
	public String getSymbol(){
		return symbol;
	}
	public void setName(String name){
		this.name = name;
	}
	public String getName(){
		return name;
	}
	public void setPreviousClosingPrice(double previousClosingPrice){
		this.previousClosingPrice = previousClosingPrice;
	}
	public double getPreviousClosingPrice(){
		return previousClosingPrice;
	}
	public void setCurrentPrice(double currentPrice){
		this.currentPrice = currentPrice;
	}
	public double getCurrentPrice(){
		return currentPrice;
	}
}