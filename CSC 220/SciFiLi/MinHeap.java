//Got this code from
//https://www.geeksforgeeks.org/min-heap-in-java/
// Java implementation of Min Heap 
public class MinHeap { 
    private Book[] Heap; 
    private int size; 
    private int maxsize; 
  
    private static final int FRONT = 1; 
    
    public MinHeap(int maxsize) 
    { 
        this.maxsize = maxsize; 
        this.size = 0; 
        Heap = new Book[this.maxsize + 1]; 
        Heap[0] = new Book(); 
    } 
  
    // Function to return the position of 
    // the parent for the node currently 
    // at pos 
    private int parent(int pos) 
    { 
        return pos / 2; 
    } 
  
    // Function to return the position of the 
    // left child for the node currently at pos 
    private int leftChild(int pos) 
    { 
        return (2 * pos); 
    } 
  
    // Function to return the position of 
    // the right child for the node currently 
    // at pos 
    private int rightChild(int pos) 
    { 
        return (2 * pos) + 1; 
    } 
  
    // Function that returns true if the passed 
    // node is a leaf node 
    private boolean isLeaf(int pos) 
    { 
        if (pos >= (size / 2) && pos <= size) { 
            return true; 
        } 
        return false; 
    } 
  
    // Function to swap two nodes of the heap 
    private void swap(int fpos, int spos) 
    { 
        Book tmp; 
        tmp = Heap[fpos]; 
        Heap[fpos] = Heap[spos]; 
        Heap[spos] = tmp; 
    } 
  
    // Function to heapify the node at pos 
    private void minHeapify(int pos) 
    { 
  
        // If the node is a non-leaf node and greater 
        // than any of its child 
        if (!isLeaf(pos)) { 
            if (Heap[pos].getPriority() > Heap[leftChild(pos)].getPriority()
                || Heap[pos].getPriority() > Heap[rightChild(pos)].getPriority()) { 
  
                // Swap with the left child and heapify 
                // the left child 
                if (Heap[leftChild(pos)].getPriority() < Heap[rightChild(pos)].getPriority()) { 
                    swap(pos, leftChild(pos)); 
                    minHeapify(leftChild(pos)); 
                } 
  
                // Swap with the right child and heapify 
                // the right child 
                else { 
                    swap(pos, rightChild(pos)); 
                    minHeapify(rightChild(pos)); 
                } 
            } 
        } 
    } 
  
    // Function to insert a node into the heap 
    public void insert(Book element) 
    { 
        if (size >= maxsize) { 
            return; 
        } 
        Heap[++size] = element; 
        int current = size; 
  
        while (Heap[current].getPriority() < Heap[parent(current)].getPriority()) { 
            swap(current, parent(current)); 
            current = parent(current); 
        } 
    } 
  
    // Function to print the contents of the heap 
    public void print() 
    { 
        for (int i = 1; i <= size / 2; i++) { 
            System.out.print(" PARENT : " + Heap[i] 
                             + " LEFT CHILD : " + Heap[2 * i] 
                             + " RIGHT CHILD :" + Heap[2 * i + 1]); 
            System.out.println(); 
        } 
    } 
  
    // Function to build the min heap using 
    // the minHeapify 
    public void minHeap() 
    { 
        for (int pos = (size / 2); pos >= 1; pos--) { 
            minHeapify(pos); 
        } 
    } 
  
    // Function to remove and return the minimum 
    // element from the heap 
    public Book remove() 
    { 
        Book popped = Heap[FRONT]; 
        Heap[FRONT] = Heap[size--]; 
        minHeapify(FRONT); 
        return popped; 
    } 
    
    public Book MinPriority()
    {
        Book b;
        int[] Priority = new int[Heap.length];
        for(int i = 0; i < Heap.length; i ++)
        {
            Priority[i] = Heap[i].getPriority();
        }
        int minI = 0;
        int min = Priority[0];
        for(int i = 0; i < Heap.length; i ++)
        {
            if(min > Priority[i+1])
            {
                min = Priority[i+1];
                minI = i;
            }
        }
        b = Heap[minI];
        return b;
        
        
    }
}
  