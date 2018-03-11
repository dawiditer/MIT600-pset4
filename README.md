# Simulating a retirement fund
### Problem 1. ###
Write a function, called `nestEggFixed`, which takes four arguments: 
* a salary, 
* a percentage of your salary to save in an investment account, 
* an annual growth percentage for the investment account, and 
* a number of years to work. 

This function should return a list, whose values are the size 
of your retirement account at the end of each year, with the most 
recent year’s value at the end of the list. 

Complete the implementation of: 
```Python
def nestEggFixed (salary, save, growthRate, years):
```

### Problem 2. ###
Write a function, called `nestEggVariable`, which takes three arguments: 
* a salary (`salary`), 
* a percentage of your salary to save (`save`), and 
* a list of annual growth percentages on investments (`growthRates`). 

The length of the last argument defines the number of years you 
plan to work; 
* `growthRates[0]` is the growth rate of the first year, 
* `growthRates[1]` is the growth rate of the second year, etc.

(Note that because the retirement fund’s initial value is 0, `growthRates[0]` 
is, in fact, irrelevant.)  This function should return a list, whose values are the size of your 
retirement account at the end of each year. 

Complete the implementation of: 
```Python
def nestEggVariable(salary, save, growthRates): 
```

### Problem 3. ###
Write a function, called `postRetirement`, which takes three arguments: 
* an initial amount of money in your retirement fund (`savings`), 
* a list of annual growth percentages on investments while you are retired (`growthRates`), 
* and your annual expenses (`expenses`). 

Assume that the increase in the investment account savings is calculated
before subtracting the annual expenditures.  
Your function should return a list of fund sizes after each year of retirement, 
accounting for annual expenses and the growth of the retirement fund. 

Like problem 2, the length of the `growthRates` argument defines the number 
of years you plan to be retired.
Note that if the retirement fund balance becomes negative, expenditures should 
continue to be subtracted, and the growth rate comes to represent the interest
rate on the debt.

Complete the definition for:
```Python
def postRetirement(savings, growthRates, expenses):
```

### Problem 4. ### 
Write a function, called `findMaxExpenses`, which takes five arguments: 
* a salary (`salary`), 
* a percentage of your salary to save (`save`), 
* a list of annual growth percentages on investments while you are still working (`preRetireGrowthRates`), 
* a list of annual growth percentages on investments while you are retired (`postRetireGrowthRates`), 
* and a value for epsilon (`epsilon`). 

As with problems 2 and 3, the lengths of `preRetireGrowthRates` and `postRetireGrowthRates` determine the number of years you plan to be working and retired, respectively. 

Use the idea of binary search to find a value for the amount of expenses you can withdraw each year from your retirement fund, such that at the end of your retirement, the absolute value of the amount remaining in your retirement fund is less than epsilon (note that you can overdraw by a small amount).  Start with a range of possible values for your annual expenses between 0 and your savings at the start of your retirement (*HINT #1: this can be determined by utilizing your solution to problem 2*).

Your function should print out the current estimate for the amount of expenses on each iteration through the binary search (*HINT #2: your binary search should make use of your solution to problem 3*), and should return the estimate for the amount of expenses to withdraw. )(*HINT #3: the answer should lie between zero and the initial value of the savings + epsilon.*) 

Complete the implementation of: 
```Python
def findMaxExpenses(salary, save, preRetireGrowthRates, postRetireGrowthRates, epsilon)
```
