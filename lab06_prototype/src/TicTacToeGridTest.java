
import org.junit.Test;
import static org.junit.Assert.assertEquals;

/**
 * The test class TicTacToeGridTest -- it tests the TicTacToeGrid class
 *
 * @author Phill Conrad (maybe some help from the students)
 * @version CS56 lecture notes 02.02.2011
 * @see TicTacToeGrid
 */
public class TicTacToeGridTest
{
    @Test public void testConstructor01()
    {
        // set up a grid with the constructor, and
        // then make sure that X's turn is first.
        
        TicTacToeGrid g = new TicTacToeGrid();
	for (int i=1;i<=9;i++)
	    assertEquals(' ',g.charAt(i));
	assertEquals('X',g.getTurn());
    }

    @Test public void testCharAt01()
    {
        TicTacToeGrid g = new TicTacToeGrid("XOX"+
					    "OXO"+
					    "XOX");
	for (int i=1;i<=9;i++) {
	    assertEquals((i%2==1)?'X':'O',g.charAt(i));
	}
    }
    @Test public void testCharAt02() {
        TicTacToeGrid g = new TicTacToeGrid("OXO"+
					    "XOX"+
					    "   ");
	for (int i=1;i<=6;i++) {
	    assertEquals((i%2==1)?'O':'X',g.charAt(i));
	}
	for (int i=7;i<=9;i++) {
	    assertEquals(' ',g.charAt(i));
	}	
    }

    @Test public void testMove01()
    {
        TicTacToeGrid g = new TicTacToeGrid();
	assertEquals(' ',g.getWinner());
	assertEquals('X',g.getTurn()); 

	g.move(5); 
	assertEquals("   "+
		     " X "+
		     "   ", g.getGameState());
	assertEquals(' ',g.getWinner());
    }

    @Test public void testMove02()
    {
        TicTacToeGrid g = new TicTacToeGrid();
	assertEquals(' ',g.getWinner());
	assertEquals('X',g.getTurn()); 

	g.move(5); 
	assertEquals("   "+
		     " X "+
		     "   ", g.getGameState());
	assertEquals(' ',g.getWinner());

	assertEquals('O',g.getTurn()); 
	g.move(7); 
	assertEquals("   "+
		     " X "+
		     "O  ", g.getGameState());
	assertEquals(' ',g.getWinner());

	assertEquals('X',g.getTurn()); 
	g.move(8); 
	assertEquals("   "+
		     " X "+
		     "OX ", g.getGameState());
	assertEquals(' ',g.getWinner());

	assertEquals('O',g.getTurn()); 
	g.move(4); 
	assertEquals("   "+
		     "OX "+
		     "OX ", g.getGameState());	
	assertEquals(' ',g.getWinner());


	assertEquals('X',g.getTurn()); 
	g.move(2); 
	assertEquals(" X "+
		     "OX "+
		     "OX ", g.getGameState());
	assertEquals('X',g.getWinner());
    }

