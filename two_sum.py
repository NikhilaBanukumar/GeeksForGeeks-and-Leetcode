def twoSum(numbers, target):
    map = {}
    for i in range(len(numbers)):
        if numbers[i] not in map:
            map[numbers[i]] = [i + 1]
        else:
            if len(map[numbers[i]]) < 2:
                map[numbers[i]].append(i + 1)
    for i in map:
        diff = target - i
        if diff == i and len(map[i]) == 2:
            return [map[i][0], map[i][1]]
        elif diff > i and diff in map:
            return [map[i][0], map[diff][0]]
    return None

print(twoSum([-1,0],-1))