musk_investment = 1.02 # Money in Billions
rate_tenner = (1.75/100) # Interest Rate for Ten Years
rate_twenty = (2.13/100) # Interest Rate for Twenty Years

# Calculate Money at the end of the Period
ten_year = musk_investment * (1 + (rate_tenner)) ** 10
twenty_year = musk_investment * (1 + (rate_twenty)) ** 20

# Print out Values at end of Period, in Billions
print('Elon Musk\'s initial investment is $' + str(musk_investment) + ' Billion.')

print('If Musk puts the Tesla Sale money into a ten year bond, the value would increase to $' +
      str(round(ten_year, 2)) + ' Billion.')
print('If Musk puts the Tesla Sale money into a twenty year bond, the value would increase to $' +
      str(round(twenty_year, 2)) + ' Billion.')

# Twenty Year Investment for Musky
yearly_income = (twenty_year - musk_investment) / 20
print('The amount ole Musky would live on from interest on the twenty year investment is $' +
      str(round(yearly_income, 2)) + ' Billion.')
