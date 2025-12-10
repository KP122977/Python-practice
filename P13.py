# Implement a function that removes a key-value pair from a dictionary

def remove_key(d, key):
    return {k: v for k, v in d.items() if k != key}

print(remove_key({'a': 1, 'b': 2, 'c': 3}, 'b'))
