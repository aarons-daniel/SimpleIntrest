def calculate_simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest

# Take user input
principal_amount = float(input("Enter the PRINCIPAL amount: "))
print('Trying to add an extra line')
interest_rate = float(input("Enter the Interest rate (%): "))
time_period = float(input("Enter the time period (in years): "))

simple_interest = calculate_simple_interest(principal_amount, interest_rate, time_period)
print("Simple Interest:", simple_interest)
