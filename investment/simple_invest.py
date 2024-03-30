import numpy as np
import matplotlib.pyplot as plt

def investment_calculator(starting_amount, years, return_rate, annual_compound, additional_contributions=0, contribution_growth_rate=0, inflation_rate=0):
    final_values = []
    annual_schedule = []
    total_amount = starting_amount
    for year in range(years):

        #total_amount *= (1 + return_rate / 100 / annual_compound)
        total_amount += (additional_contributions*12) * ((1 + contribution_growth_rate / 100) ** year)
        total_amount /= (1 + inflation_rate / 100)
        
        final_values.append(total_amount)
        annual_schedule.append(total_amount)

    return final_values, annual_schedule

def plot_results(years, final_values):
    plt.figure(figsize=(10, 5))
    plt.plot(np.arange(1, years + 1), final_values, marker='o', linestyle='-')
    plt.title('Investment Growth Over Time')
    plt.xlabel('Years')
    plt.ylabel('Final Amount')
    plt.grid(True)
    plt.show()

def plot_pie_chart(final_values):
    labels = ['Starting Amount', 'Final Amount']
    amounts = [final_values[0], final_values[-1]]
    explode = (0, 0.1)

    plt.figure(figsize=(7, 7))
    plt.pie(amounts, explode=explode, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title('Composition of Final Amount')
    plt.show()

def main():
    starting_amount = 20000 #float(input("Enter starting amount: "))
    years = 10 #int(input("Enter number of years: "))
    return_rate_percent = 10 #float(input("Enter return rate (in percent): "))
    annual_compound = 1 #int(input("Enter annual compound: "))
    additional_contributions = 2500 #float(input("Enter additional contributions: "))
    contribution_growth_rate = 10 #float(input("Enter contribution growth rate (in percent): "))
    inflation_rate = 0 #float(input("Enter inflation rate (in percent): "))

    return_rate = return_rate_percent / 100  # Convert percentage to decimal

    final_values, annual_schedule = investment_calculator(starting_amount, years, return_rate, annual_compound, additional_contributions, contribution_growth_rate, inflation_rate)

    plot_results(years, final_values)
    plot_pie_chart(final_values)
    print("Annual Schedule of Amount Growth:")
    for year, amount in enumerate(annual_schedule, start=1):
        print(f"Year {year}: ${amount:.2f}")

if __name__ == "__main__":
    main()
