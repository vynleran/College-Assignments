# Program: Search Comparison Table

## Your task in this programming assignment is to write a Python program that generates the sequential search/binary search comparison table in the lesson on Searching and Sorting. Here's the table for reference:

| Number of Items | Sequential Search | Binary Search | Performance |
|-----------------|-------------------|---------------|-------------|
| 0               | 0                 | 0             | 0           |
| 1000            | 500               | 10            | 50          |
| 2000            | 1000              | 11            | 91          |
| 3000            | 1500              | 12            | 125         |
| 4000            | 2000              | 12            | 167         |
| 5000            | 2500              | 13            | 192         |
| 6000            | 3000              | 13            | 231         |
| 7000            | 3500              | 13            | 269         |
| 8000            | 4000              | 13            | 308         |
| 9000            | 4500              | 14            | 321         |
| 10000           | 5000              | 14            | 357         |

## The first column will be specified (via user input) and the remaining columns will be calculated. Specifically, the user will specify a minimum and maximum list size (number of items in the table) and an interval (how much to increase the list size for the next row in the table). Here's output of a sample run (user input is shown in bold black):

Minimum number of list items (>=0)? **0**

Maximum number of list items (>= min (0))? **10000**

The interval between each row of the table (>= 1)? **1000**

n Seq Bin Perf

--------------------------------

0 0 0 0

1000 500 10 50

2000 1000 11 91

3000 1500 12 125

4000 2000 12 167

5000 2500 13 192

6000 3000 13 231

7000 3500 13 269

8000 4000 13 308

9000 4500 14 321

10000 5000 14 357

## Here's another sample run to further show how the user input dictates the overall structure of the table (again, user input is shown in bold black):

Minimum number of list items (>=0)? **455**

Maximum number of list items (>= min (455))? **999**

The interval between each row of the table (>= 1)? **25**

n Seq Bin Perf

--------------------------------

455 227 9 25

480 240 9 27

505 252 9 28

530 265 10 27

555 277 10 28

580 290 10 29

605 302 10 30

630 315 10 32

655 327 10 33

680 340 10 34

705 352 10 35

730 365 10 37

755 377 10 38

780 390 10 39

805 402 10 40

830 415 10 42

855 427 10 43

880 440 10 44

905 452 10 45

930 465 10 47

955 477 10 48

980 490 10 49

## Also, your program should properly deal with invalid user input; for example:

Minimum number of list items (>=0)? **-1**

*ERROR: Minimum must be >= 0!

Minimum number of list items (>=0)? **100**

Maximum number of list items (>= min (100))? **25**

*ERROR: Maximum must be >= minimum (100)!

Maximum number of list items (>= min (100))? **1000**

The interval between each row of the table (>= 1)? **0**

*ERROR: Interval must be >= 1!

The interval between each row of the table (>= 1)? **250**

n Seq Bin Perf

--------------------------------

100 50 7 7

350 175 9 19

600 300 10 30

850 425 10 43

## To help clarify, here are some specifics and/or constraints:

1. Displaying the entire table must be done in its own function;

2. Calculating the average number of comparisons of a sequential search must be done in its own
function (see the template for more details);

3. Calculating the maximum number of comparisons of a binary search must be done in its own
function (see the template for more details);

4. Obtaining user input can be done in the main part of the program (or in a separate function);

5. Range (or boundary) checking of user input must be done;

6. You must use the provided source code template; and

7. You must submit your source code as a single .py file.
