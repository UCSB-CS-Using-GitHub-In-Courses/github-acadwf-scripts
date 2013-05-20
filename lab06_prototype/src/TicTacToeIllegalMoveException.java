/**
   An exception for illegal moves in TicTacToe, used in TicTacToeGrid
   (its an unchecked exception, so it extends  RuntimeException rather than Exception)

   @author Phill Conrad
   @version CS56 Spring 2011, UCSB
   @see TicTacToeGrid
 */
public class TicTacToeIllegalMoveException extends RuntimeException {

    // We must declare this constructor if we want it to exist
    // since we declared the other one, this one won't get made automatically.

    public TicTacToeIllegalMoveException () {};

    // We must declare this constructor if we want to be able to create
    // instances with messages, because we have to pass the message to the 
    // superclass (parent) constructor.

    public TicTacToeIllegalMoveException (String message) {
	super(message);
    }
}
