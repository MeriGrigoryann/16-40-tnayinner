# ----------------------------------LIST SLIDE--------------------------------------
# ----------------------------------------------------------------------------------


# 2
# listik = [5 , 6 , 1 , 2 , 9, 44]
# res = 1
# for i in listik:
#     res *= i
# print (res)
# ----------------------------------------------------------------------------------
# 3
# listik = ['barev', 'dzez', 'inch', 'e', 'dzer', 'anunn', 'u', 'azganuny']
# erkar = ""
# for i in listik:
#     if len(i) > len(erkar):
#         erkar = i
# print (erkar)
# ----------------------------------------------------------------------------------
# 4
# list1 = ['barev', 'dzez', 'inch', 'e', 'dzer', 'anunn', 'u', 'azganuny']
# list2 = ['voxjuyn', 'im', 'anuny', 'Hayk', 'e']
# for i in list1:
#     for j in list2:
#         if i == j:
#             print (True)


# ----------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------
# ----------------------------------LIST SLIDE 2------------------------------------


# 1 New list
# mylist = [ 66 , "mard", True, 66, "T"]
# print (mylist)
# ----------------------------------------------------------------------------------
# 2 Mac
# listt = ['HP ', 'ASUS', 'DELL', 'MAC', 'LENOVO']
# for i in listt:
#     if i == 'MAC':
#         print (True)
# ----------------------------------------------------------------------------------
# 3 Password
# while True:
#     charr = 0
#     tiv = 0
#     password = input ("enter your password: ")
#     if len(password) < 8 or password[0].islower() or password.isalnum():
#             print ("Your password is nor strong")
#     else:
#         for i in password:
#             if i.isdigit():
#                 tiv += 1
#             elif i.isalpha():
#                 continue
#             else:
#                 charr +=1

#     if charr >= 2 and tiv >= 2:
#         print ("Your password is strong")
#         break
#     else:
#             print("Your password is not strong")
# ----------------------------------------------------------------------------------    # 
# 4 Link Finder
# link = input ("Enter link: ")
# hng = link.split("=")
# print (hng[1])
# ----------------------------------------------------------------------------------    # 
# 5 Sign in
# word = input("Enter a word: ")
# word = word.upper()
# if word == word[::-1]:
#     print("Open")
# else:
#     print("Trash")
# ----------------------------------------------------------------------------------    # 
# 6 String - to - list
# text = input ("enter text: ")
# print (list (text))
# ----------------------------------------------------------------------------------    # 
# 7 Even Numbers
# tver = input ("Enter numbers: ")
# numbers = tver.split(" ")
# zuyg = [ i for i in numbers if int (i) % 2 == 0]
# print ("Even numbers are: ", " ".join(zuyg))
# ----------------------------------------------------------------------------------    # 
# 8 Odd
# mylist = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]
# print ("the new list is ", ([i for i in mylist if i % 2 == 1]))
# ----------------------------------------------------------------------------------    # 
# 9 Secret Santa
#  harc 
# ----------------------------------------------------------------------------------    # 
# 10 Duplicate 
# eli harc a , bayc senc em mtacum 
# list1 = [1 , 2 , 3 , 4 , 5 , 1 , 3] 
# for i in list1:
#     if list[0] == list[i]:
#         print (list1.remove(i))
#         #  kam print (list1.pop(i))
#     print (list1) 