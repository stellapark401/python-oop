test_dict = dict()
for i in range(5):
    test_dict[i] = (i + 1, i + 5)
for k, v in test_dict.items():
    print(f'{k}: {v[0]}, {v[1]}')
