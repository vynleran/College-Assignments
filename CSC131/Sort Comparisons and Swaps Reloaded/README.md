# Program: Sort Comparisons and Swaps...Reloaded

## Your task in this programming assignment is to update your previous Python program that implemented the following sorting algorithms:

- Bubble sort

- Optimized bubble sort

- Selection sort

- Insertion sort

Recall that you had each sorting algorithm not only sort a list, but additionally provide the number of comparisons and swaps made during the sorting process! In this program, you will additionally provide the results of each sorting algorithm's comparisons and swaps to a module that will graph them, side-by-side. This module (called plot) will be provided to you.

To make this all work, the mechanism required to properly provide the module with the sorting algorithm comparison and swap results is carefully defined. You will often find that such requirements are provided to you when writing your own programs (even in industry). Someone else has defined some useful functions that you care to use, and you must provide data and obtain any returned results as the designers have defined it.

### In this case, save the provided plot module in the same location as your Python source code for this program. Import the plot module as follows:
    
    from plot import plot

### In this program, you must call a function called plot and provide it four lists as arguments. Each list should contain two values: (1) the number of comparison for a sorting algorithm; and (2) the number of swaps for a sorting algorithm – in that order. Suppose, for example, that the bubble sort required 312 comparisons and 191 swaps. The following list would therefore be correct:

    bubble = [312, 191]

### Such a list for each sorting algorithm must be generated and passed to the plot function in the plot module as follows:

    plot(bubble, optimized, selection, insertion)

### Of course, this assumes that the four lists have been stored in the variables bubble, optimized, selection, and insertion. If the plot function in the plot module has not been uniquely imported (i.e., if the entire plot library has been imported instead as import plot), then the following function call is appropriate:

    plot.plot(bubble, optimized, selection, insertion)

Pay attention to the order of the lists. The plot module expects them in this order!

Good coding style would have each sorting algorithm defined in its own function, taking an unsorted list as input, sorting the list (accurately recording the number of comparisons and swaps made), and returning the number of comparisons and swaps made as output. The output can be returned as two individual values (as is most likely the case in your previous program) or as a list (which may be better in this case).

## To help clarify, here are some specifics and/or constraints:

1. Each sorting algorithm must be implemented in its own function that only takes the list as an
input parameter and returns both the number of comparisons and swaps made as outputs;

2. Each sorting algorithm must be provided the exact same list so that a proper comparison between
the different sorting algorithms can be made;

3. The results of the sorting algorithms (i.e., comparisons and swaps) must be properly passed to
the plot function in the plot module to be graphed;

4. You must include a meaningful header, use good coding style, use meaningful variable names,
and comment your source code where appropriate;

5. Your output should be like the sample runs shown above; and

6. You must submit your source code as a single .py file.
