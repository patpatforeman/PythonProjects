musk_investment = 1.02 # Money in Billions
rate_tenner = (1.75/100) # Interest Rate for Ten Years
rate_twenter = (2.13/100) #Interest Rate for Twenty Years

# Calculate Money at the end of the Period
ten_year = musk_investment * (1 + (rate_tenner))** 10 
twenty_year = musk_investment * (1 +(rate_twenter))** 20

# Print out Values at end of Period, in Billions
print(str(round(ten_year, 2)) + ' Billion')
print(str(round(twenty_year, 2))+ ' Billion')

# Twenty Year Investment for Musky
yearly_income = (twenty_year - musk_investment)/ 20
print(str(round(yearly_income, 2))+ ' Billion')
