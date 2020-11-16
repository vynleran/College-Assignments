//Stack class to extend List class
public class Stack<Type> extends List<Type> {
    // default constructor that inherits from List
    public Stack(){
        super();
    }
    // push method to add to the top of the stack
    public void Push(Type n){
            super.First();
            super.InsertBefore(n);
    }
    // pop method to remove from the top of the stack
    public Type Pop(){
        if(!(super.IsEmpty())){ // checking ot see if the stack is empty or not 
            super.First();  // moving the pointer to the head node
            Type value = super.GetValue();  // getting the value of the top node before removing it
            super.Remove(); // removing the head node
            return value;   // returning the value of the removed top node
        }
        else{
            return null;    // if it is empty then return null
        }

    }
    // looking at the data the top stack is holding
    public Type Peek(){
        if(!(super.IsEmpty())){ // checking to see if the stack is empty or not
            super.First();  // moving the pointer to the top stack
            Type value = super.GetValue();   // getting the value of the top node
            return value;   // returning that value
        }
        else {
            return null;    // if the stack is empty then return null
        }
    }

}
