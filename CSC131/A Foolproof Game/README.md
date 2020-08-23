# Program: A Foolproof Game

## Your task in this programming assignment is to write a Python program that plays the “Heads andtails...sort of” game described in the lesson on Chaos. Recall the game: two coins are simultaneously flipped, and the results are recorded. The two coins can either both be heads, both be tails, or they can be different (i.e., one is heads and one is tails). If both coins land on heads, Group A gets a point. If both coins land on tails, Group B gets a point. If one coin lands on heads and the other lands on tails, the Prof gets a point. The group (or individual) with the most points at the end of a game wins. Of course, the purpose of this program is to play this game many times, and for each game make many flips of the coins. In the end, we should see interesting results. Before listing any requirements, let's take a look at a sample run of a correct program (with user input highlighted in bold black):

How many games? **1**

How many coin tosses per game? **100**

Game 0:

Group A: 25 (25.0%); Group B: 19 (19.0%); Prof: 56 (56.0%)

Wins: Group A=0 (0.0%); Group B=0 (0.0%); Prof=1 (100.0%)

### Here's another sample run:

How many games? **1**

How many coin tosses per game? **5**

Game 0:

Group A: 3 (60.0%); Group B: 0 (0.0%); Prof: 2 (40.0%)

Wins: Group A=1 (100.0%); Group B=0 (0.0%); Prof=0 (0.0%)

### Oh noes, the prof didn't win! Well, here's another one:

How many games? **5**

How many coin tosses per game? **10**

Game 0:

Group A: 3 (30.0%); Group B: 1 (10.0%); Prof: 6 (60.0%)

Game 1:

Group A: 6 (60.0%); Group B: 1 (10.0%); Prof: 3 (30.0%)

Game 2:

Group A: 4 (40.0%); Group B: 1 (10.0%); Prof: 5 (50.0%)

Game 3:

Group A: 4 (40.0%); Group B: 1 (10.0%); Prof: 5 (50.0%)

Game 4:

Group A: 5 (50.0%); Group B: 3 (30.0%); Prof: 2 (20.0%)

Wins: Group A=2 (40.0%); Group B=0 (0.0%); Prof=3 (60.0%)

### And another:

How many games? **3**

How many coin tosses per game? **16**

Game 0:

Group A: 3 (18.75%); Group B: 4 (25.0%); Prof: 9 (56.25%)

Game 1:

Group A: 1 (6.25%); Group B: 7 (43.75%); Prof: 8 (50.0%)

Game 2:

Group A: 6 (37.5%); Group B: 3 (18.75%); Prof: 7 (43.75%)

Wins: Group A=0 (0.0%); Group B=0 (0.0%); Prof=3 (100.0%)

### And one more:

How many games? **1000**

How many coin tosses per game? **1000**

Game 0:

Group A: 277 (27.7%); Group B: 240 (24.0%); Prof: 483 (48.3%)

Game 1:

Group A: 265 (26.5%); Group B: 226 (22.6%); Prof: 509 (50.9%)

…

Game 998:

Group A: 241 (24.1%); Group B: 257 (25.7%); Prof: 502 (50.2%)

Game 999:

Group A: 254 (25.4%); Group B: 251 (25.1%); Prof: 495 (49.5%)

Wins: Group A=0 (0.0%); Group B=0 (0.0%); Prof=1000 (100.0%)

That's more like it...

## From the sample runs, several things can be observed that help to identify and clarify requirements, specifics, and/or constraints:

1. You must obtain user input for the total number of games to play and the total number of coin
tosses per game;

2. For each game, you must properly make and record the coin tosses, and determine a winner;

3. Statistics must be displayed for each game, including the number of coin toss wins and
percentage of coin toss wins for each group;

4. Statistics must be displayed over all the games, including the number of games won and
percentage of games won for each group;

5. You must include a meaningful header, use good coding style, use meaningful variable names,
and comment your source code where appropriate;

6. Your output should be like the sample runs shown above (of course, actual input values and the
resulting output will vary depending on the provided inputs); and

7. You must submit your source code as a single .py file.

## There is one more thing to discuss. What should be done if there is a draw (or tie) between two or more groups in a single game? Although this is not likely if the number of tosses in a game is large, it could indeed happen. Suppose, for example, that a game consists of 10 tosses. It is possible that Group A and Group B both win four tosses each, leaving Prof with only two tosses (and losing). So who wins the game between Group A and Group B?

## A simple solution is to randomly select a winner in this case. If Group A and Group B draw a game, randomly select a winner from these two groups. Of course, there could be a three-way tie! The outcome is still the same: randomly select a winner from the three groups.
