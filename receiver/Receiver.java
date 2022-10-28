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
		// For each param print min, max and simple moving average of 5 values
		paramData.forEach((key, value) -> {
			printMessage("****************************************************************");
			printMessage("For param: " + key);
			printMinMax(key, value);
			printMessage("The simple moving average for 5 values is ");
			printSimpleMovingAverage(value, 5);
			printMessage("\n");
			printMessage("****************************************************************");
		});
	}

	private static void printSimpleMovingAverage(ArrayList<Float> value, int period) {

		int i;
		float sum = 0;

		// Initial sum of period elements.
		for (i = 0; i < period; i++) {
			sum += value.get(i);
			System.out.printf("%.2f ", sum / period);
		}

		// Compute MA from index K
		for (i = period; i < value.size(); i++) {
			sum -= value.get(i - period);
			sum += value.get(i);
			System.out.printf("%.2f ", sum / period);
		}
	}

	public static void printMinMax(String param, ArrayList<Float> paramValues) {

		printMessage("The min and max values respectively are min=" + Collections.min(paramValues) + " and max="
				+ Collections.max(paramValues));
	};

	public static HashMap<String, ArrayList<Float>> readData() {
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
