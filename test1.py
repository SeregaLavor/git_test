my_list = [42, 43]
my_dict = {
    'foo': {
        'a': 12,
        'b': (1, 2, 3, 4, my_list)
    },
    'bar': {
        'c': 12,
        'd': {5, 6, 7, 8}
    },
    'moo': {
        'e': 12,
        'f': {'Lol': ['L', 'o', 'l']}
    },
}
for k, v in my_dict.items():
    if k == 'foo':
        print(v)
        for k1, v1 in v.items():
            if k1 == 'b':
                print(v1)
my_list.append(44)
print(my_list)