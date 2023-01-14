def karatsubha_multiplication(left_num, right_num):
    '''

    :param left_num:
    :param right_num:
    :return:
    '''

    # both the arguments to the function needs to be an integer
    if not isinstance(left_num, int) or  not isinstance(right_num, int):
        return "two integers are expected as arguments for this function"

    if not left_num > 0 and right_num > 0:
        return "two integers must be greater than zero"

    _lst = [left_num, right_num]
    _lst.sort()
    left_num, right_num = _lst[0], _lst[1]

    left_num_length = len(str(left_num))
    right_num_length = len(str(right_num))

    # identify the number of zeroes trailing the numbers
    if left_num != 0:
        left_num_stripped = int(str(left_num).rstrip('0'))
    else:
        left_num_stripped = 0

    left_num_stripped_length = len(str(left_num_stripped))
    left_len_diff = left_num_length - left_num_stripped_length

    if right_num != 0:
        right_num_stripped = int(str(right_num).rstrip('0'))
    else:
        right_num_stripped = 0

    right_num_stripped_length = len(str(right_num_stripped))
    right_len_diff = right_num_length - right_num_stripped_length

    # base case
    if left_num_stripped_length == 1 and right_num_stripped_length == 1:
        _product = left_num_stripped * right_num_stripped
        len_product = len(str(_product))
        # this step is necessary as only single step multiplication is allowed
        val = int(str(_product).ljust(len_product + left_len_diff + right_len_diff, '0'))
        return val

    if left_num_length == 1:
        _right_pow = right_num_length // 2
        right_quotient = right_num // (10 ** _right_pow)
        right_remainder = right_num % (10 ** _right_pow)

        first_part = 10 ** _right_pow * karatsubha_multiplication(left_num, right_quotient)
        last_part = karatsubha_multiplication(left_num, right_remainder)

        return first_part + last_part

    else:
        _left_pow = left_num_length // 2
        left_quotient = left_num // (10 ** _left_pow)
        left_remainder = left_num % (10 ** _left_pow)

        _right_pow = right_num_length // 2
        right_quotient = right_num // (10 ** _right_pow)
        right_remainder = right_num % (10 ** _right_pow)

        first_part = (10 ** (_left_pow + _right_pow)) * karatsubha_multiplication(left_quotient, right_quotient)
        second_part = (10 ** _left_pow) * karatsubha_multiplication(left_quotient, right_remainder)
        third_part = (10 ** _right_pow) * karatsubha_multiplication(left_remainder, right_quotient)
        last_part = karatsubha_multiplication(left_remainder, right_remainder)

        return first_part + second_part + third_part + last_part



