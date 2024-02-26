def binary_search(haystack, needle):
    l, h = 0, len(haystack)  # an Inclusive upper bound
    # if h = len(haystack) - 1 which would make it exclusive

    while l < h:  # inclusive = l < h, exclusive l <= h
        m = l + (h - l) // 2

        if haystack[m] == needle:
            return True

        if needle > haystack[m]:
            l = m + 1
        else:
            h = m  # exclusive h = m - 1

    return False


""" 
    - m should always be found using the formula l + (h - l) // 2 to avoid introducing bug to finding the mid point
    - [l, h) low should be inclusive and high should be exclusive (cause when shifting to the high side you don't need to check the middle element)

"""

print(binary_search([1, 3, 4, 69, 71, 81,
      90, 99, 420, 1337, 69420], 69) == True)
print(binary_search([1, 3, 4, 69, 71, 81,
      90, 99, 420, 1337, 69420], 666) == False)
