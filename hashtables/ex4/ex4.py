def has_negatives(a):
    result = []
    my_dict = {}

    # for every number in a
    for number in a:
        # as long as number is less than 0
        if number < 0:
            # add all negative numbers to the dict
            my_dict[-number] = number
    # iterating again
    for number in a:
        # seeing if number is already in the dict
        if number in my_dict:
            # if it is then appending it to the result array
            result.append(number)


    return result


if __name__ == "__main__":
    print(has_negatives([-1,-2,1,2,3,4,-4]))
