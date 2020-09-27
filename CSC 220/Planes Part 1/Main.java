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
            boolean hasMeal;
            if(data[3].equals("yes")) {
                hasMeal = true; 
            } else {
                hasMeal = false;
            }
            int rows = Integer.parseInt(data[4]);  // rows
            int seats = Integer.parseInt(data[5]);  // seats
            flights[i] = new Plane(planeId, travelDay, destination, hasMeal, rows, seats); // Array to hold the variables above
            i++;    // Going through each line
            System.out.println(flights[flightdata]); // printing each element of the array
            flightdata++;
        }

        /*Getting the file and going through each line for bookings.txt*/
        File bookingFile = new File("bookings.txt");
        Scanner scannerBooking = new Scanner(bookingFile);

        scannerBooking.nextLine();  // skipping the header line
        
        Plane[] sortedFlights = bubbleSort(flights);
        while(scannerBooking.hasNext()) {
            String sb = scannerBooking.nextLine();
            String[] sbSplitted = sb.split(",");
            int planeNumberIndex = Integer.parseInt(sbSplitted[0]); 
            int planeNumber = binarySearch(sortedFlights, planeNumberIndex);   // holds the index of the plane number in the flight array
            String passengerName = sbSplitted[1]; 
            String passengerMeal = sbSplitted[2];
            int passengerRow = Integer.parseInt(sbSplitted[3]);
            int passengerSeat = Integer.parseInt(sbSplitted[4]);
            boolean b = flights[planeNumber].addPassenger(passengerName, passengerMeal, passengerRow, passengerSeat);
        }

        boolean isMenuOpen = true;
        while(isMenuOpen) {
            /*The user menu*/
            Scanner user = new Scanner(System.in);

            /*Skipping a line and showing the menu and its options*/
            System.out.println();
            System.out.println("What Option would you like?");
            System.out.println("1 - Sort the planes out");
            System.out.println("2 - Looking for your flight?");
            System.out.println("3 - Adding a passenger?");
            System.out.println("4 - List all passengers?");
            System.out.println("5 - Food count on each plane?");
            System.out.println("6 - Find a passenger?");
            System.out.println("Exit");
            System.out.println();

            String userInput = user.nextLine(); // scanning user input

            /*Exit option for the user*/
            if (userInput.equals("Exit")) {
                isMenuOpen = false;
            }
            /*using bubble sort to sort the array out*/
            else if (userInput.equals("1")) {
                Plane[] flightsBubble = bubbleSort(flights);   /*Printing the sorted flight array*/
                System.out.println();
                System.out.println("Plane ID\t\tDestination\t\tDay of Travel\t\tEmpty Seats"); //header for the flight info
                System.out.println();
                for(int flightSortedData = 0; flightSortedData < flightsBubble.length; flightSortedData++) {  // printing the elements of the array
                    System.out.print(flightsBubble[flightSortedData]);
                    System.out.print("\t\t\t" + flights[flightSortedData].planeSeatCounter());
                    System.out.println();
                    System.out.println();
                }
            }
            // Using binary search to find the right plane
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
            // Adding a passenger to one of the planes 
            else if (userInput.equals("3")) {
                System.out.println("Enter the Plane ID:"); 
                Scanner userPlane = new Scanner(System.in);
                int userPlaneInput = Integer.parseInt(userPlane.nextLine());
                Plane[] flightsSorted = bubbleSort(flights);    /*Sorting the array before searching*/
                int userPlaneInputIndex = binarySearch(flightsSorted, userPlaneInput);
                boolean isMealAvaiable = flights[userPlaneInputIndex].getHasMeal();
                
                flights[userPlaneInputIndex].isPlaneFull();

                boolean full = flights[userPlaneInputIndex].planeStatus();
                if(full) {
                    Plane[] flightsBubble = bubbleSort(flights);
                    for(int f=0;f<flightsBubble.length;f++) {
                        String destination = flightsBubble[f].getDestination();
                        int travelDay = flightsBubble[f].getTravelDay();
                        int flightNum = flightsBubble[f].getPlaneNum();
                        boolean sameFlight = userPlaneInput == flightNum;
                        if(!sameFlight && flights[userPlaneInputIndex].getDestination().equals(destination)) {
                            System.out.println();
                            System.out.println();
                            System.out.println("Flight " + flightNum + " goes to the same destination on day " + travelDay);
                            flights[f].availableSeats();
                        }
                    }
                    System.out.println("No flights with the same destination and day of travel");      
                }
                
                if(isMealAvaiable) {
                    System.out.println("Enter meal:"); 
                    Scanner userMeal = new Scanner(System.in);
                    String userMealInput = userMeal.nextLine(); 
                    
                    System.out.println("Enter your name:"); 
                    Scanner userName = new Scanner(System.in);
                    String userNameInput = userName.nextLine();
    
                    System.out.println("Enter row:"); 
                    Scanner userRow = new Scanner(System.in);
                    int userRowInput = Integer.parseInt(userRow.nextLine());
    
                    System.out.println("Enter seat:"); 
                    Scanner userSeat = new Scanner(System.in);
                    int userSeatInput = Integer.parseInt(userSeat.nextLine());

                    flights[userPlaneInputIndex].isSeatBooked(userNameInput, userMealInput, userRowInput, userSeatInput);
                    
                    boolean isNotBooked = flights[userPlaneInputIndex].addPassenger(userNameInput, userMealInput, userRowInput, userSeatInput);
                    while(!isNotBooked) {       
                        System.out.println("Enter row:"); 
                        Scanner userRow2 = new Scanner(System.in);
                        int userRow2Input = Integer.parseInt(userRow2.nextLine());
        
                        System.out.println("Enter seat:"); 
                        Scanner userSeat2 = new Scanner(System.in);
                        int userSeat2Input = Integer.parseInt(userSeat2.nextLine());
                        if(flights[userPlaneInputIndex].addPassenger(userNameInput, userMealInput, userRow2Input, userSeat2Input)) {
                            flights[userPlaneInputIndex].addPassenger(userNameInput, userMealInput, userRow2Input, userSeat2Input);
                            flights[userPlaneInputIndex].isSeatBooked(userNameInput, userMealInput, userSeat2Input, userSeat2Input);
                            isNotBooked = true;     
                        }

                    }
                } 
                else if(!isMealAvaiable){
                    System.out.println("this plane only offers snacks");
                    String userMealInput = "snack";

                    System.out.println("Enter your name:"); 
                    Scanner userName = new Scanner(System.in);
                    String userNameInput = userName.nextLine();
    
                    System.out.println("Enter row:"); 
                    Scanner userRow = new Scanner(System.in);
                    int userRowInput = Integer.parseInt(userRow.nextLine());
    
                    System.out.println("Enter seat:"); 
                    Scanner userSeat = new Scanner(System.in);
                    int userSeatInput = Integer.parseInt(userSeat.nextLine());

                    flights[userPlaneInputIndex].isSeatBooked(userNameInput, userMealInput, userRowInput, userSeatInput);
                    
                    boolean isNotBooked = flights[userPlaneInputIndex].addPassenger(userNameInput, userMealInput, userRowInput, userSeatInput);
                    while(!isNotBooked) {       
                        System.out.println("Enter row:"); 
                        Scanner userRow2 = new Scanner(System.in);
                        int userRow2Input = Integer.parseInt(userRow2.nextLine());
        
                        System.out.println("Enter seat:"); 
                        Scanner userSeat2 = new Scanner(System.in);
                        int userSeat2Input = Integer.parseInt(userSeat2.nextLine());
                        if(flights[userPlaneInputIndex].addPassenger(userNameInput, userMealInput, userRow2Input, userSeat2Input)) {
                            flights[userPlaneInputIndex].addPassenger(userNameInput, userMealInput, userRow2Input, userSeat2Input);
                            flights[userPlaneInputIndex].isSeatBooked(userNameInput, userMealInput, userSeat2Input, userSeat2Input);
                            isNotBooked = true;     
                        }

                    }
                } 

            }
            // Listing all the passengers 
            else if (userInput.equals("4")) {
                System.out.println("Enter the Plane ID to see all passengers:"); 
                Scanner userPlaneFind = new Scanner(System.in);
                int userPlaneFindInput = Integer.parseInt(userPlaneFind.nextLine());
                Plane[] flightsSorted = bubbleSort(flights);    /*Sorting the array before searching*/
                int userPlaneFindInputIndex = binarySearch(flightsSorted, userPlaneFindInput);
                flights[userPlaneFindInputIndex].seatFinder();

            }
            // Telling the user the food count for each plane
            else if (userInput.equals("5")) {
                System.out.println("Enter the Plane ID:"); 
                Scanner userPlane = new Scanner(System.in);
                int userPlaneInput = Integer.parseInt(userPlane.nextLine());
                Plane[] flightsSorted = bubbleSort(flights);    /*Sorting the array before searching*/
                int userPlaneInputIndex = binarySearch(flightsSorted, userPlaneInput);

                flights[userPlaneInputIndex].foodCount();
            }
            // user finding a passenger
            else if (userInput.equals("6")) {
                System.out.println("Enter the Plane ID:"); 
                Scanner userPlaneFind = new Scanner(System.in);
                int userPlaneFindInput = Integer.parseInt(userPlaneFind.nextLine());
                Plane[] flightsSorted = bubbleSort(flights);    /*Sorting the array before searching*/
                int userPlaneFindInputIndex = binarySearch(flightsSorted, userPlaneFindInput);
                System.out.println("Enter the passenger name:"); 
                Scanner userPassengerFind = new Scanner(System.in);
                String userPassengerFindInput = userPassengerFind.nextLine();
                flights[userPlaneFindInputIndex].findPassenger(userPassengerFindInput);

            }
            /*for invalid user input in the menu*/
            else {
                System.out.println("Invalid input!");
            }
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
