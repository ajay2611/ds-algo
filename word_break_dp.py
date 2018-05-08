def check(needle):
    cache = [False for _ in range(len(needle) + 1)]
    cache[0] = True  # Empty string case

    for i in range(1, len(needle) + 1):
        for j in range(i):

            # if 0 to j - 1 substring is valid,
            # then check if j to i is valid or not,
            # if it is valid, mark 0 to i as valid
            if cache[j] == True and needle[j:i] in word_list:
                cache[i] = True
    return cache[len(needle)]

if __name__ == '__main__':
    word_list = {
        "i", "like", "sam", "sung", "samsung", "mobile", "ice", "cream",
        "icecream", "man", "go", "mango"
    }

    print(check("ilike"))
    print(check("ilikesamsung"))
    print(check("iiiiii"))
    print(check("samsungandmango"))
    print(check("samsungandmangok"))
