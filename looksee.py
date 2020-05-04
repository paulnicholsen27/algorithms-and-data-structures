


def looksee(n, results=[]):
    # 1
    # 11 
    # 21
    # 1211
    # 111221
    n = list(str(n))
    if len(n) > 100 or len(n) < 1: 
        return results
    # accumulator = 0
    # value = None
    # result = ""
    # for digit in list(n):
    #     if digit == value:
    #         accumulator += 1
    #     else:
    #         if value:
    #             result += str(accumulator) 
    #             result += str(value)
    #         print(digit, result)
    #         accumulator = 0
    #         value = 1
    # accumulator = 0
    # value = n[0] # 1
    # next_number = n[0] # 1
    # result = ""
    # while len(n) > 0:
    #     if next_number == value:
    #         accumulator += 1
    #         n.pop(0)
    #         try:
    #             next_number = n[0]
    #         except IndexError:
    #             break
    #     else:
    #         result += str(accumulator)
    #         result += str(value)
    #         accumulator = 0
    #         value = next_number
    # result += str(accumulator)
    # result += str(value)
    # results.append(result)
    sorted_by_value = []
    current = n.pop(0)
    for digit in n:
        if digit == current[0]:
            current += digit
        else:
            sorted_by_value.append(current)
            current = digit

    # ['11', '2', '1']
    sorted_by_value.append(current)
    print sorted_by_value
    result = "".join(["{}{}".format(len(digit), digit) for digit in sorted_by_value])
    results.append(result)

    return looksee(result, results)

def print_looksee(n):
    for result in looksee(n, [n]):
        print(result)

print_looksee(3)

