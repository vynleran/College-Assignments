public class Plane {
    /*The required variables*/
    private int planeNum;
    private String destination;
    private int travelDay;

    /*Getters and setters for plane number*/
    private void setPlaneNum(int planeNum) {
        this.planeNum = planeNum;
    }
    private int getPlaneNum() {
        return this.planeNum;
    }

    /*Getters and setters for destination*/
    private void setDestination(String destination) {
        this.destination = destination;
    }
    private String getDestination() {
        return this.destination;
    }

    /*Getters and setters for the day of travel*/
    private void setTravelDay(int travelDay) {
        this.travelDay = travelDay;
    }
    private int getTravelDay() {
        if (this.travelDay <= 7 && this.travelDay >= 1) {
            return this.travelDay;
        }
        else {
            return 1;
        }

    }
}
