import ipdb

def spiral(n):
    i = 0
    j = 0
    next_num = 1
    result = [[None for x in range(n)] for y in range(n)]
    while next_num <= n**2:
        while j < n and not result[i][j]:
            result[i][j] = next_num 
            j += 1
            next_num += 1
        j -= 1
        i += 1
        while i < n and not result[i][j]:
            result[i][j] = next_num 
            i += 1
            next_num += 1
        i -= 1
        j -= 1 
        print(i, j)
        while j >= 0 and not result[i][j]:
            result[i][j] = next_num 
            j -= 1
            next_num += 1
        j += 1
        i -= 1
        while i >= 0 and not result[i][j]:
            result[i][j] = next_num
            i -= 1
            next_num += 1
        j += 1
        i += 1
    return result


print(spiral(4))