    @Test public void testToString01()
    {
        TicTacToeGrid g = new TicTacToeGrid();
	assertEquals(' ',g.getWinner());
	assertEquals('X',g.getTurn()); 
	assertEquals(("  | |       1|2|3 \n" +
		      "--+-+--    --+-+--\n" +
		      "  | |       4|5|6 \n" +
		      "--+-+--    --+-+--\n" +
		      "  | |       7|8|9 \n" ),g.toString());
    }
		     
		     
    @Test public void testToString02()
    {
        TicTacToeGrid g = new TicTacToeGrid();
	assertEquals(("  | |       1|2|3 \n" +
		      "--+-+--    --+-+--\n" +
		      "  | |       4|5|6 \n" +
		      "--+-+--    --+-+--\n" +
		      "  | |       7|8|9 \n" ),g.toString());
	g.move(5); 
	assertEquals(("  | |       1|2|3 \n" +
		      "--+-+--    --+-+--\n" +
		      "  |X|       4|5|6 \n" +
		      "--+-+--    --+-+--\n" +
		      "  | |       7|8|9 \n" ),g.toString());
	g.move(9); 
	assertEquals(("  | |       1|2|3 \n" +
		      "--+-+--    --+-+--\n" +
		      "  |X|       4|5|6 \n" +
		      "--+-+--    --+-+--\n" +
		      "  | |O      7|8|9 \n" ),g.toString());
	g.move(8); 
	assertEquals(("  | |       1|2|3 \n" +
		      "--+-+--    --+-+--\n" +
		      "  |X|       4|5|6 \n" +
		      "--+-+--    --+-+--\n" +
		      "  |X|O      7|8|9 \n" ),g.toString());
	g.move(4); 
	assertEquals(("  | |       1|2|3 \n" +
		      "--+-+--    --+-+--\n" +
		      " O|X|       4|5|6 \n" +
		      "--+-+--    --+-+--\n" +
		      "  |X|O      7|8|9 \n" ),g.toString());
	g.move(1); 
	assertEquals((" X| |       1|2|3 \n" +
		      "--+-+--    --+-+--\n" +
		      " O|X|       4|5|6 \n" +
		      "--+-+--    --+-+--\n" +
		      "  |X|O      7|8|9 \n" ),g.toString());
	g.move(6); 
	assertEquals((" X| |       1|2|3 \n" +
		      "--+-+--    --+-+--\n" +
		      " O|X|O      4|5|6 \n" +
		      "--+-+--    --+-+--\n" +
		      "  |X|O      7|8|9 \n" ),g.toString());
	g.move(3); 
	assertEquals((" X| |X      1|2|3 \n" +
		      "--+-+--    --+-+--\n" +
		      " O|X|O      4|5|6 \n" +
		      "--+-+--    --+-+--\n" +
		      "  |X|O      7|8|9 \n" ),g.toString());

    }



    @Test public void testNoWinner01()
    {
        TicTacToeGrid g = new TicTacToeGrid();
	assertEquals('X',g.getTurn()); g.move(5); 
	assertEquals('O',g.getTurn()); g.move(7); 
	assertEquals("   "+
		     " X "+
		     "O  ", g.getGameState());
	assertEquals(' ',g.getWinner());	
	// make sure it is now Xs turn again
	assertEquals('X',g.getTurn());	
    }


    @Test public void testNoWinner02()
    {
        TicTacToeGrid g = new TicTacToeGrid
	    ("OXX"+
	     "XOO"+
	     "OXX");	
	assertEquals('D',g.getWinner());
	// if game over, turn should be blank
	assertEquals(' ',g.getTurn());	
    }

    @Test public void testNoWinner03()
    {
        TicTacToeGrid g = new TicTacToeGrid();
	assertEquals(' ',g.getWinner());	
    }

    @Test public void testOWinsHoriz01()
    {
        TicTacToeGrid g = new TicTacToeGrid
	    ("OOO"+
	     "X X"+
	     " X ");	
	assertEquals('O',g.getWinner());	
	// if game over, turn should be blank
	assertEquals(' ',g.getTurn());	
    }

    @Test public void testOWinsHoriz02()
    {
        TicTacToeGrid g = new TicTacToeGrid
	    ("X X"+
	     "OOO"+
	     " X ");	
	assertEquals('O',g.getWinner());
	// if game over, turn should be blank
	assertEquals(' ',g.getTurn());		
    }

    @Test public void testOWinsHoriz03()
    {
        TicTacToeGrid g = new TicTacToeGrid
	    ("X X"+
	     "X  "+
	     "OOO");	

	assertEquals('O',g.getWinner());	
	// if game over, turn should be blank
	assertEquals(' ',g.getTurn());	
    }


    @Test public void testXWinsHoriz01()
    {
        TicTacToeGrid g = new TicTacToeGrid
	    ("XXX"+
	     "O  "+
	     "O O");	
	assertEquals('X',g.getWinner());
	// if game over, turn should be blank
	assertEquals(' ',g.getTurn());		
    }

