public class FootballPlayer {
	
	private String playerName ="";
	private String college = "";
	private double fortyYardDash = 0.0;
	private int repsBenchPress = 0;
	private double sixtyYardDash = 0.0;
	
	public String getPlayerName() { return playerName; }
	public String getCollege() { return college; }
	public double get40YdDash() { return fortyYardDash; }
	public int getRepsBenchPress() { return repsBenchPress; }
	public double get60YdDash() { return sixtyYardDash; }

    public FootballPlayer(String playerName, String college, 
			double fortyYardDash, int repsBenchPress, double sixtyYardDash){
		
		this.playerName = playerName;
		this.college = college;
		this.fortyYardDash = fortyYardDash;
		this.repsBenchPress = repsBenchPress;
		this.sixtyYardDash = sixtyYardDash;
		
	}

    public FootballPlayer(String playerName, String college, 
			double fortyYardDash, int repsBenchPress){
		
		this(playerName, college, fortyYardDash, repsBenchPress, 0.0);
		
	}
	
	public FootballPlayer(String playerName, String college, 
			double fortyYardDash, double sixtyYardDash){
		
		this(playerName, college, fortyYardDash, 0, sixtyYardDash);
		
	}
	
	public static void main(String[] args){
		
		FootballPlayer jamellFleming = new FootballPlayer2("Jamell Fleming", "Oklahoma", 4.53, 10.75);
		
		System.out.println(jamellFleming.getPlayerName());
		System.out.println(jamellFleming.getCollege());
		System.out.println(jamellFleming.get40YdDash());
		System.out.println(jamellFleming.getRepsBenchPress());
		System.out.println(jamellFleming.get60YdDash());
		
	}

}
