# 1
# mydict = {
#     1 : 45 ,
#     2 : 20 ,
#     3 : 91 ,
#     4 : 30
# }

# print (sorted(mydict.values()))

# 2
# dic = {
#     1 : 45 ,
#     2 : 20 ,
#     3 : 91 ,
#     4 : 30
# }

# dic['a'] = 15
# print (dic)

# 3
# dic = {
#     1 : 45 ,
#     2 : 20 ,
#     3 : 91 ,
#     4 : 30
# }

# print (dic.get('T'))

# 4
# dict1 = {'a': 50, 'b': 700}
# dict2 = {'c': 400, 'd': 600}
# dict1.update(dict2)
# print(dict1)

# 5
# s = 1
# t = []
# mydict = {'a': 1,'b': 2,'c': 12}
# t = mydict.values()

# for i in t: 
#     s *= i
# print(s)

# 6 

# dic = {
#     'D': 56,
#     'E': 12,
#     'F': 69, 
#     'C': 45, 
#     'B': 23, 
#     'A': 67
# }

# for i in dic:



# 136 , 137 138 144
# #  136
# my_dict = {
#     'a': 50,
#     'b': 100,
#     'c': 50,
#     'd': 200,
#     'e': 50
# }

# value_to_find = 50

# keys_with_value = []

# for i in my_dict:
#     key = i           
#     value = my_dict[i] 
#     if value == value_to_find:
#         keys_with_value.append(key)

# print(value_to_find , keys_with_value)

# value_to_find = 100
# keys_with_value = [] 

# for i in my_dict:
#     key = i
#     value = my_dict[i]
    
#     if value == value_to_find:
#         keys_with_value.append(key)

# print(value_to_find , keys_with_value)

# value_to_find = 300
# keys_with_value = []  

# for i in my_dict:
#     key = i
#     value = my_dict[i]
#     if value == value_to_find:
#         keys_with_value.append(key)

# print(value_to_find , keys_with_value)

#138
# dic = {

# 1 : '. , ? ! :',
# 2 : 'A B C',
# 3 : 'D E F',
# 4 : 'G H I',
# 5 : 'J K L',
# 6 : 'M N O',
# 7 : 'P Q R S',
# 8 : 'T U V',
# 9 : 'W X Y Z',
# 0 : ' '
# }


# 144
# text1 = input ('enter text: ').lower()
# text2 = input ("enter text: ").lower()
# txt1 = []
# txt2 = []
# for i in text1:
#     if i.isalnum():
#         txt1.append(i)
# for j in text2:
#     if j.isalnum():
#         txt2.append(j)


# print({i:txt1.count(i) for i in txt1} == {i:txt2.count(i) for i in txt2})