import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws FileNotFoundException {
        // asking the user for an input file
        System.out.println("What file?");
        System.out.println("DO NOT ADD THE .TXT");

        Scanner scannerInput = new Scanner(System.in);
        String userInput = scannerInput.nextLine();
        String uiTXT = userInput + ".txt";
        
        // reading the file
        Scanner scanner = new Scanner(new File(uiTXT));

        // creating the linkedlist of words
        List<Word> myWords = new List();

        // reading through the paragraph and placing 
        // the words in nodes
        // Got this from Lance
        while(scanner.hasNext( )) {
            String Str = scanner.nextLine();
            Str = Str.toLowerCase();
            String[] arrOfStr = Str.split("[,.:;\\s]+");
            for(int i=0; i<arrOfStr.length; i++) {
                String temp = arrOfStr[i];
                if(myWords.IsEmpty() == true) {
                    myWords.InsertAfter(new Word(temp));
                }
                else {
                    boolean c = false;
                    myWords.First();
                    for(int j=0; j<myWords.GetSize(); j++) {
                        if(myWords.GetValue().getWord().equals(temp)) {
                            myWords.GetValue().incCount();
                            c = false;
                            break;
                        }
                        if(j == myWords.GetSize()-1) {
                            c = true;
                        }
                        myWords.Next();
                    }
                    if(c == true) {
                        myWords.Last();
                        myWords.InsertAfter(new Word(temp));
                    }
                }
            }
        }

        double totalUniqueNum = 0.0;
        myWords.First();
        for(int k=0;k<myWords.GetSize();k++){
            int wordC = (myWords.GetValue()).getWordCount();     // get the wordcount
            if(wordC == 1) {     // if the word has only been used once
                totalUniqueNum++;       // add one to the unique numbers
            }
            myWords.Next();
        }

        // calculating uniqueness
        double uPec = (totalUniqueNum / myWords.GetSize()) * 100;

        // writing to the file
        try {
            FileWriter myWriter = new FileWriter(uiTXT);
            myWriter.write("Your unique word percentage is " + uPec + " percent. \n");
            myWords.First();
            for(int x=0;x<myWords.GetSize();x++) {
                myWriter.write(""+myWords.GetValue().getWord()+": "+myWords.GetValue().getWordCount()+"\n");
                myWords.Next();
            }
            myWriter.close();
            System.out.println("Successfully wrote to the file.");
          } catch (IOException e) {
            System.out.println("An error occurred.");
            e.printStackTrace();
        }
    }
}