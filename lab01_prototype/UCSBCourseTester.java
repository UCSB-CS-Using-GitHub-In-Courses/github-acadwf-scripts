/** UCSBCourseTester contains a simple main program to test UCSBCourse
 @author Phill Conrad
 @author @@@ INSERT YOUR NAME HERE
 @version 04/02/2013 for lab01, cs56, S13
*/

public class UCSBCourseTester {

    /** Main program to test UCSBCourse
    */

    public static void main (String [] args)  {
	
	UCSBCourse cs56 = new UCSBCourse("CMPSC","56",4);
	UCSBCourse math3a = new UCSBCourse("MATH","3A",4);
	UCSBCourse pstat120a = new UCSBCourse("PSTAT","120A",4);


	// for comparing strings, should use .equals method, not ==
	if (cs56.getDept().equals("CMPSC"))
	    System.out.println("Test 1 passed");
	else
	    System.out.println(" Test 1 FAILED");


	if (math3a.getNum().equals("3A"))
	    System.out.println("Test 2 passed");
	else
	    System.out.println(" Test 2 FAILED");

	// ok to use == for primitive data type int
	if (pstat120a.getUnits() == 4)
	    System.out.println("Test 3 passed");
	else
	    System.out.println(" Test 3 FAILED");

	if (cs56.getFullCourseName().equals("CMPSC56"))
	    System.out.println("Test 4 passed");
	else
	    System.out.println(" Test 4 FAILED");
	    	

    }

} // class UCSBCourse