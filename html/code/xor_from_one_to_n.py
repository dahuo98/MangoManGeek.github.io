def getXORFromOne(n):
    # fixed pattern for 1^2^3^...^n
    remainder = n % 4
    if remainder == 0:
        return n
    elif remainder == 1:
        return 1
    elif remainder == 2:
        return n+1
    else:
        return 0