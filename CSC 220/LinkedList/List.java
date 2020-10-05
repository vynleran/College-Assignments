/* ***************************************************
 * Parsa Jahanlou
 * October 9th, 2020
 *
 * List Class - handles any form of data
 *************************************************** */

public class List<Type>
{
    // We don't actually have to set a max size with linked lists
    // But it is a good idea.
    // Just picture an infinite loop adding to the list! :O
    // Yes, you may change this when you do your word count program.
    public static final int MAX_SIZE = 50;

    private Node<Type> head;
    private Node<Type> tail;
    private Node<Type> curr;
    private int num_items;

    // constructor
    // remember that an empty list has a "size" of -1 and its "position" is at -1
    public List()
    {
        head = new Node();
        tail = new Node();
        curr = new Node();
        num_items = 0;
    }

    // copy constructor
    // clones the list l and sets the last element as the current
    // (notice we're not just copying the whole list at once?)
    public List(List<Type> l)
    {
        Node<Type> n = l.head;      // n is the head of the 1 object

        head = new Node();
        tail = new Node();
        curr = new Node();
        this.num_items = 0;

        while (n != null)
        {
            this.InsertAfter(n.getData());
            n = n.getLink();
        }
    }

    // setLink() = designates a link to the node you give it
    // getLink() = you get the link of the node you are giving it 
    // setData() = sets the data based on the parameter you give it
    // getData() = gets the data stored in that node

    // navigates to the beginning of the list
    public void First()
    {
        this.curr = this.head;
    }

    // navigates to the end of the list
    // the end of the list is at the last valid item in the list
    public void Last()
    {
        this.curr = this.tail;
    }

    // navigates to the specified element (0-index)
    // this should not be possible for an empty list
    // this should not be possible for invalid positions
    public void SetPos(int pos)
    {
        if(!IsEmpty()) {
            this.curr = this.head;
            while(pos>0 && pos<num_items) {     // might be one off = pos>= 0
                curr.setLink(curr.getLink().getLink());
                pos--;
            }
        }
    }

    // navigates to the previous element
    // this should not be possible for an empty list
    // there should be no wrap-around
    public void Prev()
    {
        if(!IsEmpty()) {
            int pos = GetPos();
            SetPos(pos-1);                      // would this actually work
        }
    }
    
    // navigates to the next element
    // this should not be possible for an empty list
    // there should be no wrap-around
    public void Next()
    {
        if(!IsEmpty()) {
            curr.setLink(curr.getLink().getLink());
        }
    }

    // returns the location of the current element (or -1)
    public int GetPos()
    {
        Node<Type> n = this.curr;
        int i = 0;
        for(;i<num_items;i++) {
           n.setLink(n.getLink().getLink());
        } 
        int tailIndex = num_items-1;
        return(tailIndex-i);     // how to get i out of the for loop
    }

    // returns the value of the current element (or -1)
    public Type GetValue()
    {
        return(curr.getLink().getData());
    }

    // returns the size of the list
    // size does not imply capacity
    public int GetSize()
    {
        int nodeCounter =0;
        while(!IsEmpty() && head.getLink() != null && nodeCounter<num_items) {
            head.setLink(head.getLink().getLink());
            nodeCounter++;
        }
        return(nodeCounter);
    }

    // inserts an item before the current element
    // the new element becomes the current
    // this should not be possible for a full list
    public void InsertBefore(Type data)
    {
        if(!IsFull()) {
            // can just call prev() and then do everything i did in insertafter()
            Prev();
            InsertAfter(data);
            num_items++;
        }
    }

    // inserts an item after the current element
    // the new element becomes the current
    // this should not be possible for a full list
    public void InsertAfter(Type data)
    {
        Node<Type> newNode = new Node();
        newNode.setData(data);
        if(IsEmpty()) {
            head.setLink(newNode);
            tail.setLink(newNode);
            curr.setLink(newNode);
            num_items++;
        }    
        else if(!IsFull()) {
            newNode.setLink(curr.getLink().getLink());      // setting up a link from the newNode to the node after the previous current node
            curr.getLink().setLink(newNode);        // connecting the current node to the new Node
            curr.setLink(curr.getLink().getLink()); // moving current pointer to the new node
            num_items++;
        }
    }

    // removes the current element 
    // this should not be possible for an empty list
    public void Remove()
    {
        if(!IsEmpty()) {
            // go to previous and then follow the removing protocol
            // keep in mind for the tail and head
            Prev();
            curr.getLink().setLink(curr.getLink().getLink().getLink());
        }
    
    }

    // replaces the value of the current element with the specified value
    // this should not be possible for an empty list
    public void Replace(Type data)
    {
        if(!IsEmpty()) {
            curr.setData(data);
        }
    }

    // returns if the list is empty
    public boolean IsEmpty()
    {
        if(num_items == 0) {
            return true;
        }
        return false;
    }

    // returns if the list is full
    public boolean IsFull()
    {
        if(num_items == MAX_SIZE) {
            return true;
        }
        return false;
    }

    // // returns if two lists are equal (by value)
    // public boolean Equals(List<Type> l)
    // {
    
    // }

    // // returns the concatenation of two lists
    // // l should not be modified
    // // l should be concatenated to the end of *this
    // // the returned list should not exceed MAX_SIZE elements
    // // the last element of the new list is the current
    // public List<Type> Add(List<Type> l)
    // {
    
    // }

    // returns a string representation of the entire list (e.g., 1 2 3 4 5)
    // the string "NULL" should be returned for an empty list
    public String toString()
    {
        if(!IsEmpty()) {
            for(int i=0;i<=num_items;i++) {
                this.curr = this.head;      // moving curr to head
                Type data = curr.getLink().getData();       // getting the data from each node
                curr.setLink(curr.getLink().getLink());     // curr moving to the next node
                System.out.print(data + " ");
            }      
        }
        return("NULL");
    }
}