
import static org.junit.Assert.*;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

import org.junit.Test;

public class ReceiverTest {

@Test
	public void queryTestDataIsNotNull() {
		HashMap<String,ArrayList<Float>> paramData=Receiver.readData();
		assertNotNull(paramData);
	}
@Test
public void queryTestDataHasCorrectParamCount() {
	HashMap<String,ArrayList<Float>> paramData=Receiver.readData();
	assertEquals(paramData.keySet().size(),2);
}
@Test
public void queryTestDataFailsForIncorrectParamCount() {
	HashMap<String,ArrayList<Float>> paramData=Receiver.readData();
	assertNotEquals(paramData.keySet().size(),3);
}

	

}
