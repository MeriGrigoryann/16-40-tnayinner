# 87 88 91 92 94 98 99 101


# 87
# def araqum(items):
#     if items == 1:
#         return 10.95
#     elif  items > 1:
#         return 10.95 + (items - 1) * 2.95
    
# items = int (input ('Enter count of items: '))
# print (f'{items} apranqi araqman hamar duq petq e vchareq {araqum(items)}$ gumar')

# 88
# def mijin (a, b, c):
#     return (a + b + c)/3

# a = int (input ('Enter number: '))
# b = int (input ('Enter number: '))
# c = int (input ('Enter number: '))

# print (a , b, c)
# print (f'a  , b , c tveri mijiny klini ` {(mijin (a, b, c))}')

# 91 ( sa chi stacvel , videon nwayel em haskacel em )
# def grig_calendar(y, m, d):
#     count = 0
#     m_lst = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
#         m_lst[1] = 29
#     for i in range(m - 1):
#         count += m_lst[i]
#     count += d
#     return count
# print(grig_calendar(2025, 4, 2))

# 92
# def date(y, count):
#     m_lst = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
#         m_lst[1] = 29 
#     month = 0
    
#     while count > m_lst[month]:
#         count -= m_lst[month]
#         month += 1
#     return month + 1, count

# print(date(2025, 92)) 

# 94
# def erankyun (a, b, c):
#     if a + b > c or b + c > a or c + a > b:
#         return f'kareli e gcel erankyun {a , b , c } erkarutyamb koxmerov '
#     else: 
#         return f'{a, b, c} koxmerov erankyun gcel chi kareli'
    
# a = int(input ("Nermuceq erankyan koxmy: "))
# b = int(input ("Nermuceq erankyan koxmy: "))
# c = int(input ("Nermuceq erankyan koxmy: "))

# print (erankyun ( a,b,c))

# 98
# def parz (a):
#     if a <= 1:
#         return False
    
#     for i in range (2, int (a ** 0.5) + 1):
#         if a % i == 0:
#             return False
#     else:
#         return True

        
# a = int (input ('enter number: '))        
# print (parz (a))

# 99 

# def parz (a):
#     if a <= 1:
#         return False
    
#     for i in range (2, int (a ** 0.5) + 1):
#         if a % i == 0:
#             return False
#     else:
#         return True
   
        

# def nextPrime (tiv):
#     next = tiv + 1

#     while not parz (next):
#         next += 1
#         return next
  
        

# tiv = int (input ("enter number: "))

# print (nextPrime(tiv))


# 101 ( es xndirn el chi stacvel , nayel em , haskacel em )


