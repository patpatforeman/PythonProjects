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
max_length = 1000; upper_bound=1000000
A = generate_random_int_list(max_length, upper_bound)

B = generate_random_int_list(max_length, upper_bound)

# Define Variables for the standard deviation equation
top_A = 0
mean_A = sum(A) / len(A)
top_B = 0
mean_B = sum(B) / len(B)

# Create loops that generate the standard deviation for each list
for i in A:
    top_A += ((i - mean_A) ** 2)
    st_dev_A = ((top_A / len(A)) ** 0.5)
for i in B:
    top_B += ((i - mean_B) ** 2)
    st_dev_B = ((top_B / len(B)) ** 0.5)

# Print out SD values for verification purposes
print('List A has a standard deviation of ' + str(int(st_dev_A)) + ', and List B has a'
      ' standard deviation of ' + str(int(st_dev_B)) + '.')

# If Else statement that compares the two deviations and prints out the list with
# the largest SD
if st_dev_A > st_dev_B:
    print('\r\nList A has the greater Standard Deviation.')
if st_dev_A == st_dev_B:
    print('\r\nBoth lists have the same Standard Deviation')
if st_dev_A < st_dev_B:
    print('\r\nList B has the greater Standard Deviation.')

