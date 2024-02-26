def linear_search(haystack, needle):
    for hay in haystack:
        if hay == needle:
            return True
    return False

    # You can use the (in) key word search for an ele in py
    if needle in haystack:
        return True


print(linear_search([1, 3, 4, 69, 71, 81,
      90, 99, 420, 1337, 69420], 69) == True)
print(linear_search([1, 3, 4, 69, 71, 81,
      90, 99, 420, 1337, 69420], 666) == False)
