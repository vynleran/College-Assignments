//Queue class to extend List class
public class Queue<Type> extends List<Type> {
    // defualy constructor that inherits from the List class
    public Queue(){
        super();
    }
    // enqueue method for adding to the front of the queue
    public void Enqueue(Type n){
        if(!(super.IsEmpty())){ // checking to see if the queue is empty or not
            super.Last();   // moving the pointer to the tail
            super.InsertAfter(n); // do you insertafter or insertbefore 
        }
        else {
            super.Last();
            super.InsertAfter(n);
        }
    }
    // dequeue method for removing from the front of the queue
    public Type Dequeue(){
        if(!(super.IsEmpty())){ // checking to see if the queue is empty or not
            super.First();  // moving the pointer to the head of the queue
            Type t = super.GetValue();  // getting the value of the head node of the queue
            super.Remove(); // removing the head node 
            return t;   // returning the value of the removed node
        }
        else {
            return null;    // if it is empty then return null
        }
    }

}
