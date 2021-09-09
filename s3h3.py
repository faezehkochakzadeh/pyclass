#faezeh kuchakzadeh
#class thursday 14-18
#s3h3

def mathematic():
    shekl= input('shekl morede nazar ra vared konid (mostatil,dayere,mosalas): ')
    mohasebat=input('mohit ya masahat? : ')
    pi=3.14

    if shekl == 'mostatil'and mohasebat== 'mohit' :

        tool=int(input('tool mostatil ra vared konid : '))
        arz=int(input('arz mostatil ra vared konid : '))
        print((tool*arz)**2)
    elif shekl == 'mostatil'and mohasebat== 'masahat' :

        tool=int(input('tool mostatil ra vared konid : '))
        arz=int(input('arz mostatil ra vared konid : '))
        print(tool*arz)
    elif  shekl== 'dayere' and mohasebat == 'mohit' :
        r=float(input('shoAe dayere ra vared konid : '))
        print(2*pi*r)
    elif shekl== 'dayere' and mohasebat == 'masahat' :
        r=float(input('shoAe dayere ra vared konid : '))
        print(pi*(r**2))
    elif shekl== 'mosalas' and mohasebat == 'mohit' :
        ghaede = int(input('yek zel az mosalase motasaviol azla vared konid : '))
        print (ghaede *3)
    elif shekl== 'mosalas' and mohasebat =='masahat':
        ghaede=int(input('ghaede ra vared konid :'))
        ertefa=int(input('ertefa ra vared konid :'))
        print((ghaede * ertefa) / 2)
    else:
        print('error!!!')

mathematic()
