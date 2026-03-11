dict1 = {"a": 10, "b": 20}
dict2 = {"b": 5, "c": 30}

def merge_dicts(dict1, dict2):
    result = dict1.copy()

    for key, value in dict2.items():
        result[key] = result.get(key, 0) + value

    return result
print(merge_dicts(dict1, dict2))

