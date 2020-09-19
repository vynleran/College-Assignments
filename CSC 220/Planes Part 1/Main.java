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
        int flightdata = 0;
        scanner.nextLine(); // skip header line
        System.out.println("Plane ID\t\tDestination\t\tDay of Travel"); // header for the flight infos

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
            System.out.println(flights[flightdata]); // printing each element of the array
            flightdata++;
        }

        /*The user menu*/
        Scanner user = new Scanner(System.in);

        /*Skipping a line and showing the menu and its options*/
        System.out.println();
        System.out.println("What Option would you like?");
        System.out.println("1 - Sort the planes out");
        System.out.println("2 - Looking for your flight?");
        System.out.println("Exit");
        System.out.println();

        String userInput = user.nextLine(); // scanning user input

        /*Exit option for the user*/
        if (userInput.equals("Exit")) {

        }
        /*using bubble sort to sort the array out*/
        else if (userInput.equals("1")) {
            Plane[] flightsBubble = bubbleSort(flights);   /*Printing the sorted flight array*/
            System.out.println();
            System.out.println("Plane ID\t\tDestination\t\tDay of Travel"); //header for the flight info
            for(int flightSortedData = 0; flightSortedData < flightsBubble.length; flightSortedData++) {  // printing the elements of the array
                System.out.println(flightsBubble[flightSortedData]);
            }
        }
        else if (userInput.equals("2")) {
            System.out.println("Enter your Plane ID:"); /*Asking the Plane ID to show the index of it*/
            Scanner userPlaneId = new Scanner(System.in);
            String userPlaneIdInput = userPlaneId.nextLine();
            Plane[] flightsSorted = bubbleSort(flights);    /*Sorting the array before searching*/
            int flightInfo = binarySearch(flightsSorted, Integer.parseInt(userPlaneIdInput)); // using the index from the binary search to print the correct element
            System.out.println();
            System.out.println("Plane ID\t\tDestination\t\tDay of Travel"); // header for the flight info
            System.out.println(flights[flightInfo]);
        }
        /*for invalid user input in the menu*/
        else {
            System.out.println("Invalid input!");
        }
    }
    /*bubble sort*/
    /*Found this code in your Array text file*/
    public static Plane[] bubbleSort(Plane[] flights){
        int n = flights.length;
        for (int j = 0; j < n-1; j++)
            for (int k = 0; k < n-j-1; k++)
                if (flights[k].getPlaneNum() > flights[k+1].getPlaneNum()){
                    Plane temp = flights[k];
                    flights[k] = flights[k+1];
                    flights[k+1] = temp;
                }
        return(flights);
    }
    /*Binary search*/
    /*Found this code at https://stackabuse.com/binary-search-in-java/*/
    public static int binarySearch(Plane[] arrayToSearch, int element) {
        int lowIndex = 0;
        int highIndex = arrayToSearch.length - 1;

        // Holds the position in array for given element
        // Initial negative integer set to be returned if no match was found on array
        int elementPos = -1;

        // If lowIndex less than highIndex, there's still elements in the array
        while (lowIndex <= highIndex) {
            int midIndex = (lowIndex + highIndex) / 2;
            if (element == arrayToSearch[midIndex].getPlaneNum()) {
                elementPos = midIndex;
                return(elementPos);
            } else if (element < arrayToSearch[midIndex].getPlaneNum()) {
                highIndex = midIndex-1;
            } else if (element > arrayToSearch[midIndex].getPlaneNum()) {
                lowIndex = midIndex+1;
            }
        }
        return(elementPos);
    }
}
