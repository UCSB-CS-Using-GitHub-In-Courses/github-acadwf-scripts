
import javax.swing.JTextArea;

/**
 A JTextArea object that implements the MessageDestination interface.
 Used in TicTacToeComponent.
  
   @author Phill Conrad
   @version CS56 lecture notes 02.02.2011
   @see TicTacToeComponent
 */
public class JTextAreaMessageDestination extends JTextArea implements MessageDestination
{
    /** 
	Create a JTextArea that implements the MessageDestination interface.  This is a direct
	pass-thru to the JTextArea constructor.

	@param rows (see documentation for javax.swing.JTextArea)
	@param cols (see documentation for javax.swing.JTextArea)
	@see javax.swing.JTextArea
    */
	
    public JTextAreaMessageDestination(int rows, int cols) {
	super(rows, cols);
    }

    // there is already a public void append(String msg); method in JTextArea
    // so that's all we have to do.
}

