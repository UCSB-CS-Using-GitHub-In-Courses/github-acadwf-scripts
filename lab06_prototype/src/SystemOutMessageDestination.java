

/**
 An interface to represent a place to send messages.  Used in TicTacToeComponent
  
   @author Phill Conrad
   @version CS56 lecture notes 02.02.2011
   @see TicTacToeComponent
 */
public class SystemOutMessageDestination implements MessageDestination
{
    /** 
	Get this string to the user via System.out
	@param msg message to display to user
     */

    public void append(String msg) {
	System.out.println(msg);
    }

}

