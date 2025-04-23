# -------------------------------------------
# ------------------slide 3------------------
# -------------------------------------------
# 1
# text = input ("Enter text: ")
# dzayn = ['e', 'u', 'i', 'o', 'a']
# count = 0
# list(text)
# for i in text:
#     if i in dzayn:
#         count += 1
# print (f'textum dzaynavorneri qanaky {count} e')
# -------------------------------------------
# 2
# n = int(input("greq cucakum arka tveri qanaky: "))
# result = []
# for i in range (n):
#     if i % 2 == 0:
#         result.append(1)
#     else:
#         result.append(i % 5)
# print (result)
# -------------------------------------------
# 3 gpt
# import random
# team1 = [random.uniform(5, 10) for _ in range(20)]
# team2 = [random.uniform(5, 10) for _ in range(20)]
# winners = []
# for i in range(20):
#     if team1[i] > team2[i]:
#         winners.append(team1[i])
#     else:
#         winners.append(team2[i])
# print("tim 1: ", team1)
# print("tim 2: ", team2)
# print("haxtec` ", winners)
# ----------------------------------
# import random
# list1 = [round(random.randint(5, 10) - random.random(), 2) for i in range(10)]
# list2 = [round(random.randint(5, 10) - random.random(), 2) for i in range(10)]
# print([list1[index] if list1[index] > list2[index] else list2[index] for index in range(len(list1))])
# -------------------------------------------
# 4
# text = 'abcdefg'
# list(text)
# print (f'num1: {text[::-1]}')
# print (f'num2: {text}')
# print (f'num3: {text[2:]}')
# print (f'num4: {text[0::2]}')
# print (f'num5: {text[1::2]}')
# print (f'num6: {text[1]}')
# print (f'num7: {text[6]}')
# print (f'num8: {text[3:5]}')
# print (f'num9: {text[5:3:-1]}')
# print (f'num10: {text[-3::]}')
# -------------------------------------------
# 5 
# text = 'hqwehrty'
# index1 = text.index('h')
# index2 = text[::-1].index('h')
# print(text[index1 + 1 : -(index2 + 1)][::-1])

# -------------------------------------------
# 6
# import random
# num = []
# neww = []
# n = int (input ("cucakum ka aysqan tiv :"))
# for i in range (n):
#     tiv = random.randint(0,2)
#     num.append(tiv)
# print ("naxnakan cucaky klini` " , num)
# for j in num:
#     if j != 0:
#         neww.append(j)
# print ("verjnakan cucaky klini", neww)
# -------------------------------------------
# 7
# print([[i, i + 4, i + 8] for i in range(1, 5)])
# -------------------------------------------
# 9
# nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
# result = [item for i in nice_list for j in i for item in j]
# print(result)
# -------------------------------------------
# 10
# text = input('Enter text:  ')
# print(''.join([chr(ord(i) + 3) if i != ' ' else ' ' for i in text]))
# -------------------------------------------



# -------------------------------------------
# ------------------GRQIC--------------------
# -------------------------------------------
#110
# number = []
# while True:
#     num = int (input ("enter number: "))
#     if num == 0:
#         break
#     number.append(num)
# number.sort()
# for i in number:
#     print(i, end = " ")
# -------------------------------------------
# 111
# number = []
# while True:
#     num = int (input ("enter number: "))
#     if num == 0:
#         break
#     number.append(num)
# number.sort(reverse = True)
# for i in number:
#     print(i, end = " ")
# -------------------------------------------
# 113
# listik = []
# while True:
#     text = input ("Enter text: ")
#     if text == " ":
#         break
# if text not in listik:
#     listik.append(text)    

#     for i in listik:
#         print (i)
# -------------------------------------------
# 114
# number = []
# while True:
#     tiv = input("enter number: ")
#     if tiv == " ":
#         break
#     number.append(int(tiv))
# number.sort()
# print(number)
# -------------------------------------------
# # 115
# listik = []
# tiv = int (input ("Enter your number :  "))
# for i in range (1, tiv+1):
#     if tiv % int(i) == 0:
#         listik.append(i) 
# listik.pop()
# print (listik, end = '')
# -------------------------------------------
# 116
# listik = []
# summ = 0
# tiv = int (input ("Enter your number :  "))
# for i in range (1, tiv):
#     if tiv % int(i) == 0:
#         listik.append(i) 
#         summ += i

# if summ == tiv:
#     print (tiv, 'is perfect')
# else:
#     print (tiv, 'is not perfect')
# -------------------------------------------
# 117
# symbols = '!@#$%^&*().:_+?><"'
# text = input ('Enter text: ')
# list(text)
# text = " ".join ([i for i in text if i not in symbols])
# print (text)
# -------------------------------------------
# 118 (listi mej list heto andamnery hertov stugel , bayc chem karum grem)
# -------------------------------------------
# 119
# summ = 0
# count = 0
# numbers = []
# while True:
#     tiv = input ('enter number: ')
#     if tiv == "":
#         break


#     if tiv.isdigit():
#         tiv = int(tiv)
#         numbers.append(tiv)
#         summ += tiv
#         count += 1
 
# if count > 0:
#     averagee = summ / count
#     print("miginy klini ", averagee)

#     poqr = [i for i in numbers if i < averagee]
#     havasar = [i for i in numbers if i == averagee]

# print ("mijinic poqr tvern en` ", poqr)
# print ("mijinin havasar tvern en` ", havasar)
# -------------------------------------------
# 121
# import random 
# numbers = []
# while len(numbers) < 6:
#     num = random.randint(1, 49)
#     if num not in numbers:
#         numbers.append(num)

# numbers.sort()

# print("dzer tvern en: ", numbers)
# -------------------------------------------
# 125
# import random 
# qarter = ['H' , 'D' , 'C', 'S']
# tver = [ '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , 'J' , 'Q' , 'K' , 'A']

# listik =  []

# for i in qarter:
#     for j in tver:
#         listik.append(j + i)

# print ("naxqan xarnely klini ` " , listik)

# n = len(listik)
# for i in range (n):
#     j = random.randint(0, n-1)
#     listik[i] = listik[j]
#     listik[j] = listik[i]

# print ("xarneluc heto klini " , listik)
# -------------------------------------------
# 127
# str = input("nermuceq tver ev iraric arandznacreq bacatanishov: ")

# number = [int(i) for i in str.split()]

# ach = True
# nv = True

# for i in range(len(number) - 1):
#     if number[i] > number[i + 1]:
#         ach = False
#     if number[i] < number[i + 1]:
#         nv = False

# if ach:
#     print("nerkayacvac e achman kargov:")
# elif nv:
#     print("nerkayacvac e nvazman kargov:")
# else:
#     print("voch achum e voch nvazum:")
# -------------------------------------------
# 133