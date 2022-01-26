# bring in randomness cause we need it in our lives
import random


# copy in Dr. Forsyth's random list function for use
def generate_random_int_list(max_length, upper_bound):
    # generate random length between 2 and max_length
    list_length = int(random.uniform(2, max_length))

    # given the length above, sample the Natural Numbers up to upper_bound that many times
    vars = random.sample(range(upper_bound), list_length)

    # return the generated list
    return vars


# generate two random lists of integers
max_length = 100; upper_bound=1000000
nums = generate_random_int_list(max_length, upper_bound)

# see how long this list is
print("The list contains "+str(len(nums))+" values total.")

# Label starting counts for even and odds
even = 0
odd = 0

# Run through list, adding 1 to the count when it appears
for i in nums:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

# Print out the count of each type
print('\r\nThe number of even numbers is ' + str(even) + '.')
print('The number of odd numbers is ' + str(odd) + '.')

# Double Check Message
print('\r\nTo make sure each value in the list was counted, here is the' +
      '\nvalue that adding the even and odd counts produces: ' + str(even + odd) + '.')

# Convert the count into a percentage value
percent_even = (even / len(nums)) * 100
percent_odd = (odd / len(nums)) * 100

# Print out percentages rounded to two decimal places
print('\r\nThe percentage of even numbers in this list is ' + str(round(percent_even, 2)) + '%.')
print('The percentage of even numbers in this list is ' + str(round(percent_odd, 2)) + '%.')
