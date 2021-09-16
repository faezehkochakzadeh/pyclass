#faezeh kuchakzadeh
#class thursday 14-18
#s4h1 hajm va masahat mokaab,kore,makhroot
def mokabe_mostatil (tool, arz, ertefa):
    amaliyat= input('hajm ya masahate mokabe mostatil?')
    if amaliyat == 'masahat' :
        masahat = ((tool*arz)+(tool*ertefa)+(ertefa*arz))*2
        #print(f'masahat mokab mostatil barabar ast ba = {masahat}')
        return masahat
    elif amaliyat == 'hajm' :
        hajm = tool*arz*ertefa
        #print(f'hajm mokab mostatil barabar ast ba = {hajm}')
        return hajm
    else:
        print('error!!')

print(mokabe_mostatil(3,5,7))

def kore(r):
    pi=3.14
    amaliyat = input('hajm ya masahate kore?')
    if amaliyat == 'masahat' :
         masahat = 4*pi*(r**2)
         return masahat
    elif amaliyat == 'hajm' :
        hajm = (4/3)*pi*(r**3)
        return hajm
    else:
        print('error!!!')

print(kore(5))

def makhroot(r,ertefa,s):
    amaliyat = input('hajm ya masahate makhroot?')
    pi = 3.14
    if amaliyat == 'masahat' :
        masahate_janebi = pi*r*s
        masahate_ghaede = pi*(r**2)
        masahat = masahate_janebi + masahate_ghaede
        return masahat
    elif amaliyat == 'hajm' :
        hajm = (1/3)*pi*(r**2)*ertefa
        return hajm
    else:
        print('error!!!')
print(makhroot(3,6,5))
