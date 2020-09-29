import sys
from collections import Counter
from typing import List
import argparse

class LookupCounter(Counter):
    def incr(self, val):
        if val in self:
            self[val] += 1
        else:
            self[val] = 1

    def decr(self, val):
        if val in self:
            if self[val] <= 1:
                del self[val]
            else:
                self[val] -= 1


def find_numbers_solution(target_num: int, number_set: LookupCounter, current_working: List, level: int) -> List:
    """Recursive function to solve the countdown numbers game. Each call loops through all possible pairs of numbers in
    number_set. An operation is performed on the pair, and the resulting number replaces the pair before recursing. If
    target_num is found in number_set, then the solution has been found.

    Args:
        target_num: The target number to be calculated
        number_set: The available numbers to use. Can include combinations
        current_working: List containing the steps in the solution
        level: the level of the recursion (cannot exceed 5)

    Returns:
        current_working

    """

    if target_num in number_set:
        current_working.append("Found {}.".format(target_num))
        return current_working

    if level > 5:
        return False

    # Convert number_set to a list, where each number appears as many times as its counter value.
    iter_list = list(number_set.elements())

    for idx_1 in range(0, len(iter_list)):
        # Pick first number from the list and remove it
        first_number = iter_list[idx_1]
        number_set.decr(first_number)

        for idx_2 in range(idx_1+1, len(iter_list)):

            # Pick second number from the list and remove it
            second_number = iter_list[idx_2]
            number_set.decr(second_number)

            # Create a new number from the pair using one of four operations and add it to number_set

            # Addition
            new_number = first_number + second_number
            number_set.incr(new_number)

            # Ensure new number is not 0 and recurse with number_set having one less number than before
            if new_number != 0 and find_numbers_solution(target_num, number_set, current_working, level+1):
                current_working.append("{} + {} = {}".format(first_number, second_number, new_number))
                return current_working
            # Otherwise combination is not used in solution so remove it from number_set
            else:
                number_set.decr(new_number)

            # Multiplication
            new_number = first_number * second_number
            number_set.incr(new_number)

            if new_number != 0 and find_numbers_solution(target_num, number_set, current_working, level+1):
                current_working.append("{} * {} = {}".format(first_number, second_number, new_number))
                return current_working
            else:
                number_set.decr(new_number)

            # Subtraction
            new_number = max(first_number,second_number) - min(first_number,second_number)
            number_set.incr(new_number)

            if new_number != 0 and find_numbers_solution(target_num, number_set, current_working, level+1):
                current_working.append(
                    "{} - {} = {}".format(max(first_number, second_number), min(first_number, second_number),
                                          new_number))
                return current_working
            else:
                number_set.decr(new_number)

            # Division (not commutative, but for our purposes don't care about fractions)
            new_number = max(first_number, second_number) / min(first_number, second_number)
            number_set.incr(new_number)

            if new_number != 0 and find_numbers_solution(target_num, number_set, current_working, level + 1):
                current_working.append(
                    "{} / {} = {}".format(max(first_number, second_number), min(first_number, second_number),
                                          new_number))
                return current_working
            else:
                number_set.decr(new_number)

            # If none of the operations produce a new number used in the solution, then add the original number back in
            # the set and try another one.
            number_set.incr(second_number)

        number_set.incr(first_number)

    return False


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='This script solves the countdown numbers game.')
    parser.add_argument('--target', type=int, nargs=1, required=True,
                        help='The target number')
    parser.add_argument('--numbers', type=int, nargs=6, required=True,
                        help='The numbers available to use (six must be provided)')
    args = parser.parse_args()

    target = args.target[0]
    number_set = LookupCounter()

    for arg in args.numbers:
        number_set.incr(arg)

    working = []
    print("Finding solution for {}...".format(target))
    sol = find_numbers_solution(target, number_set, working, 1)
    if sol:
        for line in reversed(working):
            print(line)
    else:
        print("No Solution")
