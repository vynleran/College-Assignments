public class Passenger {
    private String passengerName;
    private String passengerMeal;

    /*default constructor*/
    public Passenger(String name, String meal) {
        passengerName = name;
        passengerMeal = meal;
    }

    /*Getter and setter for passengerName*/
    public void setPassengerName(String name) {
        this.passengerName = name;
    }
    public String getPassengerName() {
        return this.passengerName;
    }

    /*Getter and setter for passengerMeal*/
    public void setPassengerMeal(String meal) {
        this.passengerMeal = meal;
    }
    public String getPassengerMeal() {
        return this.passengerMeal;
    }
}
