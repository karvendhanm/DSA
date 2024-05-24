# minimum waiting time 1st iteration
# def minimumWaitingTime(queries):
#     # Write your code here.
#     queries.sort() # O(nlogn)
#     sum_ = 0
#     for i in range(1, len(queries)):
#         sum_ += sum(queries[:i])
#     return sum_


# minimum waiting time 2nd iteration
def minimumWaitingTime(queries):
    queries.sort()
    total_waiting_time = 0
    for _idx, query in enumerate(queries):
        queries_left = len(queries) - 1 - _idx
        total_waiting_time += query * queries_left
    return total_waiting_time

queries = [3, 2, 1, 2, 6]
print(minimumWaitingTime(queries))