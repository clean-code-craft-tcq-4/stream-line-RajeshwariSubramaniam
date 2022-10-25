
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

	

}
