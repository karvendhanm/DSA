def minimumWaitingTime(queries):
    # Write your code here.
    queries.sort() # O(nlogn)
    sum_ = 0
    for i in range(1, len(queries)):
        sum_ += sum(queries[:i])
    return sum_


queries = [3, 2, 1, 2, 6]
minimumWaitingTime(queries)