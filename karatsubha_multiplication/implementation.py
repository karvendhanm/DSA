def karatsubha_multiplication(left_num, right_num):
    '''

    :param left_num:
    :param right_num:
    :return:
    '''

    # both the arguments to the function needs to be an integer
    if not isinstance(left_num, int) or  not isinstance(right_num, int):
        return "two integers are expected as arguments for this function"

    left_num_length = len(str(left_num))
    right_num_length = len(str(right_num))

    # need to identify the number of zeroes trailing the numbers
    left_num_stripped = int(str(left_num).rstrip('0'))
    left_num_stripped_length = len(str(left_num_stripped))
    left_len_diff = left_num_length - left_num_stripped_length

    right_num_stripped = int(str(right_num).rstrip('0'))
    right_num_stripped_length = len(str(right_num_stripped))
    right_len_diff = right_num_length - right_num_stripped_length

    # base case
    if left_num_stripped_length == 1 and right_num_stripped_length == 1:
        _product = left_num_stripped * right_num_stripped
        len_product = len(str(_product))
        val = int(str(_product).ljust(len_product + left_len_diff + right_len_diff, '0'))
        return val



karatsubha_multiplication(5000, 4000)

