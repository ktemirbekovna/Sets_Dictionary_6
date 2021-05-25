nok_set = {"add", "update", "intersection", "remove", 
     "difference", "intersection-update", "clear", "discard", "pop"}
nok_dict = {"clear", "get", "keys", "pop","popitem", "values", "items", "update"}
x = nok_set.intersection(nok_dict)
print(x)