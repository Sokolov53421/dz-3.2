my_list=[1, 839,32,123,46,6]
if len(my_list)>1:
    last_element= my_list.pop()
    my_list.insert(0, last_element)

print(my_list)
