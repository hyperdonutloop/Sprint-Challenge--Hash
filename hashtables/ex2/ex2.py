#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    # link tickets together, in array?
    # starting location is key, destination is value
    route = []
    my_stupid_dict = {}

    for each_ticket in tickets:
        # storing the source and destination as key,value in dict
        my_stupid_dict[each_ticket.source] = each_ticket.destination

    # finding the first ticket and adding it to the route
    # finding it by key of NONE because if the source location is NONE it means it's the starting point
    route.append(my_stupid_dict['NONE'])
    # iterating through the other tickets
    # initializing key
    key = my_stupid_dict['NONE']
    # while place does not equal none
    while key != 'NONE':
        # appending the key in the dictionary (source destination) to the route
        route.append(my_stupid_dict[key])
        # linking together the matching key values
        key = my_stupid_dict[key]

    return route
