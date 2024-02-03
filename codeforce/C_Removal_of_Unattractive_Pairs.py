n = int(input())

for _ in range(n):
    x = int(input())
    words = [str(x) for x in input()]

    words_hash = {}

    for word in words:
        words_hash[word] = words_hash.get(word, 0) + 1

    max_l = max(words_hash.values())

    if max_l > x // 2:
        print(max_l - (x - max_l))
    else:
        print(x % 2)


'''
    # 1: Using a Hashmap 
        - First step is just to get a freq counter going then am just gonna check if the letter 
        with the highest freq can just be used to pair up the rest of the letter, I can do that by checking 
        if its greater then half of the letters in the string if yes then ill just print out 
        the max freq subtracted by the rest of the letters count ( which is the max freq - the len of the string) 
        but if the max freq is not greater then half of the strings count or equal to it then ill just return the mod 
        of the length with 2 

        Time: O(n)
        Space: O(n)

'''
