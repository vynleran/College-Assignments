/*Importing the necessary libraries*/
import java.io.*;
import java.util.*;

public class Main {
    public static void main (String[] Args) throws IOException {

        /*Getting the file and going through each line*/
        File planeFile = new File("plane.txt");
        Scanner scanner = new Scanner(planeFile);

        /*Flight array to hold the required variables*/
        Plane[] flights = new Plane[28];

        int i=0;
        scanner.nextLine(); // skip header line

        String s; // holds the string you read from the file
        String[] data;  // Holds the string after splitting

        while(scanner.hasNext()) {
            s = scanner.nextLine();
            data = s.split(", "); // splitting to seperate the data
            int planeId = Integer.parseInt(data[0]); // planeNum
            String destination = data[1]; // destination
            int travelDay = Integer.parseInt(data[2]); // travelDay
            flights[i] = new Plane(planeId, travelDay, destination); // Array to hold the variables above
            i++;    // Going through each line
        }
        System.out.println(Arrays.toString(flights));

        /*The user menu*/
        Scanner user = new Scanner(System.in);

        /*Skipping a line and showing the menu and its options*/
        System.out.println();
        System.out.println("What Option would you like?");
        System.out.println("1 - Sort the planes out");
        System.out.println("2 - Find your plane");
        System.out.println("Exit");

        String userInput = user.nextLine(); // scanning user input

        if (userInput.equals("Exit")) {
            return;

        }

    }
}
