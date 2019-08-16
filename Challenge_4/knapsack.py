# Got help from Jake Shams
def knapsack(items, capacity):
    '''inputs:
            an array of tuples with weights and values
            maximum capacity of the bag
        output:
            the max value that can fit in the bag
        '''
    if len(items) == 0 or capacity == 0:
        return 0

    weight, val = items[0]
    if weight > capacity:  # If weight is too much, disregard this one
        return knapsack(items[1:], capacity)

    value_without = knapsack(items[1:], capacity)
    value_with = knapsack(items[1:], capacity - weight) + val

    return max(value_with, value_without)
