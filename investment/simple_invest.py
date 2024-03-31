def future_value(PV, R, t, m, PMT, option):
    if option == 'monthly':
        n = t * m
        r = R / m
    elif option == 'yearly':
        n = t
        r = R
    else:
        print("Invalid option.")
        return None
    
    FV = PV * (1 + r)**n + PMT * ((1 + r)**n - 1) / r
    return FV

# Given data
PV = 20000  # Present Value
R = 0.10   # Annual interest rate
t = 10      # Number of years
PMT = 2500   # Monthly payment

# Compounded monthly
option = 'monthly'
FV_monthly = future_value(PV, R, t, 12, PMT, option)
print("Future value compounded monthly:", round(FV_monthly, 2))

# Compounded yearly
option = 'yearly'
FV_yearly = future_value(PV, R, t, 1, PMT, option)
print("Future value compounded yearly:", round(FV_yearly, 2))
