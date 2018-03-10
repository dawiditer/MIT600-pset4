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
