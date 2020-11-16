public class Library {

    // if something needs to be called from the book class 
    // we can simply to myBTNode.getData().getAuthor();
    private BTNode root;

    /* Constructor */
    public Library()
    {
        root = null;
    }
    /* Function to check if tree is empty */
    public boolean isEmpty()
    {
        return root == null;
    }
    /* Functions to insert data */
    public void insert(Book data)
    {
        root = insert(root, data);
    }
    /* Function to insert data recursively based on the title*/
     private BTNode insert(BTNode current, Book value) {
        if (current == null) {
            current = new BTNode(value);
        }
        // current is not heolding any data and thats the bug
        else if (value.getTitle().compareTo(current.getData().getTitle()) < 0) { // if alphabetically lower
            current.left = insert(current.left, value);
        } 
        else if (value.getTitle().compareTo(current.getData().getTitle()) > 0) {  // if alphabetically higher
            current.right = insert(current.right, value);
        } 
        else {
            // value already exists
            return current;
        }
        return current;
    }

    /* Function to count number of nodes */
    public int countNodes()
    {
        return countNodes(root);
    }
    /* Function to count number of nodes recursively */
    private int countNodes(BTNode r)
    {
        if (r == null)
            return 0;
        else
        {
            int l = 1;
            l += countNodes(r.getLeft());
            l += countNodes(r.getRight());
            return l;
        }
    }
    /* Function to search for an element */
    public void search(String val)
    {
        search(root, val);
    }
    /* Function to search for an element recursively */
    private void search(BTNode current, String value)
    {
        if ((value.compareTo(current.getData().getTitle()) == 0) && (current != null))
            System.out.println(current.getData().toString());

        else if ((value.compareTo(current.getData().getTitle()) < 0) && (current != null))
            search(current.getLeft(), value);

        else if ((value.compareTo(current.getData().getTitle()) > 0) && (current != null))
            search(current.getRight(), value);
        else{
            System.out.println("Nothing Found"); 
        }        
    }
    /* Function to change book status */
    public void statChange(String val)
    {
        statChange(root, val);
    }
    /* Function to change book status recursively */
    private void statChange(BTNode current, String value)
    {
        if (value.compareTo(current.getData().getTitle()) == 0)
            current.getData().setStatus();

        else if ((value.compareTo(current.getData().getTitle()) < 0))
            statChange(current.getLeft(), value);

        else if ((value.compareTo(current.getData().getTitle()) > 0))
            statChange(current.getRight(), value);
    }
    /* Function for inorder traversal */
    public void inorder()
    {
        inorder(root);
    }
    private void inorder(BTNode r)
    {
        if (r != null)
        {
            inorder(r.getLeft());
            System.out.println(r.getData().getTitle() +" ");
            inorder(r.getRight());
        }
    }
    /* Function for inorder traversal */
    public void authorTraverse(String authorName)
    {
        authorTraverse(root, authorName);
    }
    private void authorTraverse(BTNode r, String authorName)
    {
        if (r != null) // when it doesnt match, it just ends the function
        {
            authorTraverse(r.getLeft(), authorName);
            if (authorName.equals(r.getData().getAuthor())){
                System.out.println(r.getData().getTitle() + "\t\t" + r.getData().getStatus()); 
            }
            authorTraverse(r.getRight(), authorName);
        }
    }
    // /* Function for inorder traversal */
    // public String endDay()
    // {
    //     return endDay(root);
    // }
    // private String endDay(BTNode r)
    // {
    //     if (r != null)
    //     {
    //         endDay(r.getLeft());
    //         if(r.getData().getStatus()==true){
    //             return r.getData().toString();
    //         }
    //         endDay(r.getRight());
    //     }
    // }
    /* Function for preorder traversal */
    public void preorder()
    {
        preorder(root);
    }
    private void preorder(BTNode r)
    {
        if (r != null)
        {
            System.out.print(r.getData().getTitle() +" ");
            preorder(r.getLeft());             
            preorder(r.getRight());
        }
    }
    /* Function for postorder traversal */
    public void postorder()
    {
        postorder(root);
    }
    private void postorder(BTNode r)
    {
        if (r != null)
        {
            postorder(r.getLeft());             
            postorder(r.getRight());
            System.out.print(r.getData().getTitle() +" ");
        }
    }  

	// Method for searching by author
    public void searchAuthor(String userAuthor) {
        // traverse the binary tree and return all the books by that author
        // if userauthor.equals(r.getData().getAuthor)
        // then print that out
        // else go to the next node
        authorTraverse(userAuthor);    
        
	}

    // Method for searching by title
    public void searchTitle(String title){
        search(title);
    }

    // Sorting by title
    public void sortTitle(){
        inorder();
    }
}