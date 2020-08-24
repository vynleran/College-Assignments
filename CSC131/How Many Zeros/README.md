# Program: How Many Zeros?

## After having a go at this problem, we discussed a neat way to solve it (that involved a brilliant observation). We also briefly discussed a simple algorithm that would solve this problem. Here is the pseudocode:

    n ← 0

    count ← 0

    repeat

    n ← n + 1

    count ← count + the number of zeros in n

    until n is 1 million

    display count

## Of course, how can the number of zeros in n be counted? An algorithm for this could be:

    zeros ← 0

    repeat

    if n % 10 is 0

    then

    zeros ← zeros + 1

    end

    n ← n / 10

    until n is 0

## This algorithm checks to see if a remainder exists when n is divided by 10 (i.e., the value of the rightmost digit of n). If there is no remainder, then the right-most digit must be 0, and the counter is incremented. The number is then divided by ten (integer division) to remove the right-most digit, and the process continues until n is 0. Take, for example, the number 10,102:

| n      | Remainder | Quotient |
|--------|-----------|----------|
| 10,102 | 2         | 1,010    |
| 1,010  | 0         | 101      |
| 101    | 1         | 10       |
| 10     | 0         | 1        |
| 1      | 1         | 0        |
| zeros  | 2         |          |

You may be wondering why we don't just store the numbers as strings and count the number of times the character '0' occurs. This is indeed possible; however, numeric calculations are often much faster than string processing.

Your task in this programming assignment is to write a Python program that implements this (or a similar) algorithm efficiently and correctly calculates the number of zeros written from one to a target value specified by the user. What does efficiently mean? Well, think through the problem so that you do not have to unnecessarily perform operations (as they can be costly). And perhaps don't count zeros using the string method summarized above.

## In addition, your program should calculate how long it took to provide a result. To do this, you will make use of a Python library called time. Details are located below. Structure your output so that it is like mine. Here's output of a sample run (user input is shown in bold black):

What number do you want to count zeros to? **1000000**

The number of zeros written from 1 to 1000000 is 488895.

This took 1.46663212776 seconds.

## Since the target value is specified by the user, we can see results for different target values. Here are several other sample runs:

What number do you want to count zeros to? **10000**

The number of zeros written from 1 to 10000 is 2893.

This took 0.0105922222137 seconds.

What number do you want to count zeros to? **2500000**

The number of zeros written from 1 to 2500000 is 1438894.

This took 3.77886605263 seconds.

How is the time it takes to calculate the number of zeros from 1 to a specified target value determined? In general, we can get the current time immediately before and after the process of counting zeros occurs. The difference in the two times (i.e., the stop time minus the start time) is the time elapsed – and provides a fairly accurate representation of how long the algorithm took to complete. Python provides a time library that includes a function that returns the current time. Import this
functionality as follows:

    from time import time

You can get the current time as follows:

    time()

Here's sample output of a call to the function time():

    1510841671.210023

How is this a time at all? Actually, the value returned represents the number of seconds elapsed since an epoch defined in your operating system. For Unix and Unix-like operating systems (e.g., the “flavor” of Linux used on the Raspberry Pi), the epoch is 1970-01-01 00:00:00. Regardless of what the epoch time actually is, by capturing a start time and an end time, we can calculate the difference to obtain the time elapsed of some portion of code. Here's an example:

    start_time = time()

### do algorithm stuff here

    stop_time = time()

    elapsed = stop_time - start_time

## To help clarify, here are some specifics and/or constraints:

1. You must obtain user input for the target value to count zeros to (you may assume that the value
will be provided as an integer greater than or equal to 1);

2. You must calculate the number of zeros from 1 to the target value;

3. Counting the number of zeros in a single number should be done in its own function;

4. You must time how long it takes your algorithm to count the number of zeros (note that you
should absolutely not include user input and program output in the timing; that is, we are only
interested in the time it takes your zero counting algorithm to complete);

5. You must include a meaningful header, use good coding style, use meaningful variable names,
and comment your source code where appropriate;

6. Your output should be like the sample runs shown above (of course, actual input values and the
resulting output will vary depending on the provided inputs); and

7. You must submit your source code as a single .py file.
