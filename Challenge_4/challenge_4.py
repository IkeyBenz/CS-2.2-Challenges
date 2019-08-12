def memoize(f):
    vals = {}

    def inner(W, wt, val, n):
        if (W, wt, val, n) not in vals:
            vals[(W, wt, val, n)] = f(W, wt, val, n)
        return vals[(W, wt, val, n)]
    return inner


@memoize
def knapSack(W, wt, val, n):

    # Base Case
    if n == 0 or W == 0:
        return 0

    # If weight of the nth item is more than Knapsack of capacity
    # W, then this item cannot be included in the optimal solution
    if (wt[n-1] > W):
        return knapSack(W, wt, val, n-1)

    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included

    return max(val[n-1] + knapSack(W-wt[n-1], wt, val, n-1),
               knapSack(W, wt, val, n-1))


def knapsack(C, items, n):
    ''' A  method to determine the maximum value of the items included in the knapsack 
        without exceeding the capacity  C

        Parameters: 
        C= 50
        items = (("boot", 10, 60),
            ("tent", 20, 100),
            ("water", 30, 120),
            ("first aid", 15, 70))
        Returns: max value
    '''
