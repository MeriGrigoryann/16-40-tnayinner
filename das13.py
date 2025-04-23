# dic = {
#     'Hayk' : 10, 
#     'Ani' : 5,
#     'Anahit' : 4, 
#     'Karen' : 7, 
#     'Laura' : 9, 
#     'Mane' : 6, 
#     'Roza' : 10,
#     'Vardges' : 3,
#     'Sima' : 7,
#     'Silva' : 10
# }
# print (dic)


# -----
# dic = {
#     'Hayk' : 10, 
#     'Ani' : 5,
#     'Anahit' : 4, 
#     'Karen' : 7, 
#     'Laura' : 9, 
#     'Mane' : 6, 
#     'Roza' : 10,
#     'Vardges' : 3,
#     'Sima' : 7,
#     'Silva' : 10
# }
# avr = 0
# summ = 0
# for i in dic:
#     summ += dic[i]
# avr = summ / len(dic)
# print (avr)


# ----
# dic = {
#     'Hayk' : 10, 
#     'Ani' : 5,
#     'Anahit' : 4, 
#     'Karen' : 7, 
#     'Laura' : 9, 
#     'Mane' : 6, 
#     'Roza' : 10,
#     'Vardges' : 3,
#     'Sima' : 7,
#     'Silva' : 10
# }
# lav=[]
# vat=[]
# for i in dic:
#     if dic[i] >= 7:
#         lav.append(i)
#     else:
#         vat.append(i)
# print(f'lav sovorox usanonern en` {lav}')
# print (f'vat sovorox usanoxnern en` {vat}')

# ----
# dic = {
#     'Hayk' : 10, 
#     'Ani' : 5,
#     'Anahit' : 4, 
#     'Karen' : 7, 
#     'Laura' : 9, 
#     'Mane' : 6, 
#     'Roza' : 10,
#     'Vardges' : 3,
#     'Sima' : 7,
#     'Silva' : 10
# }
# good = []
# for i in dic:
#     if dic[i] >= 5:
#         good.append(i)
# print(f'good students are: {good}')

# ----
# dic = {
#     'Hayk' : 10, 
#     'Ani' : 5,
#     'Anahit' : 4, 
#     'Karen' : 7, 
#     'Laura' : 9, 
#     'Mane' : 6, 
#     'Roza' : 10,
#     'Vardges' : 3,
#     'Sima' : 7,
#     'Silva' : 10
# }
# bad = []
# for i in dic:
#     if dic[i] >= 5:
#         bad.append(i)
# print(f' not enough good students are: {bad}')

# ----
# name = input ('Enter name: ')
# dic = {
#     'Hayk' : 10, 
#     'Ani' : 5,
#     'Anahit' : 4, 
#     'Karen' : 7, 
#     'Laura' : 9, 
#     'Mane' : 6, 
#     'Roza' : 10,
#     'Vardges' : 3,
#     'Sima' : 7,
#     'Silva' : 10
# }

# for i in dic:
#     if name in i:
#         print (i , dic[i])


# ----
# s = 'a,2,b,5,c,8,a,4,e,11'

# list(s)
# y = s.split(",")
# dic = {}
# for i in range (0,len(y),2):
#     tar = y[i]
#     tiv = int(y[i+1])
#     if tar in dic:
#         dic[tar] +=tiv
#     else:
#         dic[tar] = tiv
# print(dic)


# ----
# word = 'exercises'
# list(word)
# dic = {}
# for i in word:
#     if i not in dic:
#         dic[i] = 1
#     else: 
#         dic[i]+=1
# print(dic)


# ----
# new_list = []
# old_list = [{'key1':'value1'},{},{},{'key1':'value1'},{'key2':'value2'}] 
# for i in old_list:   
#     if i not in new_list:
#         new_list.append(i)
# print("old list: " , old_list)
# print("new list: " , new_list)


# ----
gumar = 0
print("bari galust ov e uzum darnal milionater xax ")
harc = input (' patrast eq sksel xaxy ? ').lower()
if harc == "ayo":
    print('PUL 1')

    print('sksum enq xaxy, ev 1 in harcy arje 5000 dram , USHADRUTYUN ')
   
   
    harc1 = print('2 + 2 = ?')
    print ( 'A) 5' , 'B) 10' , 'C) 4 ' , 'D) 0'  )
    patasxan1 = input ('nsheq vor pataxann eq yntrum (A, B, C kam D)  ').upper()



    if patasxan1 == 'C':
        gumar += 5000
        print(f"shnorhavorum em , duq uneq {gumar} dram")

    else:
        print(f'cavum em patasxany sxal er, shnorhakalutyun xaxi hamar, duq vastakel eiq {gumar} dram  ')
        exit()

else:
    print('duq durs eq galis xaxic')
    exit()

print('PUL 2')

print('sharunakum enq xaxy, ev 2rd harcn arje 15000 dram , USHADRUTYUN ')


harc1 = print('vorn e Hayastani mayraqaxaqy ? ')
print ( 'A) Erevan' , 'B) Dvin' , 'C) Kars ' , 'D) Erebuni'  )
patasxan1 = input ('nsheq vor pataxann eq yntrum (A, B, C kam D)  ').upper()
if patasxan1 == 'A':
    gumar += 15000
    print(f"shnorhavorum em , duq uneq {gumar} dram")