    @Test public void testXWinsHoriz02()
    {
        TicTacToeGrid g = new TicTacToeGrid
	    ("O O"+
	     "XXX"+
	     "O  ");	
	assertEquals('X',g.getWinner());
	// if game over, turn should be blank
	assertEquals(' ',g.getTurn());		
    }

    @Test public void testXWinsHoriz03()
    {
        TicTacToeGrid g = new TicTacToeGrid
	    (" OO"+
	     "  O"+
	     "XXX");

	assertEquals('X',g.getWinner());
	// if game over, turn should be blank
	assertEquals(' ',g.getTurn());		
    }


    @Test public void testOWinsVert01()
    {
        TicTacToeGrid g = new TicTacToeGrid
	    ("O X"+
	     "O  "+
	     "OXX");

	assertEquals('O',g.getWinner());
	// if game over, turn should be blank
	assertEquals(' ',g.getTurn());		
    }

    @Test public void testOWinsVert02()
    {
        TicTacToeGrid g = new TicTacToeGrid
	    ("XOX"+
	     "XO "+
	     " O ");

	assertEquals('O',g.getWinner());
	// if game over, turn should be blank
	assertEquals(' ',g.getTurn());		
    }

    @Test public void testOWinsVert03()
    {
        TicTacToeGrid g = new TicTacToeGrid
	    ("X O"+
	     "X O"+
	     " XO");

	assertEquals('O',g.getWinner());
	// if game over, turn should be blank
	assertEquals(' ',g.getTurn());		
    }

    @Test public void testXWinsVert01()
    {
        TicTacToeGrid g = new TicTacToeGrid
	    ("X  "+
	     "XO "+
	     "XOO");

	assertEquals('X',g.getWinner());
	// if game over, turn should be blank
	assertEquals(' ',g.getTurn());		
    }

    @Test public void testXWinsVert02()
    {
        TicTacToeGrid g = new TicTacToeGrid
	    ("XXO"+
	     " X "+
	     "OXO");

	assertEquals('X',g.getWinner());
	// if game over, turn should be blank
	assertEquals(' ',g.getTurn());		
    }

    @Test public void testXWinsVert03()
    {
        TicTacToeGrid g = new TicTacToeGrid
	    ("O X"+
	     "X X"+
	     "OOX");

	assertEquals('X',g.getWinner());
	// if game over, turn should be blank
	assertEquals(' ',g.getTurn());		
    }

    @Test public void testOWinsDiag01()
    {
        TicTacToeGrid g = new TicTacToeGrid
	    ("OXX"+
	     "XO "+
	     "XOO");

	assertEquals('O',g.getWinner());
	// if game over, turn should be blank
	assertEquals(' ',g.getTurn());		
    }
    @Test public void testOWinsDiag02()
    {
        TicTacToeGrid g = new TicTacToeGrid
	    ("X O"+
	     "XO "+
	     "OX ");

	assertEquals('O',g.getWinner());
	// if game over, turn should be blank
	assertEquals(' ',g.getTurn());		
    }

    @Test public void testXWinsDiag01()
    {
        TicTacToeGrid g = new TicTacToeGrid
	    ("X  "+
	     " X "+
	     "OOX");

	assertEquals('X',g.getWinner());
	// if game over, turn should be blank
	assertEquals(' ',g.getTurn());		
    }

    @Test public void testXWinsDiag02()
    {
        TicTacToeGrid g = new TicTacToeGrid
	    ("  X"+
	     " X "+
	     "XOO");

	assertEquals('X',g.getWinner());
	// if game over, turn should be blank
	assertEquals(' ',g.getTurn());		
    }


    @Test(expected=IllegalArgumentException.class)
	public void testBadParamToConstructor01() {
	
	TicTacToeGrid g = new TicTacToeGrid("AAA"+
					    "BBB" +
					    "CCC");
    }
    
    @Test(expected=IllegalArgumentException.class)
	public void testBadParamToConstructor02() {
	
	TicTacToeGrid g = new TicTacToeGrid("XXX"+
					    "   " +
					    "   ");
    }

