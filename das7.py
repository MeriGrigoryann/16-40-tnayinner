# Number   1

# for i in range (15 , 180):
#     if i % 15 == 0 and i % 12 == 0:
#         print (i)
#         break


# Odd or Even  2 

# zuyg = 0
# kent = 0
# for i in range (1, 101):
#     if i % 2 == 0:
#         zuyg += 1
#     else:
#         kent += 1
# print ("(1,100) mijakayqum ka ", zuyg, "hat zuyg tiv")
# print ("(1,100) mijakayqum ka ", kent , "hat kent tiv")


# ______________________________________________sxal_______________________________________________________________________________
# # # Fibonacci 3


# # number = 0
# # for i in range (0, 40):
# #     # while True:
# #     # # for i in range (0, 40):

# #     #     if i + (i+1) < 40:
# #     number += int ((i  ) + (i-1))
# #     print (number)
# #             # i += 1
    

# i = 0
# j=0
# while i+1 < 40:
#     print (i,i+1)
#     i=j
#     for j in range (0 , 40):

#     # print (i+1)
#     # i+=1

# _____________________________________________________________________________________________________________________________________


# Numbers and letters 4

# letter = 0
# number = 0
# symbol = 0
# string = "python  3.9"

# for char in string:
#     if char.isalpha ():
#         letter += 1
#     elif char.isdigit ():
#         number += 1
#     else:
#         symbol += 1

# print ("There are ", letter, "letters")
# print ("There are ", number, "numbers")
# print ("There are ", symbol, "symbols")



# Count 5

# number = 73421
# summ = 0

# while number > 0:
#     summ += number % 10 
#     number = number // 10  

# print ("The sum of the digits is: ", summ)



#  Factorial 6

# factorial = 1
# number = int (input ("input the number: "))
# for i in range (1 , number+1 ):
#    factorial *= i 
# print (factorial)



#  Check 7

# tariq = int ( input ( "input your age: "))
# ser = input ( "you are male or female? ").lower()
# if tariq >=18 and tariq <=20 and ser == "male":
#     print ( "You are approved: ")
# else: 
#     print ("You are not approved! ")

# ---------------------------------------------------------next slide---------------------------------------------------

#  3 astichanixndir 

# number = int (input ( "nermucel tivy :  "  ))
# for i in range (1, number+1):
#     print (i, "tvi xoranardy klini : " ,i ** 3)


#  Robot

# name = input ( "enter your name: ")
# partq = int (input ( "nermucel partqi chapy: "))
# while True:
#     vcharum = int (input ( "vorqan gumar eq patrast vcharel? "))
#     if vcharum >= partq:
#         print (name, " Duq marel eq dzer partq, shnorhakalutyun ")
#         break
#     else:
#         print (name, "Dzer arajarkac gumary bavarar che parqn amboxjovin marelu hamar, ayl gumar arajarkeq ")



#  tvanshanneri hashvark

# number = input ( " nermucel tiivy : ")
# count = 0
# for char in number:
#     if number.isdigit():
#         count += 1
# print (number , "tivy uni " , count, "hat tvanshan")


# drakan u bacasakan tveri qanak


# drakan = 0
# bacasakan = 0
# while True:
#     tiv = int ( input ("nermucel tiv: "))
#     if tiv == 0:
#         break
#     elif tiv > 0:
#         drakan += 1
#     elif tiv < 0:
#         bacasakan += 1
# print ("drakan tveri qanak: ", drakan)
# print ("bacasakan tveri qanak: ", bacasakan)



#  Maxim to dolist 

# count = 0
# for i in range (1,8):
#     print ("jam ", i , "-rd, qani handznararutyun eq duq katarel ?")
#     harcum = int (input ("mutqagreq dzer katarac handznararutyunneri qanaky: ")) 
#     count += harcum
#     zang = int ( input ( " patasxanel zangin ?          (ayo=1,voch=0) -   "))
# print ("orva avartin duq katareciq ", count, "handznararutyun")
# if zang == 1:
#         print (" petq e xanut gnal")


# բանկ

# x = int (input ("greq dzer nerdrman gumary: "))  
# p = int (input ("amen tari qani tokov e avelanalu: "))
# # sa aveli mec tiv a qan nerdrumy 
# y = int (input("greq ayn gumary vorin cankanum eq hasnel: "))
# tariner = 0
# while x<y:
#     x += x * p/100
#     tariner += 1
# print (tariner, "tari heto duq kunenaq ", y, "dram gumar, bankum")



#  xax - guishakir tivy 


# import random

# number = random.randint(0,100)
# while True:
#     gushakel = int (input ("nermucir tivy: "))
#     if gushakel == number:
#         print ("shnorhavorum enq duq gushakel eq tivy")
#         break
#     elif gushakel > number:
#         print (" pordzeq aveli poqr tiv nermucel")    
#     else:
#         print (" pordzeq aveli mec tiv gushakel ")    


a = 0
res = "0, 1, 1"
while True:
    a = int(res[-1]) + int(res[-4])
    
    print(a)
    if int(res[-1]) >= 40:
        break
print(res)

# res = "0, 1, 1"

# a = "b"

# print(res + a)