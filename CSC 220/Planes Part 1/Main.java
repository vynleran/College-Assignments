/*Importing the necessary libraries*/
import java.io.*;
import java.util.*;

public class Main {
    public static void main (String[] Args) throws IOException {

        /*Getting the file and going through each line*/
        File planeFile = new File("plane.txt");
        Scanner scanner = new Scanner(planeFile);

        /*Array to store the flights in*/
        String[] flights = new String[29];

        /*With the help of https://stackoverflow.com/questions/63875415/how-to-store-a-line-in-an-array*/
        int i=0;
        scanner.nextLine(); // skip header line

        while(scanner.hasNext()) {
            flights[i] = scanner.nextLine();
        }
        System.out.println(Arrays.toString(flights));
    }
}
