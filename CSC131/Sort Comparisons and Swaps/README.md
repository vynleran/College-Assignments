# Program: Sort Comparisons and Swaps

## Your task in this programming assignment is to write a Python program that implements the following sorting algorithms:

- Bubble sort

- Optimized bubble sort

- Selection sort

- Insertion sort

You can find pseudocode (and even Python code) for these sorting algorithms in previous lessons in the
curriculum. It probably seems a bit boring to simply write sorting functions and watch lists being
sorted. So, let's make this a bit more interesting by having each sorting algorithm not only sort a list, but
additionally provide the number of comparisons and swaps made during the sorting process! Any time
a sorting algorithm compares one value in the list to another, a comparison has been made.
Appropriately, a counter should be updated (that, of course, was properly initialized). Any time a value
is swapped with one located at another (different) index in the list, a swap has been made. Similarly, a
counter should be updated.

## Since the sorting algorithms have been detailed in previous lessons, you should only be left with figuring out how to count the number of comparisons and swaps made as each sorting algorithm runs. The difficulty in this depends on how you choose to implement the sorting algorithms. It is strongly suggested that you manually “play computer” with short lists to test out your algorithm modifications and verify that they indeed accurately count the number of comparisons and swaps. Of course, sample runs are provided. In fact, here's one:

    The list: [100, 5, 63, 29, 69, 74, 96, 80, 82, 12]

    After bubble sort: [5, 12, 29, 63, 69, 74, 80, 82, 96, 100]

    45 comparisons; 19 swaps

    The list: [100, 5, 63, 29, 69, 74, 96, 80, 82, 12]

    After optimized bubble sort: [5, 12, 29, 63, 69, 74, 80, 82, 96, 100]

    45 comparisons; 19 swaps

    The list: [100, 5, 63, 29, 69, 74, 96, 80, 82, 12]

    After selection sort: [5, 12, 29, 63, 69, 74, 80, 82, 96, 100]

    45 comparisons; 9 swaps

    The list: [100, 5, 63, 29, 69, 74, 96, 80, 82, 12]

    After insertion sort: [5, 12, 29, 63, 69, 74, 80, 82, 96, 100]

    37 comparisons; 19 swaps

## To simplify testing, a template will be provided to you that includes a function that will generate the same list each time it is called. The included function has several other sample lists (commented out) that you can use to test. Here's a sample run with another list:

    The list: [82, 65, 93, 0, 60, 31, 99, 90, 31, 70]

    After bubble sort: [0, 31, 31, 60, 65, 70, 82, 90, 93, 99]

    45 comparisons; 23 swaps

    The list: [82, 65, 93, 0, 60, 31, 99, 90, 31, 70]

    After optimized bubble sort: [0, 31, 31, 60, 65, 70, 82, 90, 93, 99]

    42 comparisons; 23 swaps

    The list: [82, 65, 93, 0, 60, 31, 99, 90, 31, 70]

    After selection sort: [0, 31, 31, 60, 65, 70, 82, 90, 93, 99]

    45 comparisons; 9 swaps

    The list: [82, 65, 93, 0, 60, 31, 99, 90, 31, 70]

    After insertion sort: [0, 31, 31, 60, 65, 70, 82, 90, 93, 99]

    39 comparisons; 23 swaps

## And one more:

    The list: [63, 16, 78, 69, 36, 36, 3, 66, 75, 100]

    After bubble sort: [3, 16, 36, 36, 63, 66, 69, 75, 78, 100]

    45 comparisons; 17 swaps

    The list: [63, 16, 78, 69, 36, 36, 3, 66, 75, 100]

    After optimized bubble sort: [3, 16, 36, 36, 63, 66, 69, 75, 78, 100]

    42 comparisons; 17 swaps

    The list: [63, 16, 78, 69, 36, 36, 3, 66, 75, 100]

    After selection sort: [3, 16, 36, 36, 63, 66, 69, 75, 78, 100]

    45 comparisons; 9 swaps

    The list: [63, 16, 78, 69, 36, 36, 3, 66, 75, 100]

    After insertion sort: [3, 16, 36, 36, 63, 66, 69, 75, 78, 100]

    33 comparisons; 17 swaps

There are other lists commented out in the function included in the template that have more predictable
patterns (e.g., already sorted, reverse sorted, almost sorted, etc) and make for an interesting look at how
the different sorting algorithms work.

## To help clarify, here are some specifics and/or constraints:

1. Each sorting algorithm must be implemented in its own function that only takes the list as an
input parameter and returns both the number of comparisons and swaps made as outputs
(more details later);

2. Each sorting algorithm must be provided the exact same list so that a proper comparison between
the different sorting algorithms can be made;

3. You must include a meaningful header, use good coding style, use meaningful variable names,
and comment your source code where appropriate;

4. Your output should be like the sample runs shown above; and

5. You must submit your source code as a single .py file.

You may have noticed that the sorting algorithms must return both the number of comparisons and
swaps made during sorting. How can a function return two values? Glad you asked. Python is a
powerful general purpose language and allows such a thing! It's simple, actually! Here's an example:
def bubbleSort(nums):

    comparisons = 0

    swaps = 0

    # do some bubble sorting

    # (figure out how to count comparisons and swaps)

    # …

    # sorting is done!

    return comparisons, swaps

Notice how the return statement includes both variables (separated by a comma). Capturing these in the
function call as they are returned is also pretty simple:

    comps, swaps = bubbleSort(nums)

And that's it! The variables comps and swaps will contain the matching returned values of the variables
comparisons and swaps in the function bubbleSort.
