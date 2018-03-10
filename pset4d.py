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
