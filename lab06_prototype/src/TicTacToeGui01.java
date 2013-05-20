
import javax.swing.JFrame;
import java.awt.ComponentOrientation;

/** TicTacToeGui01.java is a GUI interface for TicTacToe that uses
    System.out as the destination for messages.

     @author P. Conrad
     @version CS56, Spring 2011, UCSB
*/

public class TicTacToeGui01 {

    /** main method to fire up a JFrame on the screen  
          @param args not used
     */

    public static void main (String[] args) {
       JFrame frame = new JFrame() ;
       frame. setDefaultCloseOperation(JFrame. EXIT_ON_CLOSE) ;
       
       // since TicTacToeGrid implements the TicTacToeGame interface,
       // we can use TicTacToeGame on left hand side.

       TicTacToeGame game = new TicTacToeGrid();
       MessageDestination md = new SystemOutMessageDestination();

       TicTacToeComponent tttc = new TicTacToeComponent(game, md);
       frame.getContentPane().add(tttc);

       // to make sure that grids go left to right, no matter what

       frame .applyComponentOrientation(ComponentOrientation.LEFT_TO_RIGHT);
       frame. setSize(300,300) ;
       frame. setVisible(true) ;
    }
}
