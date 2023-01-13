def karatsubha_multiplication(left_num, right_num):
    '''

    :param left_num:
    :param right_num:
    :return:
    '''

    left_num_length = len(str(left_num))
    right_num_length = len(str(right_num))

    # base case
    if left_num_length == 1 and right_num_length == 1:
        return left_num_length * right_num_length

