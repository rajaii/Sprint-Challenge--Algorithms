#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)The runtime of this is O(n) because there is only one loop and one command being run on each iteration.  It would seem because of the a < n^3 that this would not be so.  But upon closer inspection of the resetting of a in the actual operation the n^2 cancels out mathematically from the while condition thus yielding an actual increase in operations of linear nature.  As n increases the amout of operations increases linearly making it o(n)


b)
This is o(n log n).  We have a nested loop structure and thus we will as the size of n increases the amount of operations will increase.  But j approaches n quickly because of the j *= 2 so when you pug such a function and run it and look at the steps taken to run it, they increase slightly more than linear.  In fact between n of 2-9 they are linear increases of 12 steps each time with a once in a while larger amount of steps averaging out to o n log n. 

c)
This is o(n).  It has a recursive call with a short stack resovling at a bunnies == 0 base case. The steps involved in running the code increase linearly by 4 steps as n increases.

## Exercise II


I would use the same thing that gets used in binary search.  I would start in the middle, and drop one and see if it breaks, if it does, I would go up half of the floors left, and if not I would go down half the floors left.
I would keep repeating the process halfing the floors left until I 0 in on the correct floor for f.

This would give a runtime of Ologn which is very efficient.
