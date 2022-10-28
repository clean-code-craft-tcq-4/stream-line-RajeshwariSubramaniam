package receiver;

import java.util.ArrayList;
import java.util.Collections;

public class Statistics{
	public void printSimpleMovingAverage(ArrayList<Float> value, int period) {

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

	public  void printMinMax(String param, ArrayList<Float> paramValues) {

		System.out.println("The min and max values respectively are min=" + Collections.min(paramValues) + " and max="
				+ Collections.max(paramValues));
	};
}