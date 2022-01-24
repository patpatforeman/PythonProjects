musk_investment = 1.02 # in billion
ten_year = musk_investment * (1 + (.0175))**10
twenty_year = musk_investment * (1 +(0.0213))**20
print(str(round(ten_year, 2)) + ' Billion')
print(str(round(twenty_year, 2))+ ' Billion')
yearly_income = (twenty_year - musk_investment)/ 20
print(str(round(yearly_income, 2))+ ' Billion')
