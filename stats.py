import random


####
# Version 0.1 - JF
###

def generate_random_int_list(max_length, upper_bound):
    # generate random length between 2 and max_length
    list_length = int(random.uniform(2, max_length))

    # given the length above, sample the Natural Numbers up to upper_bound that many times
    vars = random.sample(range(upper_bound), list_length)

    # return the generated list
    return vars

# Diagnostic #2: complete the methods calculate_mean and calculate_std_dev

class StatsPackage:

    def __init__(self):
        # Do nothing! :)
        return

    # complete the method implementation to calculate the mean of an unknown list
    def calculate_mean(self, nums):
       mean = sum(nums) / len(nums)
       return int(mean)



    # complete the method implementation to calculate the standard deviation
    # https://mathworld.wolfram.com/StandardDeviation.html
    def calculate_std_dev(self, nums):

        mean = sum(nums) / len(nums)
        top = 0
        for i in nums:
            top += ((i - mean)**2)
        st_dev = ((top/len(nums))**0.5)

        return int(st_dev)


if __name__ == "__main__":
    print('Welcome to the stats program!!')

    print('Now generating a random length list of random integers....')
    rands = generate_random_int_list(100, 10000)

    stats_package = StatsPackage()

    print('List mean is ' + str(stats_package.calculate_mean(rands)))
    print('List standard deviation is ' + str(stats_package.calculate_std_dev(rands)))

    print('All done!')