    @Test(expected=IllegalArgumentException.class)
	public void testBadParamToConstructor03() {
	
	TicTacToeGrid g = new TicTacToeGrid("O  "+
					    "   " +
					    "   ");
    }

    @Test(expected=IllegalArgumentException.class)
	public void testBadParamToConstructor04() {
	
	TicTacToeGrid g = new TicTacToeGrid("OXO"+
					    "   " +
					    "   ");
    }

    @Test(expected=IllegalArgumentException.class)
	public void testBadParamToConstructor05() {	
	TicTacToeGrid g = new TicTacToeGrid("");
    }

    @Test(expected=IllegalArgumentException.class)
	public void testIllegalArgumentIsBlank01() {	
	TicTacToeGrid g = new TicTacToeGrid();
	boolean result = g.isBlank(0);
    }

    @Test(expected=IllegalArgumentException.class)
	public void testIllegalArgumentIsBlank02() {	
	TicTacToeGrid g = new TicTacToeGrid();
	boolean result = g.isBlank(10);
    }

    @Test(expected=TicTacToeIllegalMoveException.class)
	public void testIllegalMove01() {	
	TicTacToeGrid g = new TicTacToeGrid();
	g.move(1);
	g.move(1);
    }

    @Test(expected=TicTacToeIllegalMoveException.class)
	public void testIllegalMove02() {	
	TicTacToeGrid g = new TicTacToeGrid("   "+
					    "   "+
					    "  X");
	g.move(9);
    }

    @Test(expected=IllegalArgumentException.class)
	public void testNonBlankMatchIllegalArg01() {	
	TicTacToeGrid g = new TicTacToeGrid("XXX"+
					    "O O"+
					    " OX");
	char result = g.nonBlankMatch(1,1,1);
    }

    @Test(expected=IllegalArgumentException.class)
	public void testNonBlankMatchIllegalArg02() {	
	TicTacToeGrid g = new TicTacToeGrid("XXX"+
					    "O O"+
					    " OX");
	char result = g.nonBlankMatch(1,2,2);
    }

    @Test(expected=IllegalArgumentException.class)
	public void testNonBlankMatchIllegalArg03() {	
	TicTacToeGrid g = new TicTacToeGrid("XXX"+
					    "O O"+
					    " OX");
	char result = g.nonBlankMatch(1,2,1);
    }

    @Test(expected=IllegalArgumentException.class)
	public void testNonBlankMatchIllegalArg04() {	
	TicTacToeGrid g = new TicTacToeGrid("XXX"+
					    "O O"+
					    " OX");
	char result = g.nonBlankMatch(3,2,4);
    }

    @Test(expected=IllegalArgumentException.class)
	public void testNonBlankMatchIllegalArg05() {	
	TicTacToeGrid g = new TicTacToeGrid("XXX"+
					    "O O"+
					    " OX");
	char result = g.nonBlankMatch(3,5,3);
    }


    @Test
	public void testNonBlankMatch01() {	
	TicTacToeGrid g = new TicTacToeGrid("XXX"+
					    "O O"+
					    " OX");
	assertEquals('X',g.nonBlankMatch(1,2,3));
	
    }

    @Test
	public void testNonBlankMatch02() {	
	TicTacToeGrid g = new TicTacToeGrid("XXX"+
					    "O O"+
					    " OX");
	// g.nonBlankMatch doesn't require them to be in a legal tic tac toe 
	// configuration
	assertEquals('O',g.nonBlankMatch(4,6,8));
    }

    @Test
	public void testNonBlankMatch03() {	
	TicTacToeGrid g = new TicTacToeGrid("XXX"+
					    "O O"+
					    "XO ");
	assertEquals(' ',g.nonBlankMatch(1,4,7));
    }

    @Test
	public void testNonBlankMatch04() {	
	TicTacToeGrid g = new TicTacToeGrid("XXO"+
					    "X O"+
					    " OX");
	assertEquals(' ',g.nonBlankMatch(3,6,9));
    }


}

