import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.List;
import java.util.Scanner;

public class Receiver {
	public static void main(String[] args) {
		HashMap<String, ArrayList<Float>> paramData = readData();
		// For each param print min, max and simple moving average of 5 values
		paramData.forEach((key, value) -> {
			System.out.println("****************************************************************");
			System.out.println("For param: " + key);
			printMinMax(key, value);
			System.out.println("The simple moving average for 5 values is ");
			printSimpleMovingAverage(value, 5);
			System.out.println("\n");
			System.out.println("****************************************************************");
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

		System.out.println("The min and max values respectively are min=" + Collections.min(paramValues) + " and max="
				+ Collections.max(paramValues));
	};

	public static HashMap<String, ArrayList<Float>> readData() {
		Scanner sc = new Scanner(System.in);
		// sender data to be provided as input from console
		// for now sending hardcoded data
		// String data=sc.next();
		// System.out.println("data is:"+data);
		String data = "temp:12\nsoc:123\ncharge:1\n" + "temp:13\nsoc:124\ncharge:2\n" + "temp:14\nsoc:125\ncharge:3\n"
				+ "temp:15\nsoc:126\ncharge:4\n" + "temp:16\nsoc:127\ncharge:5\n" + "temp:17\nsoc:128\ncharge:6\n";
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
}
