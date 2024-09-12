def flatten_tuple(t):
    
    flattened = []
    def flatten(item):
        if isinstance(item, tuple):
            for i in item:
                flatten(i)
        else:
            flattened.append(item)

    flatten(t)
    
    return tuple(flattened)
example_tuple = (1, (2, 3), (4, 5, 6))
flattened_tuple = flatten_tuple(example_tuple)
print(flattened_tuple) 
