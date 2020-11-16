import java.io.*;
import java.util.*;
import javax.crypto.Mac;

public class Main {
    public static void main (String[] Args) throws IOException {

        /*Getting the file and going through each line*/
        File libraryFile = new File("log.txt");
        Scanner scanner = new Scanner(libraryFile);

        /*scifili(BT) to hold the required variables*/
        Library scifili = new Library();
        MinHeap fire = new MinHeap(108);
        StringHeap authorHeap = new StringHeap(108);

        Stack<String> pile = new Stack();

        String string; // holds the string you read from the file
        String[] split;  // Holds the string after splitting

        // going through the file and storing the books
        while(scanner.hasNext()) {
            string = scanner.nextLine();
            split = string.split(", "); // splitting to seperate the data
            String title = split[0];
            String author = split[1];
            Boolean status;
            if(Integer.parseInt(split[2])==1){
                status = true;
            }
            else{
                status = false;
            }
            int priority = Integer.parseInt(split[3]);
            scifili.insert(new Book(title, author, status, priority)); // ==> needs to be a Book object and not object
            fire.insert(new Book(title, author, status, priority)); // ==> this is for the fire heap
            authorHeap.insert(new Book(title, author, status, priority));
        }

        /*The user menu*/
        boolean isMenuOpen = true;
        while(isMenuOpen) {
            Scanner user = new Scanner(System.in);

            /*Skipping a line and showing the menu and its options*/
            System.out.println();
            System.out.println("What Option would you like?");
            System.out.println("1 - Sort based on author name");
            System.out.println("2 - Sort based on title");
            System.out.println("3 - Oh there is a fire? Lets save the books");
            System.out.println("4 - Searching for an author's books?");
            System.out.println("5 - Searching for a specific book and need details?");
            System.out.println("6 - Are you trying to check in/out?");
            System.out.println("7 - Are you leaving and need a list of the books?");
            System.out.println("Exit");
            System.out.println();

            String userInput = user.nextLine(); // scanning user input

            // if the user wants to sort by author name
            if (userInput.equals("1")) {
                sortAuthor(authorHeap);
            }

            // if the user wants to sort by the title
            else if (userInput.equals("2")) {
                System.out.println();
                System.out.println("Titles:");
                scifili.sortTitle();
            }

            // if there is a fire
            else if (userInput.equals("3")) {
                fire(fire);
            }

            // if the user is searching based on author name
            else if (userInput.equals("4")) {
                System.out.println("Who is the author you are looking for?"); 
                Scanner userAuthor = new Scanner(System.in);
                String userAuthorInput = userAuthor.nextLine();
                System.out.println();
                System.out.println("Books by " + userAuthorInput + ":");
                System.out.println("Title\t\tStatus");
                System.out.println("----------------------------");
                scifili.searchAuthor(userAuthorInput);
            }

            // if the user is searching based on title
            else if (userInput.equals("5")) {
                System.out.println("What book are you looking for?"); 
                Scanner userTitle = new Scanner(System.in);
                scifili.searchTitle(userTitle.nextLine());
            }

            // if the user is trying to check in
            else if (userInput.equals("6")) {
                System.out.println("What book are you checking in/out?");
                System.out.println("type \"no\" to stop checking in/out"); 
                while(true){
                    Scanner userBook = new Scanner(System.in);
                    String s = userBook.nextLine();
                    if(s.equals("no")){
                        System.out.println();
                        System.out.println("All Done!");
                        break;
                    } else {
                        pile.Push(s);
                        checkBook(scifili, pile);
                    }
                }
            }

            // if the user is leaving the library
            else if (userInput.equals("7")) {
                // creating the new file
                try {
                    File myObj = new File("LibraryStatus.txt");
                    if (myObj.createNewFile()) {
                        System.out.println("File created: " + myObj.getName());
                    } else {
                        System.out.println("File already exists.");
                    }
                } catch (IOException e) {
                    System.out.println("An error occurred.");
                    e.printStackTrace();
                }

                // writing to the new file
                try {
                    FileWriter myWriter = new FileWriter("LibraryStatus.txt");
                    myWriter.write("Title\t\tAuthor\t\tStatus\n");
                    //myWriter.write(scifili.endDay());
                    myWriter.close();
                    System.out.println("Successfully wrote to the file.");
                } catch (IOException e) {
                    System.out.println("An error occurred.");
                    e.printStackTrace();
                }
                isMenuOpen = false; // closing the menu
            }

            // if the user wants to exit
            else if (userInput.equals("Exit")) {
                isMenuOpen = false;
            }

            // if the user input is invalid
            else {
                System.out.println("Invalid Input!");
            }
        }
    }

    // Method for checking in and checking out
    public static void checkBook(Library library, Stack pile) {
        // push into the stack till done and no books
        // pop those books out and change their status
        // pop from the tree and find it in the tree and then change the status
        while (!(pile.IsEmpty())) {
            String book = (String) pile.Pop();
            library.statChange(book);
        }
    }

    // Method for sorting based on author name
    public static void sortAuthor(StringHeap authorHeap){
        // copy the binary tree
        // and turn it into a heap
        // then start removing the author names
        System.out.println("ORGANIZED (Z-A) BASED ON AUTHOR\n------------------");
        for(int i = 1; i <= 108; i++){
            System.out.println(authorHeap.extractMax());
        }
        
    }

    // Heap Method for the fire
    public static void fire(MinHeap fire){
        // copy the binary tree ==> (Did this alongside the Library creation)
        // you put everything into a max heap based on priority
        // you just start removing nodes
        for(int i = 1; i <= 108; i++){
            System.out.println(fire.remove() + "--REMOVED");
        }
    }

    public static void endDay()
    {

    }
}
