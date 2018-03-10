##Successive Approximation:
##  Retirement App
##  The goal is to use successive approximation to calculate
##  the size of the retirement account at the end of each year

###How to use this function on the variable one
def nestEggFixed(salary, save, growthRate, years):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - growthRate: the annual percent increase in your investment account (an
      integer between 0 and 100).
    - years: the number of years to work.
    - return: a list whose values are the size of your retirement account at
      the end of each year.
    """
    # TODO: Your code here.
    ##setting up guardians
    salary = abs(float(salary))
    save = abs(float(save))
    if save > 100: return "Save should be less than 100"
    if growthRate > 100: return "growth rate should be less than 100"

    ##set up variables
    calc_fixed_funds = salary*save*0.01
    funds_lst = [[]]*years
    funds_lst[0] = calc_fixed_funds
    for year in xrange(1,years):
        calc_growth = 1 + 0.01*growthRate
        funds_lst[year] = funds_lst[year-1]*calc_growth + calc_fixed_funds
    return funds_lst
    ##funds_lst = [[]]*years##list of all 5 years
    
    
def testNestEggFixed(salary,save,growthRate,years = 5):
    savingsRecord = nestEggFixed(salary, save, growthRate, years)
    print savingsRecord

salary = 10000
save = 10
growthRate = 15

testNestEggFixed(salary,save,growthRate)

# Output should have values close to:
# [1000.0, 2150.0, 3472.5, 4993.375, 6742.3812499999995]

# TODO: Add more test cases here.
raw_input("Press enter for next test... ")
testNestEggFixed(40000,15,10)

raw_input("Press enter for next test... ")
testNestEggFixed(10000000,14,5)

raw_input("Press enter for next test... ")
testNestEggFixed(-100,100000,0.9)

raw_input("Press enter for next test... ")
testNestEggFixed(0,5,10)

raw_input("Press enter for next test... ")
testNestEggFixed(50000,10,5)
