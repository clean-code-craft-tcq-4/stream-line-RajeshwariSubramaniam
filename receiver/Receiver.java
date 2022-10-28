package receiver;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Scanner;

public class Receiver {
	public  void reeciverLogic() {
		HashMap<String, ArrayList<Float>> paramData = readData();
		PrintStatistics stats=new PrintStatistics();
		// For each param print min, max and simple moving average of 5 values
		paramData.forEach((key, value) -> {
			printLine();
			printMessage("For param: " + key);
			stats.printMinMax(key, value);
			printMessage("The simple moving average for 5 values is ");
			stats.printSimpleMovingAverage(value, 5);
			printMessage("\n");
			printLine();
		});
	}
public printLine()
{
	printMessage("****************************************************************");
}
	
	public  HashMap<String, ArrayList<Float>> readData() {
		Scanner sc = new Scanner(System.in);
		// sender data to be provided as input from console

		String data = new String();
		for (int i = 0; i < 100; i++)
			data += sc.nextLine() + "\n";
		String[] eachLine = data.split("\n");
		List<String> stringList = Arrays.asList(eachLine);
		HashMap<String, ArrayList<Float>> paramMap = new HashMap<String, ArrayList<Float>>();
		stringList.forEach(entry -> {
			String param = entry.substring(0, entry.indexOf(":"));
			Float paramValue = Float.valueOf(entry.substring(entry.indexOf(":") + 1, entry.length()));
			// map is empty or map is not empty but does not have param
			if (paramMap.isEmpty() || !paramMap.containsKey(param)) {
				ArrayList<Float> list = new ArrayList<Float>();
				list.add(paramValue);
				paramMap.put(param, list);
			}
			// map has param value already in it
			else if (paramMap.containsKey(param)) {
				ArrayList<Float> list = paramMap.get(param);
				list.add(paramValue);
				paramMap.put(param, list);

			}

		});

		return paramMap;
	}

	public static void printMessage(String content) {
		System.out.println(content);
	}
}
