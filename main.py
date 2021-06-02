#!/usr/bin/env python3

# Created by: Myles Trump
# Created on: May 2021
# This program randomizes 10 numbers and figures out their average

import random


def main():
    # this function randomizes 10 numbers and figures out their average

    my_numbers = []
    sum = 0

    # input
    for loop_counter in range(0, 10):
        randomized_number = random.randint(1, 100)  # a number between 1-100
        my_numbers.append(randomized_number)

    print("Your numbers are: ", end="")

    for loop_counter in range(0, 10):
        print("{0} ".format(my_numbers[loop_counter]), end="")
        sum = sum + my_numbers[loop_counter]

    sum_final = sum / len(my_numbers)
    print("\n\nThe average of all those numbers is {0}.".format(sum_final))


if __name__ == "__main__":
    main()
