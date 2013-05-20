
/**
 An interface for Tic Tac Toe games
  
   @author Phill Conrad
   @version CS56 lecture notes 02.02.2011
   @see TicTacToeGrid
   @see TicTacToeComponent
   @see TextTicTacToe
 */
public interface TicTacToeGame 
{
    /** returns 'X' or 'O' depending on whose turn it is.  Returns ' ' if game over.
     */
    public char getTurn(); 

    /** is this square blank.  Should be called before move() to see
	whether the move is legal.  
	@param i number between 1 and 9 indicating square
	@return whether square is blank or not.
    */
    public boolean isBlank(int i);

    /**	play the next move. if isBlank(i) is not true, will throw
	TicTacToeIllegalMoveException.

	@param i number between 1 and 9 indicating square, 
	       organized like a telephone grid.  If i is already occupied,
	       a TicTacToeIllegalMoveException is thrown.
	@return winner 'X', 'O', or 'D' for draw, or ' ' for none yet.
     */
    public char move(int i) throws TicTacToeIllegalMoveException;

    public String toString();
}
