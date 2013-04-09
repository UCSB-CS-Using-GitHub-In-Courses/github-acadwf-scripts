import org.junit.Test;
import static org.junit.Assert.assertEquals;

/** Test class for UCSBCourse

 * @author Phill Conrad
 * @author Insert your name here
 * @author If working in pair, insert 2nd pair here, otherwise delete this line
 * @version 2013/04/09 for lab02, cs56, s13
 * @see UCSBCourse

*/

public class UCSBCourseTest {

    /** Test case for UCSBCourse.getDept()
     @see UCSBCourse
    */

    @Test
	public void test_getDept() {
	UCSBCourse cs56 = new UCSBCourse("CMPSC","56",4);
	assertEquals("CMPSC",cs56.getDept());
    }

    /** Test case for UCSBCourse.getNum() 
     @see UCSBCourse
    */
    
    @Test
	public void test_getNum() {
	UCSBCourse math3a = new UCSBCourse("MATH","3A",4);
	assertEquals("3A",math3a.getNum());
    }





    


}
