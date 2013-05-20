

/**
 An interface to represent a place to send messages.
 Used in TicTacToeCompoment
  
   @author Phill Conrad
   @version CS56 lecture notes 02.02.2011
   @see TicTacToeComponent
 */
public interface MessageDestination
{
    /** 
	Get this string to the user
	@param msg String to send to the user
     */

    public void append(String msg);

}

