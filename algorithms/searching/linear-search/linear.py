def linearSearch(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1 # target not found