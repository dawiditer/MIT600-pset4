#
# Problem 2
#

def nestEggVariable(salary, save, growthRates):
    # TODO: Your code here.
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - growthRate: a list of the annual percent increases in your investment
      account (integers between 0 and 100).
    - return: a list of your retirement account value at the end of each year.
    """
    ##setting up guardians
    salary = abs(float(salary))
    save = abs(float(save))
    if save > 100: return "Save should be less than 100"
    if len(growthRates) == 0: return "No growth rates entered"

    ##set up variables
    years = len(growthRates)
    calc_fixed_funds = salary*save*0.01
    funds_lst = [[]]*years
    funds_lst[0] = calc_fixed_funds
    for year in xrange(1,years):
        calc_growth = 1 + 0.01*growthRates[year]
        funds_lst[year] = funds_lst[year-1]*calc_growth + calc_fixed_funds
    return funds_lst

def testNestEggVariable(salary,save,growthRates):
    savingsRecord = nestEggVariable(salary, save, growthRates)
    print savingsRecord
    
salary = 10000
save = 10
growthRates = [3, 4, 5, 0, 3]
testNestEggVariable(salary,save,growthRates)
    # Output should have values close to:
    # [1000.0, 2040.0, 3142.0, 4142.0, 5266.2600000000002]

    # TODO: Add more test cases here. raw_input("Press enter for next test... ")
testNestEggVariable(40000,15,[1,2,0])

raw_input("Press enter for next test... ")
testNestEggVariable(10000000,14,[5,3,2])

raw_input("Press enter for next test... ")
testNestEggVariable(-100,100000,growthRates)

raw_input("Press enter for next test... ")
testNestEggVariable(0,5,growthRates)

raw_input("Press enter for next test... ")
testNestEggVariable(50000,10,[5])
