# python_decoder

This python decoder reads in a text file that has a decoded message. The text file will be in a format like such, where each line contains a number and its associated "code word":

3 like
6 pizza
2 moose
4 star
1 I
5 pineapple

It takes each line and puts the number and code word into a dictionary that is used as the "decoder". It then takes the numbers and forms them into an ordered pyramid like so:

1
23
456

The number at the end of each row is the number that is used to look up the code words. So the encoded message will be of the form:

1 3 6
Which corresponds to "I like pizza"

In this case where all of the numbers from 1 to 6 are used, you could simplify the code by using a formula instead of a for loop and if-elif-else block to create the pyramid. Since the pyramid is formed manually instead, you can use any set of numbers in the code word file. For instance, if you passed this file, you would get the same output:

43 like
96 pizza
22 moose
64 star
1 I
85 pineapple
