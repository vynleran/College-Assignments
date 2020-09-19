public class Plane {
    /*The required variables*/
    private int planeNum;
    private String destination;
    private int travelDay;

    /*The constructor*/
    public Plane(int n, int t, String d) {
        planeNum = n;
        destination = d;
        travelDay = t;
    }

    /*Getters and setters for plane number*/
    public void setPlaneNum(int planeNum) {
        this.planeNum = planeNum;
    }
    public int getPlaneNum() {
        return this.planeNum;
    }

    /*Getters and setters for destination*/
    public void setDestination(String destination) {
        this.destination = destination;
    }
    public String getDestination() {
        return this.destination;
    }

    /*Getters and setters for the day of travel*/
    public void setTravelDay(int travelDay) {
        this.travelDay = travelDay;
    }
    public int getTravelDay() {
        if (this.travelDay <= 7 && this.travelDay >= 1) {
            return this.travelDay;
        }
        else {
            return 1;
        }

    }

    /*Printing the array elements instead of their memory address*/
    public String toString() {
        return(planeNum + "\t\t\t" + destination + "\t\t\t" + travelDay);
    }

}
