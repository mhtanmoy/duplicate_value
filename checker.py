my_list = ['a','b','c','c','a','b','e','a',1,2,2,4]

dubli_dict = dict()
dubli = []
for item in my_list:
    if my_list.count(item) > 1:
        if dubli.count(item) < 1:
            count = my_list.count(item)
            dubli.append(item)
            # print(f"{item} = {count}")
            dubli_dict.update({item:count})
for key, value in dubli_dict.items():
    print(f"{key} = {value}")
