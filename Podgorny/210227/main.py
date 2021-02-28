def min_of_list(arr):
    s = None
    i = 0
    l = len(arr)

    while i < l:
        if s is None:
            s = arr[i]
        else:
            s = min(s, arr[i])
        i = i + 1

    return s
