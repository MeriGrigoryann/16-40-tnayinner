# 149

# try:
#     file = open('filik.txt', 'r')
#     for i in range(10):
#         line = file.readline()
#         if not line:
#             break
#         print(line.strip())
#     file.close()
# except FileNotFoundError:
#     print(f"{'filik.txt'}-y goyutyun chuni։")




#  150


# try:
#     file = open('filik.txt', 'r')
#     lines = file.readlines()
#     file.close()
    
#     last_10 = lines[-10:]  
#     for line in last_10:
#         print(line.strip())
# except FileNotFoundError:
#     print(f"{'filik.txt'}-y goyutyun chuni։")





# 151

# filenames = input("Nermuceq fayleri anunnery iraric arandznacnelov bacatanishov: ").split()

# if not filenames:
#     print("Mutqagreq fayli anun։")
# else:
#     for i in filenames:
#         try:
#             file = open(i, 'r')
#             print(f"--- {i} ---")
#             for j in file:
#                 print(j.strip())
#             file.close()
#         except FileNotFoundError:
#             print(f"{i} fayly chi gtnvel")





# 152

# naxnakan = input ( 'Nermuceq file-y vortexic petq e vercneq infon  ')
# verjnakan = input ('Nermuceq verjnakan(nor stexcvox) file-i anuny  ')

# file1 = open(naxnakan, 'r')
# file2 = open (verjnakan , 'w')


# num = 1
# for line in file1:
#     nor_tox = str(num) + ':' + line

#     file2.write(nor_tox)
#     num += 1



# 153

# filename = input("Enter file name: ")

# try:
#     file = open(filename, 'r')
#     kard = file.read()
#     file.close()

#     words = kard.split() 
#     max_len = 0
#     longest_words = []

#     for i in words:
#         length = len(i)
#         if length > max_len:
#             max_len = length
#             longest_words = [i]
#         elif length == max_len:
#             longest_words.append(i)

#     print("Length", max_len)
#     print("words-->", ', '.join(longest_words))

# except FileNotFoundError:
#     print(f"{filename} chka։")




#  154



# 155
# sxal a ashxatum , bayc chem jnjum 
# filename = input("Enter file name: ")

# try:
#     file = open(filename, 'r')
#     text = file.read()
#     file.close()

#     words = []
#     for char in text:
#         if char.isalpha() or char == ' ': 
#             words.append(char.lower())  
#         else:
#             words.append(" ")

#     words = ''.join(words).split()  
#     hachax = {}

#     for word in words:
#         if word in hachax:
#             hachax[word] += 1
#         else:
#             hachax[word] = 1

#     maxx = max(hachax.values())
#     barer = []
#     for word, count in hachax.items():
#         if count == maxx:
#             barer.append(word)



#     print(f"amenashat handipac bar: {', '.join(barer)}")
#     print(f"Hachaxakanutyun {maxx}")

# except FileNotFoundError:
#     print(f"{filename} chka ")







# 156

# summ = 0

# while True:
#     user = input("Enter number: ")

#     if user == "":
#         break

#     try:
#         number = float(user) 
#         summ += number
#         print(f"Sum will be {summ}")
#     except ValueError:
#         print("Enter numbers please :")





# 158



# skzbnakan = input ('Nermuceq ayn file-y vori het ashxatanq eq cankanum katarel  ')
# verjnakan = input ('Inch anun eq cankanum vor verjnakan file-y unena ?  ')

# try:

#     file1 = open (skzbnakan, 'r')
#     file2 = open ( verjnakan, 'w')


#     for line in file1:
#         if '#' in line:
#             line = line[:line.index('#')]

#             line += '\n'

        
#         file2.write(line)

#     file1.close()
#     file2.close()
#     print("done ")

# except:
#     print('file-y chi gtnvel')


# 159 

# import random

# filename = input ('Nermuceq ayn file-i anuny, vori het uzum eq ashxateq ')


# try:

#     file = open (filename, 'r')
#     words = []

#     for word in file:
#         word = word.strip()

#         if len(word) >= 3:
#             words.append(word)

    
#     file.close()

#     if len(words) < 2:
#         print ( 'file-um chkan bavarar barer ')

#     else: 
#         count = 0

#         while count < 1000:
#             word1 = random.choice(words)
#             word2 = random.choice(words)

#             password = word1.capitalize() + word2.capitalize()


#             if len(password) >= 8 and len(password) <=10:
#                 print (f'Your password is {password}')
#                 break

#             count += 1

#         else:
#             print('Length of password is not right')

# except:
#     print(f'File not found')




# 161 sa yndhanrapes chem haskanum 
# 162 xndiry haskanum em bayc chhem karum grem 
# 163, 164, 165, 166   anunneri xndir



# 172

# filename = input("Enter files name: ")


# try:
#     with open(filename, 'r') as file:
#         for line in file:
#             words = line.split()
            
#             for word in words:
#                 word_lower = word.lower() 
#                 if ('a' in word_lower and
#                     'e' in word_lower and
#                     'i' in word_lower and
#                     'o' in word_lower and
#                     'u' in word_lower and
#                     'y' in word_lower):
#                         print(f"Գտնվեց բառ՝ {word}")


# except:
#     print("We couldn't find a file, try another way: ")

