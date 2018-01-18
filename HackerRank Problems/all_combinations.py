from copy import copy


def combinations(target, data):
    for i in range(len(data)):
        new_target = copy.copy(target)
        new_target.append(data[i])
        new_data = data[i+1:]
        print(new_target)
        combinations(new_target, new_data)


target = []
data = ['a','b','c','d']
print(combinations(target, data))
