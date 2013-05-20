
import java.awt.GridLayout;
import javax.swing.JComponent;
import javax.swing.JButton;
import java.awt.event.ActionListener;
import java.awt.event. ActionEvent;
import java.awt.Font;
import java.util.ArrayList;
import javax.swing.JTextArea;

/**
 * An Swing component for playing tic tac toe

<pre>
 1|2|3 
--+-+--
 4|5|6 
--+-+--
 7|8|9 
</pre>

  
   @author Phill Conrad
   @version CS56 Spring 2011
   @see TicTacToeGrid
 */
public class TicTacToeComponent extends JComponent
{
    private TicTacToeGame game;
    private MessageDestination md;

    private JButton [] buttons = new JButton[10];

    /** Constructor
	
	@param game an object that implements the TicTacToeGame interface to keep track
	            of the moves in each game, ensuring the rules are followed and detecting
	            when someone has won.
	@param md an object that implements the MessageDestination interface.  This is just
	           a place to send any messages that need to be communicated to the user.
		   Making this separate allows a user of this components to decide to
		   send those messages to the console, or to a variety of different
		   swing Widgets, or even to a web page, as needed.
    */
       
    public TicTacToeComponent(TicTacToeGame game, MessageDestination md) {
	super(); // is this line necessary?  what does it do?
	
	this.game = game;  // the TicTacToe game
	this.md = md;  // a place we can write messages to

	// note columns ignored when rows are set
	// number of columns is implicit from the number of things added

	this.setLayout(new GridLayout(3,0)); 
	for(int i=1; i<=9; i++) {
	    String label=String.format("%d",i);
	    JButton jb = new JButton(label);
	    buttons[i] = jb;
	    jb.addActionListener(new ButtonListener(i));
	    this.add(jb);
	}
	
    }    


    class ButtonListener implements ActionListener {
	private int num;

	public ButtonListener(int i) {
	    super();  // is this line necessary? what does it do?
	    this.num = i;
	}

	public void actionPerformed (ActionEvent event) {
	    char turn=game.getTurn();
	    if (turn==' ')
		return;
	    if (!game.isBlank(num)) {		
		md.append("That square is already occupied!\n");
		return;
	    }	    
	    char winner=game.move(num);
	    JButton jb = buttons[num];
	    jb.setFont(new Font("sansserif",Font.BOLD,36));
	    jb.setText(Character.toString(turn)); // this is how we convert char to String

	    // check for a winner
	    if (winner=='D')
		md.append("Phooey.  It's a draw.\n");
	    else if (winner!=' ')
		md.append(winner + " wins!\n");
	}
    }

}