else:
    print(f'cavum em patasxany sxal er, shnorhakalutyun xaxi hamar, duq vastakel eiq {gumar} dram  ')
    exit()

print('PUL 3')


print('sharunakum enq xaxy, ev 3rd harcn arje 20000 dram , USHADRUTYUN ')


harc1 = print('ov e stexcel hayoc grery ? ')
print ( 'A) Sahak Partev' , 'B) Mesrop Mashtoc' , 'C) Grigor Lusavorich' , 'D) Komitas'  )
patasxan1 = input ('nsheq vor pataxann eq yntrum (A, B, C kam D)  ').upper()
if patasxan1 == 'B':
    gumar += 20000
    print(f"shnorhavorum em , duq uneq {gumar} dram")
else:
    print(f'cavum em patasxany sxal er, shnorhakalutyun xaxi hamar, duq vastakel eiq {gumar} dram  ')
    exit()



print('PUL 4')


print('sharunakum enq xaxy, ev 4rd harcn arje 50000 dram , USHADRUTYUN ')


harc1 = print(' sharunakeq mitqy` "qani lezu gites aynqan ...." ')
print ( 'A) harust es ' , 'B)mard em' , 'C) xelaci es ' , 'D) mard es '  )
patasxan1 = input ('nsheq vor pataxann eq yntrum (A, B, C kam D)  ').upper()
if patasxan1 == 'D':
    gumar += 50000
    print(f"shnorhavorum em , duq uneq {gumar} dram")
else:
    print(f'cavum em patasxany sxal er, shnorhakalutyun xaxi hamar, duq vastakel eiq {gumar} dram  ')
    exit()



print('PUL 5')


print('sharunakum enq xaxy, ev 5rd harcn arje 100000 dram , USHADRUTYUN ')


harc1 = print(' vorn e ashxarhi amenabardzr lery ? ')
print ( 'A) Kilamanjaro' , 'B) Everest' , 'C) Ararat' , 'D) Alper'  )
patasxan1 = input ('nsheq vor pataxann eq yntrum (A, B, C kam D)  ').upper()
if patasxan1 == 'B':
    gumar += 100000
    print(f"shnorhavorum em , duq uneq {gumar} dram")
else:
    print(f'cavum em patasxany sxal er, shnorhakalutyun xaxi hamar, duq vastakel eiq {gumar} dram  ')
    exit()


print('PUL 6')


print('sharunakum enq xaxy, ev 6rd harcn arje 250000 dram , USHADRUTYUN ')


harc1 = print(' vorn e amenaarajin mayrcamaqy vortex sksvecin arajanal qaxaqner ? ')
print ( 'A) Hyusisayin Amerika' , 'B) Evropa' , 'C) Afrika' , 'D) Asia'  )
patasxan1 = input ('nsheq vor pataxann eq yntrum (A, B, C kam D)  ').upper()
if patasxan1 == 'D':
    gumar += 250000
    print(f"shnorhavorum em , duq uneq {gumar} dram")
else:
    print(f'cavum em patasxany sxal er, shnorhakalutyun xaxi hamar, duq vastakel eiq {gumar} dram  ')
    exit()


print('PUL 7')


print('sharunakum enq xaxy, ev 6rd harcn arje 310000 dram , USHADRUTYUN ')


harc1 = print(' vorn e amenamec ovkianosy ? ')
print ( 'A) Xaxax ' , 'B) Atlantyan' , 'C) Hndkakan' , 'D) Hyusisayin sarucyal'  )
patasxan1 = input ('nsheq vor pataxann eq yntrum (A, B, C kam D)  ').upper()
if patasxan1 == 'A':
    gumar += 310000
    print(f"shnorhavorum em , duq uneq {gumar} dram")
else:
    print(f'cavum em patasxany sxal er, shnorhakalutyun xaxi hamar, duq vastakel eiq {gumar} dram  ')
    exit()

    
print('PUL 8')
print ('sa verjin harcn e, ete chisht patasxaneq kvastakeq 1.000.000 dram , hakarak depqum , kpartveq ')
ayo = input( 'uzum eq sharunakeol xaxy ? ').lower()
if ayo == "ayo":
    print('sharunakum enq xaxy, ev verjin harcy hetevyaln e , USHADRUTYUN ')


    harc1 = print(' ov e haytni "Homerosy" gexarvestakan stexcagorcutyan hexinaky ? ')
    print ( 'A) Homeros ' , 'B) V. Sheqspir' , 'C) Platon' , 'D) Herodotos'  )
    patasxan1 = input ('nsheq vor pataxann eq yntrum (A, B, C kam D)  ').upper()
    if patasxan1 == 'A':
        gumar += 250000
        print(f"shnorhavorum em , duq haxtum eq xaxum ev vastakum {gumar} dram")
    else:
        print(f'cavum em patasxany sxal er, shnorhakalutyun xaxi hamar, duq vastakel eiq {gumar} dram  ')
        exit()
else:
    print(f'shnorhakalutyan masnakcutyan hamar , duq vastakeciq {gumar} dram guumar')
    exit()

