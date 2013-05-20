
/**
 * A grid for playing tic tac toe, with numbers as shown here:

<pre>
 1|2|3 
--+-+--
 4|5|6 
--+-+--
 7|8|9 
</pre>

  
   @author Phill Conrad
   @version CS56 lecture notes 02.02.2011
   @see TicTacToeGridTest
 */
public class TicTacToeGrid implements TicTacToeGame
{

    // instance variables 
    private String grid="_          "; 
    private int numMoves=0;
    private char turn = 'X';
    private char winner = ' ';
    private boolean gameOver = false;
    
    /**
     * Default constructor for objects of class TicTacToeGrid
     */
    public TicTacToeGrid() {}

    /**
     Constructor for objects of class TicTacToeGrid that allows
     creation of games in middle of play.  This is mostly for testing.

     There should be an equal number of Xs and Os
     (in which case it is Xs turn) or else
     1 more X than there are Os (in which case it is Os turn),
     otherwise IllegalArgumentException("illegal game state") is thrown.
     
     @param gameState nine character string with Xs and Os for positions 1-9

     */
    public TicTacToeGrid(String gameState) {
	this.setGameState(gameState);
    }


    public char getTurn() { 
	// return 'Q'; // stub
	return turn;
    }

    /** 
	@param i is number of square (like telephone pad)
	@return 'X','O', or ' '--i.e. contents of square i
     */

    public char charAt(int i) { return grid.charAt(i);}


    /** 
	nonBlankMatch checks spaces i,j,k to see if they all match.  
	i,j,k must be distinct, and strictly
	increasing (i.e. i<j, j<k), otherwise an IllegalArgumentException
	will be thrown.

	@return 'X' or 'O' if the three spaces are non-zero and all match
	@param i space to check
	@param j space to check
	@param k space to check
     */

    public char nonBlankMatch(int i, int j, int k) {
	return '?'; // stub
    }
    
    /** This private convenience method sets the gameOver and winner variables,
	and then returns the winner.  It is simply a way to factor out
	common code from all the cases in getWinner */
	
    private char setWinner(char c) {
	this.gameOver = true;
	this.winner = c;
	this.turn = ' ';
	return c;
    }

    /** 
	@return 'X' or 'O' if there is a winner, ' ' if there is not
     */

    public char getWinner() {
	char result;

	if (gameOver)
	    return winner;

	// horizontal
	result = nonBlankMatch(1,2,3);
	if (result != ' ')  return this.setWinner(result); 
	result = nonBlankMatch(4,5,6);
	if (result != ' ')  return this.setWinner(result); 
	result = nonBlankMatch(7,8,9);
	if (result != ' ')  return this.setWinner(result) ;

	// vertical
	result = nonBlankMatch(1,4,7);
	if (result != ' ') return this.setWinner(result);
	result = nonBlankMatch(2,5,8);
	if (result != ' ') return this.setWinner(result);
	result = nonBlankMatch(3,6,9);
	if (result != ' ') return this.setWinner(result);

	// diagonal
	result = nonBlankMatch(1,5,9);
	if (result != ' ') return this.setWinner(result);
	result = nonBlankMatch(3,5,7);
	if (result != ' ') return this.setWinner(result);
	
	// there is no winner yet.  

	if (numMoves == 9) return this.setWinner('D'); // draw

	return ' '; // no winner yet
    }
    

    /** is this square blank.  Should be called before move() to see
	whether the move is legal.  

	

	@param i number between 1 and 9 indicating square
	@return whether square is blank or not.
	@throws IllegalArgumentException if i is not between 1 and 9 (inclusive)
    */
    public boolean isBlank(int i) {
	return false; // STUB!!!
    }

    /** 
	play the next move. if isBlank(i) is not true, will throw
	TicTacToeIllegalMoveException

	@param i number between 1 and 9 indicating square, 
	       organized like a telephone grid.  If i is already occupied,
	       a TicTacToeIllegalMoveException is thrown.
	@return winner 'X', 'O', or 'D' for draw, or ' ' for none yet.
     */
    public char move(int i) throws TicTacToeIllegalMoveException { 
	/* indexes go from 0 to 9. 
	   Second substring has 10 as last param because second param
	   to substring is first index NOT included in subsequence.
	*/
	if (!this.isBlank(i))
	    throw new TicTacToeIllegalMoveException("Square " + i + " occupied");
	grid = grid.substring(0,i) + turn + grid.substring(i+1,10);
	turn = (turn=='X')?'O':'X'; // change turn
	numMoves++;		
	
	return this.getWinner(); // may change gameOver and winner as side effect
    }

    /** For testing only, this method sets the entire game
	state in one method.   

	Any previous game state is overwritten. 
	
	There should be an equal number of Xs and Os
	(in which case it is Xs turn) or else
	1 more X than there are Os (in which case it is Os turn),
	otherwise IllegalArgumentException("illegal game state") is thrown.
       
	See testcases in TicTacToeGridTest.java for examples of
	how this is used.

	@param gameState nine character string with Xs and Os for positions 1-9
	@see TicTacToeGridTest

    */
    public void setGameState (String gameState) {

	// first, check if gameState is legal

	if (gameState.length()!=9)
	    throw new IllegalArgumentException("gameState should be 9 chars long");

	int numXs=0;
	int numOs=0;
	for (int i=0; i<gameState.length(); i++) {
	    char c = gameState.charAt(i);
	    switch (c) {
		case 'X': numXs++; break;
		case 'O': numOs++; break;
		case ' ': break;
		default: 
		    throw new IllegalArgumentException
			("Bad char " + c + " at position " + i);
		}
	}

	if (numXs==numOs) {
	    turn = 'X';
	} else if (numXs == numOs + 1) {
	    turn = 'O';
	} else {
	    throw new IllegalArgumentException
		(numXs + " Xs and " + numOs + " Os");
	}
	this.grid = "_" + gameState;

	// All other game variables should be updated to reflect
	// the state represented in the string.

	this.numMoves = numXs + numOs;
	this.gameOver = false;
	this.winner = ' ';
	this.getWinner(); // may reset winner, gameOver, and turn as side effects
    }

    /** Return game state as a 9 character string.
	This is mostly for testing purposes.

	@return game state string
    */

    public String getGameState() {
	return grid.substring(1,10);
    }


    /** 
	return the TicTacToe grid with the contents, and
	a representation of the numbers beside it (4 spaces over)
    */

    public String toString() {

	final String gridLine = "--+-+--";
	final String lines[] = { " 1|2|3 "," 4|5|6 "," 7|8|9 "};

	String result = "";

	for (int i=0;i<3;i++) {
	    result += (" " + this.charAt(i*3 + 1)); // a space then the number
	    result += ("|" + this.charAt(i*3 + 2) + "|"); // |d| where d is the number
	    result += (this.charAt(i*3 + 3) + " "); // number then a space
	    // four spaces, then the example grid
	    result += ("    " + lines[i]) + "\n";
	    if (i<2)
		result += gridLine + "    " + gridLine + "\n";
	}

	return result;
    }

   
}
