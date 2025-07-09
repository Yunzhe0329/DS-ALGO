def flipped_dict(dict_obj):
    return {value:key for key, value in dict_obj.items()}
my_dict = {'a' : 1, 'b' : 2, 'c' : 3}
print(flipped_dict(my_dict))

# 不使用 items() 走訪dict 只會走訪key
def flipped_dict_without_items(dict_obj):
    return {dict_obj[key] : key for key in dict_obj}
print(flipped_dict_without_items(my_dict))
