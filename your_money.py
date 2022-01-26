investment = 6000 # Initial Investment
final_invest = investment * 40 # Final Amount Invested
rate = 0.07 # Interest rate in Decimal Form
invest_time = 40 # Years of Investment

# Calculate Interest Accumulated, then add to Final Investment Total
interest = investment * (((1 + rate)**invest_time)-1)
total_amt = final_invest + interest

# Print out results
print('Your investment adds up to $' + str(final_invest) + ' without interest')
print('The total interest earned on your investment is $' + str(int(interest)))
print('The final amount that your investment comes to is $' + str(int(total_amt)))
