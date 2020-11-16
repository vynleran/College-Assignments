/* Class BTNode */
class BTNode
{    
    BTNode left, right;
    Book data;

    /* Constructor */
    public BTNode()
    {
        left = null;
        right = null;
        data = null;
    }
    /* Constructor */
    public BTNode(Book n)
    {
        left = null;
        right = null;
        data = n;
    }
    /* Function to set left node */
    public void setLeft(BTNode n)
    {
        left = n;
    }
    /* Function to set right node */ 
    public void setRight(BTNode n)
    {
        right = n;
    }
    /* Function to get left node */
    public BTNode getLeft()
    {
        return left;
    }
    /* Function to get right node */
    public BTNode getRight()
    {
        return right;
    }
    /* Function to set data to node */
    public void setData(Book d)
    {
        data = d;
    }
    /* Function to get data from node */
    public Book getData()
    {
        return data;
    }     
}