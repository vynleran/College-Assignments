// Parsa Jahanlou
// Teacher's Helper
// October 23rd, 2020

// importing the necesaary libraries
import java.util.*;

public class Main {
    public static void main(String[] args) {
        //asking the user for their formula
        System.out.println("What is the formula?");
        System.out.println("Do not space out the variables and operators");
        // scanning the value they have put in
        Scanner scannerInput = new Scanner(System.in);
        String userInput = scannerInput.nextLine();

        // putting the operators and operands in the same array
        String[] split = userInput.split("");

        // stack and queue objects
        Stack<String> stack = new Stack();
        Queue<String> queue = new Queue();

        // Going throught the formula and doing the right operations
        for(int j=0;j<split.length;j++){
            if(split[j].equals("+") || split[j].equals("-") || split[j].equals("/") || split[j].equals("*") || split[j].equals("(") || split[j].equals(")"))    // if an operator
            {
                if(stack.Peek() == null){   // if the stack is empty
                    stack.Push(split[j]);   // pushing the operator
                }
                else if(split[j].equals("(")){  // if opening paranthesis
                    stack.Push(split[j]);   // push the paranthesis
                }
                else if(split[j].equals(")")){  // if closing paranthesis
                    while(!(stack.Peek().equals("(")) && !(stack.IsEmpty())){ // while you have no reached opening paranthesis
                        queue.Enqueue(stack.Pop()); // enqueue everything that being popped
                    }
                    stack.Pop();    // pop the opening paranthesis now
                }
                else if(pemdas(stack.Peek()) > pemdas(split[j])) {
                    while(pemdas(split[j]) < pemdas(stack.Peek()) && stack.Peek() != null){ // while the operator in the stack is higher in pemdas than the one in the formula
                        queue.Enqueue(stack.Pop()); // enqueue the ones that are being popped
                        break;
                    }
                    stack.Push(split[j]);   // push the operator in the formula
                }
                else if(pemdas(stack.Peek()) < pemdas(split[j])){
                    stack.Push(split[j]);   // push the operator
                }
                else if(pemdas(stack.Peek()) == pemdas(split[j])){  // same operator
                    queue.Enqueue(stack.Pop());
                    stack.Push(split[j]);
                }
            }
            else {  // if an operand
                queue.Enqueue(split[j]);    // adding the operand to th queue
            }
        }

        // popping the remaning operator
        while(stack.GetSize()>0){
            queue.Enqueue(stack.Pop());
        }

        // printing the postfix expression
        queue.First();
        int queueSize = queue.GetSize();
        System.out.print("Postfix Expression: ");
        while(!(queue.IsEmpty()) && queueSize>0){
            System.out.print(queue.GetValue());
            queue.Next();
            queueSize--;
        }
        System.out.println();
        System.out.println();

        // stack for dequeuing
        Stack<Integer> postStack = new Stack();

        // calculating the postfix expression
        queue.First();
        for(int n=0; n<queue.GetSize();){
            String data = queue.GetValue();
            if(data.equals("+")){
                int a = postStack.Pop();
                int b = postStack.Pop();
                postStack.Push(a+b);
                queue.Dequeue();
            }
            else if(data.equals("-")){
                int a = postStack.Pop();
                int b = postStack.Pop();
                postStack.Push(a-b);
                queue.Dequeue();
            }
            else if(data.equals("*")){
                int a = postStack.Pop();
                int b = postStack.Pop();
                postStack.Push(a*b);
                queue.Dequeue();
            }
            else if(data.equals("/")){
                int a = postStack.Pop();
                int b = postStack.Pop();
                postStack.Push(a/b);
                queue.Dequeue();
            }
            else{
                System.out.println("What is the value of " + queue.Dequeue() + " ?");
                Scanner scannerVar = new Scanner(System.in);
                String userVar = scannerVar.nextLine();
                postStack.Push(Integer.parseInt(userVar));
            }
        }
        System.out.println();
        System.out.println("Results: " + postStack.Pop());
    }

    // pemdas function for checking the right order of operation
    public static int pemdas(String value) {
        int order = 0;
        switch(value){
            case "-":
                order = 1;
                break;
            case "+":
                order = 2;
                break;
            case "/":
                order = 3;
                break;
            case "*":
                order = 4;
                break;
            default:
                order = 0;
                break;
        }
        return order;
    }
}