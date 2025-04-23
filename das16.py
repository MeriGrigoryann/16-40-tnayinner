# 175
# def func(n):
#     if n < 0:
#         return (f'! Please enter positive number ! ')
#     if n == 0:
#         return "0"
#     elif n == 1:
#         return "1"
#     else:
#         return func(n // 2) + str (n % 2)
    
# print (func(15))

# 176
# alphabet = {
#     'A' : ' Alpha'  ,
#     'B' : ' Bravo ',
#     'C' : ' Charlie' ,
#     'D' : ' Delta ',
#     'E' : ' Echo ',
#     'F' : ' Foxtrot ',
#     'G' : ' Golf ',
#     'H' : ' Hotel ',
#     'I' : ' India ',
#     'J' : ' Juliet ',
#     'K' : ' Kilo',
#     'L' : ' Lima',
#     'M' : ' Mike',
#     'N' : ' November',
#     'O' : ' Oscar',
#     'P' : ' Papa',
#     'Q' : ' Quebec',
#     'R' : ' Rome',
#     'S' : 'Sierra',
#     'T' : 'Tango',
#     'U' : 'Uniform',
#     'V' : 'Victor',
#     'W' : 'Whiskey',
#     'X' : 'Xray',
#     'Y' : 'Yankee',
#     'Z' : 'Zulu'
# }
# def nato(text):
#     if len(text) == 0:
#         return ""
#     first = text[0].upper()

#     if first in alphabet:
#         return alphabet[first] + ' ' + nato(text[1:])
    

# print (nato('MARD'))

# 181  ( es karaq chnayeq, sxal a )
#  1, 5, 10, 25

# def func(summa, count = 0):
#     if summa == 1:
#         count = 1
#         return f' anhrajesht e {count} hat {1} $'
#     if summa == 5:
#         count = 1
#         return f' anhrajesht e {count} hat {5} $'
#     if summa == 10:
#         count = 1
#         return f' anhrajesht e {count} hat {10} $'
#     if summa == 25:
#         count = 1
#         return f' anhrajesht e {count} hat {25} $'

    # else:
    #     func(summa - 25)
    #     count+=1
    #     return f' anhrajesht e {count} hat {25} $'



# print (func(40))
# # print (count)



# 182
listik = [ "H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne",
    "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar", "K", "Ca",
    "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn",
    "Ga", "Ge", "As", "Se", "Br", "Kr", "Rb", "Sr", "Y", "Zr",
    "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd", "In", "Sn",
    "Sb", "I", "Te", "Xe", "Cs", "Ba", "La", "Ce", "Pr", "Nd",
    "Pm", "Sm", "Eu", "Gd", "Tb", "Dy", "Ho", "Er", "Tm", "Yb",
    "Lu", "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg",
    "Tl", "Pb", "Bi", "Po", "At", "Rn", "Fr", "Ra", "Ac", "Th",
    "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf", "Es", "Fm",
    "Md", "No", "Lr", "Rf", "Db", "Sg", "Bh", "Hs", "Mt", "Ds",
    "Rg", "Cn", "Nh", "Fl", "Mc", "Lv", "Ts", "Og" ].lower()

def func(text):
    if len(text) == 0:
        return ''
    elif text in l













text = input ('Enter text: ')