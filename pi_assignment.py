# import pi function from math module
from math import pi

# Set Initial Values
a = 1
b = 1/(2**(1/2))
t = 1/4
p = 1
loop = range(1, 11)

# Create a loop to iterate through ten times
for i in loop:
    a_n = ((a+b) / 2)
    b_n = ((b*a)**(1/2))
    t_n = t - p * ((a - a_n) ** 2)
    p_n = (2 * p)

# This Section gives me my pi approximation and the percent difference between my pi
# and Python's pi
    approx_pi = ((a_n + b_n) ** 2) / (4 * t_n)
    percent_diff = (abs((approx_pi - pi) / pi)) * 100

# This simply appends the initial values to the final values to increase accuracy through the loop
    a = a_n
    b = b_n
    t = t_n
    p = p_n

# Print statement showing approximation and percent difference
    print('\r\nThe approximation of pi on loop ' + str(loop[i - 1]) + ' is ' + str(approx_pi) + '.'
          '\r\nThe percent difference between the two is ' + str(percent_diff) + '%.')