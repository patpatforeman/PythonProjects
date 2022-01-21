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

#Diagnostic #1: Complete the methods student_min, student_max, and runner_up

# write a function to determine the minimum value in the list
# Don't use the min() function. That's too easy :)
def student_min(nums):
    init = nums[0]
    for i in nums:
        if i < init:
            init = i
        else:
            continue
    min = init
    return min


# write a function to determine the maximum value in the list
# Don't use the max() function. That's too easy :)
def student_max(nums):
    init = nums[0]
    for i in nums:
        if i > init:
            init = i
        else:
            continue
    max = init
    return max


# write a function that determines the 2nd highest value in the list. Not #1, but the runner up :)
def runner_up(nums):
    init_1 = nums[0]
    for i in nums:
        if i > init_1:
            init_1 = i
        else:
            continue
    mumps = init_1
    init_2 = nums[0]
    if mumps == nums[0]:
        init_2 = nums[1]
    for n in nums:
        if n > init_2 and n < mumps:
            init_2 = n
        else:
            continue
    return init_2


if __name__ == "__main__":
    print('Welcome to the program!')

    print('Now generating a random length list of random integers....')
    rands = generate_random_int_list(10, 100)

    print('Random List is:')
    print(rands)

    print('Now running your code to determine the minimum value...')
    print('Maximum value is ' + str(student_max(rands)))
    print('Minimum value is ' + str(student_min(rands)))
    print('Second Highest value is ' + str(runner_up(rands)))

    print('All done!')