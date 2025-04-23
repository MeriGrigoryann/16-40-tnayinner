# xndir 1
# slot1 = [[5, 17], [20,31],[40, 45],[51 ,63], [70, 80] ,[93 ,97]]
# slot2 = [[1, 8], [14, 25], [27, 40], [50, 59], [61, 67], [75, 82], [85, 91], [97, 100]]
# duration = 8

# verjnakan = []
# for a in slot1:
#     for b in slot2:
#         start = max(a[0], b[0])
#         end = min(a[1],b[1])
#         if start < end:
#             verjnakan.append([start, end])

# verj = []
# for i in verjnakan:
#     if i[1]-i[0] >= duration:
#         verj.append(i)
# print (f'handipumy karox e kayanal{verj} ynkac jamanakahatvacum)





# xndir 2

# 1 2 5 6 ^^^^^^
# 4 7 
# 4 5 6 
# 7 
# 5 6 

# def func(mylist):
#     if mylist[0] > mylist[1]:
#         return mylist[1:]
#     else:
#         return mylist[:]


# mylist = [4, 7, 1, 2, 5, 6]
# func(mylist)


















# >>>>> sevagir <<<<

# listik = []
# y = [0, 1, 2, 3, 4, 5]
# x = [0, 2, 4, 5, 8, 10]

# for a in y:
#     for b in x:
#         if a <= b:
#             listik.append(a*b)


# print (max(listik))




# gcikner = [[0,2],[2,3], [4,2], [5, 5], [8, 3],[9,2],[10,4]]
# max_y = 0
# count = 0
# for i in gcikner:
#     if i[1] > max_y:
#         max_y = i[1]


# for j in gcikner:
#     if j[1] == max_y:
#         count += 1

# if count == 1:
#     new_max_y = -1

#     for j in gcikner:
#         if j[1] < max_y and j[1] >new_max_y:
#             new_max_y = j[1]

#     res = new_max_y
# else:

#     res = max_y



# print (res)

# makeresner = []
# for x in range(0,11):
#     for y in gcikner:
#         if y[1] < x and x <= 5:
            
#            makeresner.append(x*y)
#         elif





# print (makeresner)



# gcikner = [[0,2], [2,3], [4,2], [5,5], [8,3], [9,2], [10,4]]
# gcikner.sort()

# max_s = 0
# bardzr = 0
# zuyg = ()



# for i in range (len(gcikner)):
#     x1 = gcikner[i][0]
#     y1 = gcikner[i][1]


#     for j in range (i+1, len(gcikner)):
#         x2 = gcikner[j][0]
#         y2 = gcikner[j][1]


#     if x2 > x1:
#         himq = x2 - x1
#     else:
#         himq = x1 - x2


#     if y1 > y2:
#         bardzr = y2
#     else:
#         bardzr = y1


    
#     makeres = bardzr * himq 


#     if makeres > max_s:
#         max_s = makeres

#         zuyg = (x1, x2)


# print (max_s)

# print(zuyg)
# <<<<>>>>>>>>>