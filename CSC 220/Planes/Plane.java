public class Plane {
    /* The required variables */
    private int planeNum;
    private String destination;
    private int travelDay;
    private boolean hasMeal;
    private int rows;
    private int seats;
    private int numOnPlane; // how many people are on the plane
    private int maxSeats; // the amount of seats on a plane => rows*seats
    private Passenger[][] bookings;

    /* The default constructor */
    public Plane(int n, int t, String d, boolean m, int r, int s) {
        planeNum = n;
        destination = d;
        travelDay = t;
        hasMeal = m;
        seats = s;
        rows = r;
        bookings = new Passenger[r][s];
    }

    /* Getters and setters for plane number */
    public void setPlaneNum(int planeNum) {
        this.planeNum = planeNum;
    }

    public int getPlaneNum() {
        return this.planeNum;
    }

    /* Getters and setters for destination */
    public void setDestination(String destination) {
        this.destination = destination;
    }

    public String getDestination() {
        return this.destination;
    }

    /* Getters and setters for the day of travel */
    public void setTravelDay(int travelDay) {
        this.travelDay = travelDay;
    }

    public int getTravelDay() {
        if (this.travelDay <= 7 && this.travelDay >= 1) {
            return this.travelDay;
        } else {
            return 1;
        }

    }

    /* Getters and setter for hasMeal */
    public void setHasMeal(boolean hasMeal) {
        this.hasMeal = hasMeal;
    }

    public boolean getHasMeal() {
        return this.hasMeal;
    }

    /* Getters for numOnPlane */
    public int getNumOnPlane() {
        return this.numOnPlane;
    }

    /* Getters and setter for maxSeats */
    public void setMaxSeats(int maxSeats) {
        this.maxSeats = maxSeats;
    }

    public int getMaxSeats() {
        return this.maxSeats;
    }

    // Getter for bookings dimensional array
    public Passenger[][] getBookings() {
        return this.bookings;
    }

    /* Printing the array elements instead of their memory address */
    public String toString() {
        return (planeNum + "\t\t\t" + destination + "\t\t\t" + travelDay);
    }

    // Method for adding a passenger
    public boolean addPassenger(String passengerName, String passengerMeal, int passengerRow, int passengerSeat) {
        if ((passengerRow <= bookings.length) && (passengerSeat <= bookings[0].length)
                && isSeatEmpty(passengerRow, passengerSeat)) {
            bookings[passengerRow - 1][passengerSeat - 1] = new Passenger(passengerName, passengerMeal);
            return true;
        }
        return false;
    }

    /* Method to return how many of each food */
    public void foodCount() {
        int pastaCount = 0;
        int chickenCount = 0;
        int specialCount = 0;
        int i = 0;
        int j = 0;
        String pasta = "pasta";
        String chicken = "chicken";
        String special = "special";
        for(i = 0; i<rows;i++) {
            for(j=0;j<seats;j++){
                if(bookings[i][j] != null) {
                    String foodPreference = bookings[i][j].getPassengerMeal();
                    if(foodPreference.equals(pasta)) {
                        pastaCount++;
                    }
                    else if(foodPreference.equals(chicken)){
                        chickenCount++;
                    }
                    else if(foodPreference.equals(special)){
                        specialCount++;
                    }
                }
            }
        }
        System.out.println("Pasta\t\t\tChicken\t\t\tSpecial");       
        System.out.println(pastaCount + "\t\t\t" + chickenCount + "\t\t\t" + specialCount);
    }

    // Method to return an alphabetical list of who is on the plane and which seat
    public void seatFinder() {
        String one = "1";
        maxSeats = rows*seats;
        System.out.println("Name\t\t\trow\t\t\tseat");
        for(int i = 0; i<rows;i++)
            for(int j=0;j<seats;j++)
                if(bookings[i][j] != null){
                    System.out.println(bookings[i][j].getPassengerName() + "\t\t\t" + (i+Integer.parseInt(one)) + "\t\t\t" + (j+Integer.parseInt(one)));
                }                                                                                                                
    }

    // Shows all the available seats
    public void availableSeats() {
        String one = "1";
        System.out.println();
        System.out.println("empty seats:");
        System.out.println();
        for(int i = 0; i<rows;i++)
            for(int j=0;j<seats;j++)
                if(bookings[i][j] == null){
                    System.out.print("row " + (i+Integer.parseInt(one)) + " seat " + (j+Integer.parseInt(one)) + " |");      // gives up
                }  
    }

    /* Method to find a passenger on a plane and return which seat */
    public void findPassenger(String userName) {
        // if bookings[][] has name then return "passenger is here"
        // else return "passenger not here
        int i;
        int j;
        String one = "1";
        for(i = 0; i<rows;i++) {
            for(j=0;j<seats;j++){
                if(bookings[i][j] != null) { //if it is empty
                    String name = bookings[i][j].getPassengerName();
                    if(name.equals(userName)) {
                        System.out.println(userName + " is in row " + (i+Integer.parseInt(one)) + " and their seat is " + (j+Integer.parseInt(one))); 
                    }
                    else if(name != userName && i==rows-1 && j==seats-1) {
                        System.out.println("passenger not found");  
                    }
                } 
            }  
        }  
    }

    /* Method to tell user how many are on plane */
    public int planeSeatCounter() {
        // returning the numOnPlane for each plane
        // looping through bookings[][] and finding all the elements that are in there//loop issue
        maxSeats = rows*seats;
        int takenSeats = 0;
        int i = 0;
        int j = 0;
        for(i = 0; i<rows;i++)
            for(j=0;j<seats;j++)
                if(bookings[i][j] != null) {
                    takenSeats++;
                }
        int emptySeats = maxSeats - takenSeats;
        return(emptySeats);       
    }

    /* Method to tell user if the plane is full */
    public void isPlaneFull() {
        // if the numOnPlane is equal to maxSeats then the
        // plane is full
        int emptySeats = planeSeatCounter();
        if(emptySeats != 0) {
            System.out.println("This plane is not full");
        }
        else{
            System.out.println("This plane is full");
        }
    }

    // Checks to see if the plane is full or not
    public boolean planeStatus() {
        // int emptySeats = planeSeatCounter();
        // if(emptySeats == 0){
        //     return true;
        // }
        // else {
        //     return false;
        // }
        return true;
    }

    /*Method to tell user if a seat's already been booked*/
    public void isSeatBooked(String userName, String userMeal, int userRow, int userSeat){
        if(bookings[userRow-1][userSeat-1] != null) {   //not empty=booked
            System.out.println("seat is booked. Please pick another seat");
        } else {
            System.out.println("Here's your ticket!");
        }

    }

    /*Method to tell user which seats are available*/
    public boolean isSeatEmpty(int row, int seat){              
        if (bookings[row-1][seat-1] != null) {
            return false;
        } 
        return true;
    }
}
