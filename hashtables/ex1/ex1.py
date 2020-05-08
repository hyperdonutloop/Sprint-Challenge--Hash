def get_indices_of_item_weights(weights, length, limit):
    # use a hashtable
    my_dict = {}
    # weight limit = limit
    # list of weights
    # find two items whose sum of weights = weight limit
    # return those two items

    
    # iterate through the list
    for i in range(length):
        # store weight as keys and index as values
        weight = weights[i]
        # storing in dict. 
        # saying value = index
        my_dict[weight] = i
    
    for j in range(length):
        # assigning key to limit-weight
        key = limit - weights[j]
        # then checking if key is in the dictionary
        if key in my_dict:
            # if it is then return the key
            # my_dict[key] in the solution example would be 6, the value of 6 is 1 
            # j would be the index 3 which is 15, the number we found when subtracting limit-weight
            return (my_dict[key], j)

