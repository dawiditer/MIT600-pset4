##Given I earn 50,000 and I plan to use it all 5 years in retirement, whats the math

def nestEggVariable(salary, save, growthRates):
    """Calculates the amount of savings you have each year"""
    salary = abs(float(salary))
    save = abs(float(save))
    if save > 100: return "Save should be less than 100"
    if len(growthRates) == 0: return "No growth rates entered"
    years = len(growthRates)
    calc_fixed_funds = salary*save*0.01
    funds_lst = [[]]*years
    funds_lst[0] = calc_fixed_funds
    for year in xrange(1,years):
        calc_growth = 1 + 0.01*growthRates[year]
        funds_lst[year] = funds_lst[year-1]*calc_growth + calc_fixed_funds
    return funds_lst

def postRetirement(savings, growthRates, expenses):
    """Calculates the amount of cash you have left after making constant annual withdrawals"""
    expenses = abs(float(expenses))
    savings = abs(float(savings))
    years = len(growthRates)
    rem_funds = [[]]*years
    rem_funds[0] = savings*(1+0.01*growthRates[0]) - expenses
    for year in xrange(1,years):
        rem_funds[year] = rem_funds[year-1]*(1+0.01*growthRates[year]) - expenses
    return rem_funds

def findMaxExpenses(salary, save, preRetireGrowthRates, postRetireGrowthRates,
                    epsilon=0.001):
    """Finds the max annual expense you can withdraw to
    empty your account in len(postRetireGrowthRates) years"""
    savings = nestEggVariable(salary, save, preRetireGrowthRates)[-1]
    
    low = 0
    high = savings
    expenses = (low+high)/2
    
    current_rem_funds = postRetirement(savings, postRetireGrowthRates, expenses)[-1]
    while abs(current_rem_funds) > epsilon:
        current_rem_funds = postRetirement(savings, postRetireGrowthRates, expenses)[-1]
        if current_rem_funds < epsilon:
            high = expenses
        elif current_rem_funds > epsilon:
            low = expenses
        else: break
        expenses = (low+high)/2
    return expenses

salary = 2582
save = 10
preRetireGrowthRates = [3, 4, 5, 0, 3]
postRetireGrowthRates = [10, 5, 0, 5, 1]
epsilon = .01
expenses = 2000
print "_"*71,"\n"
print "\t\t\tRETIREMENT FUNDS CALCULATOR"
print "_"*71,"\n"

print "Salary: ", salary
print "%i%s going to retirement fund" % (save,'%')
print "Annual savings fund growth rate(%):",",".join(map(str, preRetireGrowthRates))
print "Annual retirement fund growth rate(%):",",".join(map(str, postRetireGrowthRates)),"\n"

print "Work years:"
print "-"*71
annual_savings_lst = nestEggVariable(salary, save, preRetireGrowthRates)
print "Annual savings(from year1 to retirement): "
print " ",", ".join(map(str, annual_savings_lst))
print "-"*71,"\n"

print "Retirement period:"
print "-"*71
annual_remaining_savings_lst = postRetirement(annual_savings_lst[-1], postRetireGrowthRates, expenses)
print "Annual remaining savings(%s annual expenses):" % expenses
print " ",", ".join(map(str, annual_remaining_savings_lst))
print "-"*71,"\n"

print "Retirement period:"
print "-"*71
to_fin = findMaxExpenses(salary, save, preRetireGrowthRates, postRetireGrowthRates, epsilon)
print "Max Annual Expenses to empty account in %s years : %s" % (len(postRetireGrowthRates),to_fin)
annual_remaining_savings_lst = postRetirement(annual_savings_lst[-1], postRetireGrowthRates, to_fin)
print "Annual remaining savings:"
print " ",", ".join(map(str, annual_remaining_savings_lst))
print "-"*71,"\n"
