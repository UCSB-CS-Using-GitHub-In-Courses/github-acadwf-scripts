

import java.util.Scanner;

/**
   A Text UI for playing Tic Tac Toe

<pre>
bash-4.1 $ java PlayTicTacToeAscii

 1|2|3	  | | 	
--+-+-- --+-+-- 
 4|5|6	  | | 	
--+-+-- --+-+-- 
 7|8|9    | | 

Player X, select square > 5 

 1|2|3	  | | 	
--+-+-- --+-+-- 
 4|5|6	  |X| 	
--+-+-- --+-+-- 
 7|8|9    | | 

Player O, select square > 7 

 1|2|3	  | | 	
--+-+-- --+-+-- 
 4|5|6	  |X| 	
--+-+-- --+-+-- 
 7|8|9   O| | 

Player X, select square > 

etc.

Until either 

Draw (all squares filled)

or 

Player X  wins!
Player O  wins!
</pre>

  
   @author Phill Conrad
   @version CS56 lecture notes 02.02.2011
   @see TicTacToeGridTest
 */
public class TextTicTacToe
{
    
    public static void main(String [] args) {
	
	Scanner sc = new Scanner(System.in);
	boolean done = false;
	char winner=' ';
	
	// TicTacToeGrid implements TicTacToeGame
	TicTacToeGame g = new TicTacToeGrid();
	
	while (!done) {
	   System.out.println(g); // g.toString() implicitly invoked
	   System.out.print(g.getTurn() + "'s move: ");
	   String line  = sc.nextLine();
	 
	   int num = 0;
	   try {
	       num = Integer.parseInt(line);
	       if (g.isBlank(num)) {
		   winner = g.move(num);		   
		   done = (winner!=' ');
	       }
	       else
		   System.out.println("Space " + num + " is already occupied");
	   } catch ( NumberFormatException nfe ) {
	       System.out.println("You entered: " + line);
	       System.out.println("Instead, please enter a number between 1 and 9 of a space not occupied.");
	   }
	   
	}
	System.out.println(g); // g.toString() implicitly invoked
	if (winner=='D')
	    System.out.println("Game was a draw");
	else if (winner!=' ')
	    System.out.println(winner + " wins!");
	System.out.println("Goodbye!");
    }

}
