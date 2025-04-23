# -------------------------------------------
# ------------------slide 1------------------
# -------------------------------------------
#  1
# n = int (input("enter number: "))
# listt = []
# for i in range (1,n+1):
#     if i % 2 == 1:
#         listt.append (i)
# print (listt)
# -------------------------------------------
# 2
# index = 0
# mylist = ['Артемий', 'Борис', 'Влад', 'Гоша', 'Дима', 'Евгений', 'Женя', 'Захар']
# neww =[]
# neww = mylist[ : : 2]
# print (neww)
# -------------------------------------------
# 3
# mylist = [1, 5, 6, 9, 15, 1, 2, 6]
# for i in range (len(mylist)):
#     if mylist[i] < i:
#         print (mylist[i])
# -------------------------------------------
# 4
# list1 = [3050, 3080, 3090, 3070, 3090, 3060]
# max_value = max(list1)
# list1 = [i for i in list1 if i != max_value]
# print(list1)
# -------------------------------------------
# 5
# films = ['Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']
# sireliner = []
# qanak = int (input ("Qani film eq uzum avelacnel ? "))
# for i in range (qanak):
#     anun = input ("nermuceq dzer sireli filmi anuny: ")
#     if anun  not in films:
#         print(f'neroxutyun {anun} filmy mez mot bacakayum e :( ')
#     else:
#         sireliner.append(anun)
#         print(f'dzer sireli filmern en` {anun}')
# print ("dzer sireli filme en` ")
# for j in sireliner:
#     print (j)
# -------------------------------------------
# 6 ????????
# bar = input ("enter bar: ")
# # list(bar)
# y = list(bar)
# y.pop(0)
# count = 0
# for i in y:
# #     for j in y
#     if bar[0] == i:
#         count+=1
# print (count)
# -------------------------------------------
# 7
# խնդիրը չեմ հասկանում 
# -------------------------------------------
# 8
# lst = input("nermuceq andamnery: ").split()
# lst = [int(x) for x in lst]
# K = int(input("nermuceq qanaky: "))
# N = len(lst)
# K = K % N
# lst = lst[-K:] + lst[:-K]
# print("ardyunqum kstacvi", lst)
# -------------------------------------------
# 9
# word = input("nermucel bary: ")
# if word == word[::-1]:  
#     print(f"{word} bary palindrom e")
# else:
#     print(f"{word}  palindrom che")
# -------------------------------------------
# 10
# list1 = [5, 6, 7, 3, 2, -5, 12]
# list1.sort()
# print(list1)
# -------------------------------------------
# ------------------slide 2------------------
# -------------------------------------------
#  2
# list1 = [160, 164, 162, 165, 170, 169, 171]
# list2 = [162, 164, 167, 175, 165, 178, 166]
# neww = []
# neww = list1 + list2
# neww.sort()
# print(neww)
# -------------------------------------------
# 3
# shop = [['каретка', 1200], ['шатун', 1000], ['седло', 300], ['педаль', 100], ['седло', 1500], ['рама', 12000], ['обод', 2000], ['шатун', 200], ['седло', 2700]]
# qanak = 0
# gin = 0
# anun = input ("nermucel apranqi anuny:      ")
# for i in shop:
#     if i[0] == anun:
#         qanak += 1
#         gin += i[1]

# if qanak > 0:
#     print (f'{anun} y vercvel e {qanak} angam ev yndhanur arjeqy kazmum e {gin}')
# else:
#     print (f'xanutum {anun} apranqy chi gtnvel')
# -------------------------------------------
# 4
# guests = ['Петя', 'Ваня', 'Саша', 'Лиза', 'Катя']
# max_guests = 6
# while True:
#     print (f'ayjm nerka hyurern en` {", ".join(guests)}')
#     gorcoxutyuny = input ("nermuceq ekav kam gnac (kam 'para spat')")       
#     if gorcoxutyuny.lower() =='para spat':
#         print ('para spat')
#         break
#     elif gorcoxutyuny not in guests:
#             if len(guests) < 6:
#                  print (f'{gorcoxutyuny} mnum e gisherelu')
#             else:
#                  print ('neroxutyun bayc gisherakaci texery verjacel en :(')
#     elif gorcoxutyuny in guests:
#          guests.remove(gorcoxutyuny)
#          print(f'{gorcoxutyuny} gnacel e tun')
# -------------------------------------------
# 5
# erger = [
#     ['erg1' , 4.86],
#     ['erg2' , 4.20],
#     ['erg3' , 4.65],
#     ['erg4' , 4.25],
#     ['erg5' , 4.32],
#     ['erg6' , 4.87],
#     ['erg7' , 4.26],
#     ['erg8' , 4.5],
#     ['erg9' , 4.86],
#     ['erg10' , 4.36]

# ]
# qanak = int(input('qani erg eq uzum avelacnel: '))
# for _ in range (qanak):
#     anun = input ('nermucel ergi anuny : ')

# jam = 0
# for i in erger:
#     if i[0] == anun:
#         jam += i[1]
#         break
# print ('yndhanur ergeri tevoxutyuny {jam} rope e')
# -------------------------------------------
# 6
# list1 = int (input (' nermuceq 3 tiv: '))
# list2 = int(input('nermuceq 7 tiv: '))
# list(list1)
# list(list2)
# y = list1+list2
# z = []
# for i in y:
#     if i not in z:
#         z.append(i)
# print (z)
# -------------------------------------------
# # 7 chi linum sa
# hamar = int (input ('nermuceq dzer votqi hamry: '))
# arka = int(input('nermuceq arka hamrnery'))
# list(arka)
# if hamar in arka:
#     print ('xndrem vercreq:')
# elif hamar >= arka:
#     print ('xndrem vercreq:')
# else:
#     print('cavum em menq chunenq ayd hamary')

# for i in arka:
#     if i >= hamar:
#         print ('xndrem vercreq:')
#     else:
#         print('cavum em menq chunenq ayd hamary')
# -------------------------------------------
# 8
# n = int(input("nermuceq xaxacoxneri qanaky: "))
# k = int(input("nermuceq hamary: "))
# people = []
# for i in range(1, n + 1):
#     people.append(i)
# index = 0
# while len(people) > 1:
#     index = (index + k - 1) % len(people)
#     people.pop(index)
# print(f"haxtec: {people[0]}")
# -------------------------------------------
# 9  logikan haskanum em byc chem karum luchem
# tvox = int (input ('enter number: ')) 
# vercnox = int (input ('enter number: ')) 
# qanak = int (input)
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
# 5 harc 
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
# 7 harc
# -------------------------------------------
# 8
# -------------------------------------------
# 9
# nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
# result = [item for i in nice_list for j in i for item in j]
# print(result)
# -------------------------------------------
# 10
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