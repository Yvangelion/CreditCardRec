import math

# ===== CONFIG =====
USE_STATIC_VALUES = True  # Set to True for static mode, False for interactive mode

# --- Static Mortgage Values ---
STATIC_MORTGAGE = {
    "home_price": 400_000,
    "down_payment": 80_000,
    "loan_term_years": 30,
    "annual_interest_rate": 6.5,
    "property_tax_rate": 1.2,   # % per year
    "homeowners_insurance": 120, # per month
    "pmi": 0,                    # per month
    "hoa": 50                    # per month
}

# --- Static Investment Values ---
STATIC_INVESTMENT = {
    "starting_amount": 20000,
    "investment_length_years": 30,
    "return_rate_annual": 8,
    "compounding_choice": "monthly",  # "annual", "quarterly", "monthly"
    "monthly_contribution": 500
}
# ==================


def mortgage_vs_investment():
    # --- Mortgage Inputs ---
    if USE_STATIC_VALUES:
        home_price = STATIC_MORTGAGE["home_price"]
        down_payment = STATIC_MORTGAGE["down_payment"]
        loan_term_years = STATIC_MORTGAGE["loan_term_years"]
        annual_interest_rate = STATIC_MORTGAGE["annual_interest_rate"] / 100
        property_tax_rate = STATIC_MORTGAGE["property_tax_rate"] / 100
        homeowners_insurance = STATIC_MORTGAGE["homeowners_insurance"]
        pmi = STATIC_MORTGAGE["pmi"]
        hoa = STATIC_MORTGAGE["hoa"]
    else:
        home_price = float(input("Home price ($): "))
        down_payment = float(input("Down payment ($): "))
        loan_term_years = int(input("Loan term (years): "))
        annual_interest_rate = float(input("Annual mortgage interest rate (%): ")) / 100
        property_tax_rate = float(input("Annual property tax rate (% of home price): ")) / 100
        homeowners_insurance = float(input("Homeowners insurance per month ($): "))
        pmi = float(input("PMI per month ($, 0 if none): "))
        hoa = float(input("HOA fees per month ($): "))
    
    loan_amount = home_price - down_payment
    monthly_interest_rate = annual_interest_rate / 12
    total_months = loan_term_years * 12
    
    mortgage_payment = loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate)**total_months) / \
                       ((1 + monthly_interest_rate)**total_months - 1)
    
    monthly_property_tax = (home_price * property_tax_rate) / 12
    total_monthly_payment = mortgage_payment + monthly_property_tax + homeowners_insurance + pmi + hoa
    
    # --- Investment Inputs ---
    if USE_STATIC_VALUES:
        starting_amount = STATIC_INVESTMENT["starting_amount"]
        investment_length_years = STATIC_INVESTMENT["investment_length_years"]
        return_rate_annual = STATIC_INVESTMENT["return_rate_annual"] / 100
        compounding_choice = STATIC_INVESTMENT["compounding_choice"].strip().lower()
        monthly_contribution = STATIC_INVESTMENT["monthly_contribution"]
    else:
        starting_amount = float(input("Starting investment amount ($): "))
        investment_length_years = int(input("Investment length (years): "))
        return_rate_annual = float(input("Expected annual return rate (%): ")) / 100
        compounding_choice = input("Compounding frequency (annual, quarterly, monthly): ").strip().lower()
        monthly_contribution = float(input("Monthly contribution ($): "))
    
    compounding_map = {"annual": 1, "quarterly": 4, "monthly": 12}
    compounding_frequency = compounding_map.get(compounding_choice, 12)
    
    # --- Simulation ---
    portfolio_value = starting_amount
    remaining_mortgage = loan_amount
    month = 0
    found_month = None
    
    while month < investment_length_years * 12:
        # Mortgage update
        interest_payment = remaining_mortgage * monthly_interest_rate
        principal_payment = mortgage_payment - interest_payment
        remaining_mortgage -= principal_payment
        remaining_mortgage = max(remaining_mortgage, 0)
        
        # Investment update
        months_per_period = 12 / compounding_frequency
        if (month + 1) % months_per_period == 0:
            portfolio_value *= (1 + return_rate_annual / compounding_frequency)
        portfolio_value += monthly_contribution
        
        if found_month is None and portfolio_value > remaining_mortgage:
            found_month = month + 1
            
        month += 1
    
    # --- Output ---
    print("\n==== Results ====")
    print(f"Monthly mortgage payment (P+I only): ${mortgage_payment:,.2f}")
    print(f"Total monthly payment (P+I+Taxes+Ins+PMI+HOA): ${total_monthly_payment:,.2f}")
    
    if found_month:
        years = found_month // 12
        months = found_month % 12
        print(f"Portfolio surpasses remaining mortgage after {years} years and {months} months.")
    else:
        print("Portfolio did not surpass mortgage within the investment period.")


if __name__ == "__main__":
    mortgage_vs_investment()
