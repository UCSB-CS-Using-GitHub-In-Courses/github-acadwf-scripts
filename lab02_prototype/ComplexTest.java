import org.junit.Test;
import static org.junit.Assert.assertEquals;

/**
 * A complex number with a real and imaginary part
 * 
 * @author Phill Conrad
 * @author Insert your name here
 * @author If working in pair, insert 2nd pair here, otherwise delete this line
 * @version 2013/04/09 for lab02, cs56, s13
 * @see Complex
 */

public class ComplexTest 
{
    // define a static final (a constant) for error tolerance
    // we'll pass this as the last value of every assertEquals()
    // call that is done on double values to allow for roundoff error
    
   public static final double TOL = 0.00001;
    
   @Test public void testNoArgConstructor()
    {
        // the no arg constructor should give us zero for
        // both imaginary and real parts
        Complex c = new Complex();
        assertEquals(0.0,c.getReal(),TOL);
        assertEquals(0.0,c.getImag(),TOL);
	
    }
    
   @Test public void testTwoArgConstructor()
   {
        // the no arg constructor should give us zero for
        // both imaginary and real parts
        Complex c = new Complex( 1.2, -3.4 );
        assertEquals( 1.2, c.getReal(), TOL);
        assertEquals( -3.4, c.getImag(), TOL);
    }

   @Test public void testSetters()
   {
       // the no arg constructor should give us zero for
       // both imaginary and real parts
       Complex c = new Complex();
       c.setReal(-3.4);
       c.setImag(1.2);
       assertEquals( -3.4, c.getReal(), TOL);
       assertEquals( 1.2, c.getImag(), TOL);
   }
    
    
   @Test public void testToString1()
    {
        Complex c = new Complex();
        assertEquals("0.0 + 0.0i",c.toString());
    }
    
   @Test public void testToString2()
   {
       // the no arg constructor should give us zero for
       // both imaginary and real parts
       Complex c = new Complex(1.2, -3.4);
       assertEquals("1.2 + -3.4i",c.toString());
   }
    
   @Test public void testToString3()
    {
        // the no arg constructor should give us zero for
        // both imaginary and real parts
        Complex c = new Complex(2.0, 3.0);
        assertEquals("2.0 + 3.0i",c.toString());
    }
    
}
