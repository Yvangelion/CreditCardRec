import math
from datetime import datetime, timedelta

# ===== CONFIG =====
USE_STATIC_VALUES = True  # Set to True for static mode, False for interactive mode

# --- Static Mortgage Values ---
STATIC_MORTGAGE = {
    "home_price": 100_000,
    "down_payment": 23_500,
    "loan_term_years": 30,
    "annual_interest_rate": 6.775,
    "property_tax_rate": 1,       # % per year
    "homeowners_insurance": 79,   # per month
    "pmi": 120,                   # per month
    "hoa": 0,                     # per month
    "start_date": "2025-01-01",   # YYYY-MM-DD
    "home_growth_rate": 2.5        # % annual growth in home value
}

# --- Static Investment Values ---
STATIC_INVESTMENT = {
    "starting_amount": 10_000,
    "investment_length_years": 30,  # This is just how long we track growth
    "return_rate_annual": 6,
    "compounding_choice": "annual",  # "annual", "quarterly", "monthly"
    "monthly_contribution": 50
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
        start_date = datetime.strptime(STATIC_MORTGAGE["start_date"], "%Y-%m-%d")
        home_growth_rate = STATIC_MORTGAGE["home_growth_rate"] / 100
    else:
        home_price = float(input("Home price ($): "))
        down_payment = float(input("Down payment ($): "))
        loan_term_years = int(input("Loan term (years): "))
        annual_interest_rate = float(input("Annual mortgage interest rate (%): ")) / 100
        property_tax_rate = float(input("Annual property tax rate (% of home price): ")) / 100
        homeowners_insurance = float(input("Homeowners insurance per month ($): "))
        pmi = float(input("PMI per month ($, 0 if none): "))
        hoa = float(input("HOA fees per month ($): "))
        start_date_str = input("Mortgage start date (YYYY-MM-DD): ")
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
        home_growth_rate = float(input("Annual home growth rate (%): ")) / 100
    
    loan_amount = home_price - down_payment
    monthly_interest_rate = annual_interest_rate / 12
    total_months = loan_term_years * 12

    mortgage_payment = loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate)**total_months) / \
                       ((1 + monthly_interest_rate)**total_months - 1)

    monthly_property_tax = (home_price * property_tax_rate) / 12

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
    home_value = home_price
    month = 0
    found_date = None
    found_portfolio_value = 0
    found_remaining_mortgage = 0
    pmi_end_date = None
    yearly_data = []
    monthly_data = []

    while month < loan_term_years * 12:
        # Update home value
        home_value *= (1 + home_growth_rate / 12)

        # Check PMI removal point (20% equity)
        equity_ratio = 1 - (remaining_mortgage / home_value)
        if pmi_end_date is None and equity_ratio >= 0.20:
            pmi_end_date = start_date + timedelta(days=(month+1) * 30.4375)

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

        current_date = start_date + timedelta(days=(month+1) * 30.4375)

        # Monthly total payment (stop PMI after removal date)
        current_pmi = pmi if (pmi_end_date is None or current_date < pmi_end_date) else 0
        total_monthly_payment = mortgage_payment + monthly_property_tax + homeowners_insurance + current_pmi + hoa

        # Record yearly snapshot
        if (month + 1) % 12 == 0:
            yearly_data.append({
                "year": current_date.year,
                "portfolio_value": round(portfolio_value, 2),
                "remaining_mortgage": round(remaining_mortgage, 2),
                "home_value": round(home_value, 2)
            })

        # Record monthly snapshot
        monthly_data.append({
            "year_month": current_date.strftime("%Y-%m"),
            "portfolio_value": round(portfolio_value, 2),
            "remaining_mortgage": round(remaining_mortgage, 2),
            "home_value": round(home_value, 2)
        })

        # Check crossover date
        if found_date is None and portfolio_value > remaining_mortgage:
            found_date = current_date
            found_portfolio_value = portfolio_value
            found_remaining_mortgage = remaining_mortgage

        month += 1

    # --- Save Yearly File ---
    with open("investment/outputs/mortgage_vs_portfolio_yearly.txt", "w") as f_year:
        if found_date:
            f_year.write(f"Portfolio surpasses mortgage on: {found_date.strftime('%Y-%m')}\n")
        else:
            f_year.write("Portfolio never surpasses mortgage within the loan term.\n")
        if pmi_end_date:
            f_year.write(f"PMI removed on: {pmi_end_date.strftime('%Y-%m')}\n\n")
        else:
            f_year.write("PMI never removed within loan term.\n\n")
        f_year.write("Year | Portfolio Value | Remaining Mortgage | Home Value\n")
        f_year.write("-" * 65 + "\n")
        for entry in yearly_data:
            f_year.write(f"{entry['year']} | ${entry['portfolio_value']:,.2f} | "
                         f"${entry['remaining_mortgage']:,.2f} | ${entry['home_value']:,.2f}\n")

    # --- Save Year-Month File ---
    with open("investment/outputs/mortgage_vs_portfolio_monthly.txt", "w") as f_month:
        if found_date:
            f_month.write(f"Portfolio surpasses mortgage on: {found_date.strftime('%Y-%m')}\n")
        else:
            f_month.write("Portfolio never surpasses mortgage within the loan term.\n")
        if pmi_end_date:
            f_month.write(f"PMI removed on: {pmi_end_date.strftime('%Y-%m')}\n\n")
        else:
            f_month.write("PMI never removed within loan term.\n\n")
        f_month.write("Year-Month | Portfolio Value | Remaining Mortgage | Home Value\n")
        f_month.write("-" * 80 + "\n")
        for entry in monthly_data:
            f_month.write(f"{entry['year_month']} | ${entry['portfolio_value']:,.2f} | "
                          f"${entry['remaining_mortgage']:,.2f} | ${entry['home_value']:,.2f}\n")

    # --- Console Output ---
    print("\n==== Results ====")
    print(f"Monthly mortgage payment (P+I only): ${mortgage_payment:,.2f}")
    print(f"Initial total monthly payment (P+I+Taxes+Ins+PMI+HOA): "
          f"${mortgage_payment + monthly_property_tax + homeowners_insurance + pmi + hoa:,.2f}")
    if pmi_end_date:
        print(f"PMI removed on: {pmi_end_date.strftime('%Y-%m')}")
    print(f"Dates portfolio value: ${found_portfolio_value:,.2f}")
    print(f"Dates remaining mortgage: ${found_remaining_mortgage:,.2f}")
    if found_date:
        print(f"Portfolio surpasses remaining mortgage on: {found_date.strftime('%Y-%m')}")
    else:
        print("Portfolio did not surpass mortgage within the loan term.")
    print("Data saved to 'mortgage_vs_portfolio_yearly.txt' and 'mortgage_vs_portfolio_monthly.txt'")
    print("\n==== Done! ====\n")


if __name__ == "__main__":
    mortgage_vs_investment()
