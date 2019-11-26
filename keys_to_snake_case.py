def convert_to_snake(string):
    result = ""

    for i, c in enumerate(string):
        if c.isupper():
            snake = "_"
            if i == 0:
                snake = ""
            result += f'{snake}{c.lower()}'
        else:
            result += c
    return result


print(convert_to_snake("someListIsGood"))


def convert_obj(obj):
    if isinstance(obj, list):
        return list(map(convert_obj, obj))
    elif isinstance(obj, dict):
        for k, v in list(obj.items()):
            key = convert_to_snake(k)
            value = convert_obj(v)
            del obj[k]
            obj[key] = value
        return obj
    else:
        return obj


import pprint

pp = pprint.PrettyPrinter(indent=4)

# print('\nTesting Scalar')
# d = {'someList': 1}
# print(convert_obj(d))

# print('\nTesting List')
# d = {'someList': [1, 2, 3]}
# print(convert_obj(d))

# # Testing Maps
# print('\nTesting Maps')
# d = {'someList': {'anotherList': 1}}
# print(convert_obj(d))

# print('\nTesting Maps in List')
# d = {'someList': [{'secondList': 1}, {'thirdList': 2}]}
# print(convert_obj(d))

# print('\nTesting multiple keys')
# d = {'someList': {'secondList': 1}, 'someList2': {'thirdList': 2}}
# print(convert_obj(d))

# d = {
#     'someList': {
#         'secondList': 1
#     },
#     'someList2': {
#         'thirdList': 2
#     },
#     'AnotherCamel': 1
# }
# print(convert_obj(d))

# print('\nTesting Empty')

d = {
    'someInt': 11,
    'someNestedDict': {
        'someOtherInt': 12,
        'anotherDict': {
            'aM': 'lo'
        }
    },
    'someList': [13, 14, {
        'someKey': 2
    }],
    'someString': "aaak"
}

d = {
    'firstTier1': 1,
    'firstTier2': {
        'secondTier1': 12,
        'secondTier2': {
            'ThirdTier1': 'lo'
        }
    },
    'firstTier3': [13, 14, {
        'secondTier3': 2
    }],
    'firstTier4': 'aaak'
}

pp.pprint(convert_obj(d))
