
import javax.swing.JFrame;
import java.awt.ComponentOrientation;
import javax.swing.JTextArea;
import javax.swing.JScrollPane;
import javax.swing.JScrollPane;
import javax.swing.ScrollPaneConstants;
import java.awt.BorderLayout;

/** TicTacToeGui01.java is a GUI interface for TicTacToe that uses
    System.out as the destination for messages.

     @author P. Conrad
     @version CS56, Spring 2011, UCSB
*/


public class TicTacToeGui02 {

    /** main method to fire up a JFrame on the screen  
          @param args not used
     */

    public static void main (String[] args) {
       JFrame frame = new JFrame() ;
       frame. setDefaultCloseOperation(JFrame. EXIT_ON_CLOSE) ;


       // A JTextArea (see p. 414-415 of textbook)
       JTextAreaMessageDestination text = new JTextAreaMessageDestination(10,30);
       JScrollPane scroller = new JScrollPane(text);
       scroller.setVerticalScrollBarPolicy(ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS);
       scroller.setHorizontalScrollBarPolicy(ScrollPaneConstants.HORIZONTAL_SCROLLBAR_NEVER);
       frame.getContentPane().add(BorderLayout.SOUTH,scroller);
       
       // since TicTacToeGrid implements the TicTacToeGame interface,
       // we can use TicTacToeGame on left hand side.

       TicTacToeGame game = new TicTacToeGrid();
       TicTacToeComponent tttc = new TicTacToeComponent(game,text);
       frame.getContentPane().add(tttc);


       // to make sure that grids go left to right, no matter what

       frame .applyComponentOrientation(ComponentOrientation.LEFT_TO_RIGHT);
       frame. setSize(300,500) ;
       frame. setVisible(true) ;
    }
}
