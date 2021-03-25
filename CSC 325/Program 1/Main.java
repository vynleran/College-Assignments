import java.io.*;
import java.util.*;
import java.time.*;

public class Main {
    public static void main(String [] args) throws IOException{
        
        //LLs
        LinkedList<Character> text = new LinkedList();
        LinkedList<Character> pattern = new LinkedList();
        
        Scanner user = new Scanner(System.in);

        /*Skipping a line and showing the menu and its options*/
        System.out.println("File Name: ");
        String userInput = user.nextLine(); // scanning user input
        File file = new File(userInput);
        String output = "";

        boolean inDir = false;
        while(!inDir){
            if(file.isFile()){
                inDir = true;
            } else{
                System.out.println();
                System.out.println("File Not Found. Enter Another File: ");
                user = new Scanner(System.in);
                output += user.nextLine(); // scanning user input
                file = new File(output);
            }
        }

        Scanner userFile = new Scanner(file);
        
        //user input for pattern
        Scanner userPat = new Scanner(System.in);

        //Pattern to locate in the file
        System.out.println();
        System.out.println("pettern: ");
        String userPattern = userPat.nextLine();
        System.out.println();

        //pattern to LL
        char[] list = userPattern.toCharArray();
        for(int i = 0;i<list.length;i++){
            pattern.InsertAfter(list[i]);
        }

        //string to LL
        String input = "";
        while(userFile.hasNextLine()){
            input = userFile.nextLine();
        }

        list = input.toCharArray();

        //string -> LL
        for(int i = 0;i<list.length;i++){
            text.InsertAfter(list[i]);
        }

        HashMap<Long, String> timeTable = new HashMap<Long, String>();

        long startTimeKMP = System.nanoTime();
        KMP(text, pattern);
        long endTimeKMP = System.nanoTime();
        long kmpRes = endTimeKMP - startTimeKMP;
        System.out.println();
        timeTable.put(kmpRes, "KMP");

        long startTimeBM = System.nanoTime();
        BoyerMoore(text, pattern);
        long endTimeBM = System.nanoTime();
        long bmRes = endTimeBM - startTimeBM;
        System.out.println();
        timeTable.put(bmRes, "Boyer Moore");

        long startTimeB = System.nanoTime();
        brute(text, pattern);
        long endTimeB = System.nanoTime();
        long bRes = endTimeB - startTimeB;
        timeTable.put(bRes, "Brute Force");
        System.out.println();

        long min = Collections.min(timeTable.keySet());
        
        System.out.println("Algorithm Time:");
        System.out.println("----------------------------");
        System.out.println("Brute: " + bRes + " nano seconds");
        System.out.println("KMP: " + kmpRes + " nano seconds");
        System.out.println("Boyer Moore: " + bmRes + " nano seconds");
        System.out.println("The best pattern matching algorithm for this file is " + timeTable.get(min));
    }

    //Code From Geeks4Geeks <https://www.geeksforgeeks.org/java-program-for-kmp-algorithm-for-pattern-searching-2/>
    public static void KMP(LinkedList text, LinkedList pattern){
        String output = "";
        int M = pattern.GetSize(); 
        int N = text.GetSize(); 
    
        // create lps[] that will hold the longest 
        // prefix suffix values for pattern 
        int lps[] = new int[M]; 
        int j = 0; // index for pat[] 
        // John Helped with this part
        int prev = 0; 
        int i = 1; 
        lps[0] = 0;
    
        // the loop calculates lps[i] for i = 1 to M-1 
        while (i < M) { 
            if (pattern.ValueAt(prev) == pattern.ValueAt(i)) { 
                prev++; 
                lps[i] = prev; 
                i++; 
            } 
            else{ 
                if (prev != 0) { 
                    prev = lps[prev - 1]; 
                } 
                else{ 
                    lps[i] = prev; 
                    i++; 
                } 
            } 
        }
        
        i = 0;
        while (i < N) { 
            if (pattern.ValueAt(j) == text.ValueAt(i)) { 
                j++; 
                i++; 
            } 
            if (j == M) {
                output += (i - j);
                output += ", ";
                //System.out.println("KMP Patterns: " + (i - j));
                j = lps[j - 1]; 
            } 
    
            // mismatch after j matches 
            else if (i < N && pattern.ValueAt(j) != text.ValueAt(i)) { 
                // Do not match lps[0..lps[j-1]] characters, 
                // they will match anyway 
                if (j != 0) 
                    j = lps[j - 1]; 
                else
                    i = i + 1; 
            } 
        }
        if(output.equals("")){
            System.out.println("Nothing found using KMP!");
        } else{
            System.out.println("KMP: " + output);
        }
    }
    //I got this code from: https://www.codespeedy.com/boyer-moore-algorithm-in-java/ 
    public static void BoyerMoore(LinkedList text, LinkedList pattern){
        int m = pattern.GetSize(); 
        int n = text.GetSize();
        String output = "";
  
        int badchar[] = new int[256]; 
        badCharHeuristic(pattern, m, badchar); 
  
        int s = 0;  
        while(s <= (n - m)){ 
            int j = m-1; 
  
            while(j >= 0 && pattern.ValueAt(j) == text.ValueAt(s+j)) 
                j--; 
  
            if (j < 0){ 
                output += s;
                output += ", ";
                // John helped here too since I was having some problems with data types
                s += (s+m < n)? m-badchar[(Character) text.ValueAt(s+m)] : 1; 
            } 
            else
                s += max(1, j - badchar[(Character) text.ValueAt(s+j)]); 
        }
        if(output.equals("")){
            System.out.println("Nothing found using Boyer Moore!");
        } else{
            System.out.println("Boyer Moore: " + output);
        }
    }
    public static void badCharHeuristic(LinkedList str, int size, int badchar[]) { 
        int i; 
        for (i = 0; i < 256; i++) 
            badchar[i] = -1; 
        for (i = 0; i < size; i++) 
            badchar[(Character) str.ValueAt(i)] = i; 
    }
    
    static int max (int a, int b) { return (a > b)? a: b; }

    // got this code from https://gist.github.com/Madhivarman/a4975e3e8e547681a5d5a0da46f77f80
    public static void brute(LinkedList text,LinkedList pattern){
        int textSize = text.GetSize();//length of the text
        int patternSize = pattern.GetSize();//length of the pattern;
        String output = "";

        //loop condition
        for(int i=0;i<textSize-patternSize;i++) {
            //initialization of j
            int j = 0;
            while ((j < patternSize) && (text.ValueAt(i + j) == pattern.ValueAt(j))) {
                j++;
            }
            if (j == patternSize) {
                output += i;
                output += ", ";
            }
            text.Next();
        }
        if(output.equals("")){
            System.out.println("Nothing found using brute force!");
        } else{
            System.out.println("Brute Force: " + output);
        }
    }

}
