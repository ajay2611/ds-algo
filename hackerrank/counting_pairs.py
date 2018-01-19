# Complete the function below.

from collections import defaultdict


def countPairs(numbers, k):
    count = 0
    hash_dict = defaultdict(int)
    for n in numbers:
        hash_dict[n] = 1

    print(hash_dict)

    for n in numbers:
        if hash_dict[n+k]:
            count += 1
        hash_dict[n+k] = 0
        print(hash_dict)
    
    return count
    
    
print(countPairs([1,2,3,4,5,6], 2))


