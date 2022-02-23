import math
import ipaddress
#2
def centenaire(age) :
    if (age !=0 ) & (type(age)==int):
        cent=100-age
        print(' Vous aurez 100 ans en ',2022+cent)
    else:
        print('entrer une valeur valide')

#3
def cone(r,h) :
    if (r !=0 ) & (type(r)==int) & (h !=0 ) & (type(h)==int) :
        
        return math.pi * r **2 * (h/3)
    else :
        print('Entrer des valeurs valides')

#4
def pair(nb):
    
    if (type(nb)==int):   
        if nb%2==0 :
            print(nb,'est pair')
        else :
            print(nb,' est impair' )
    else :
        print('Valeur non valide')
#5
def fibo (n):
    if (type(n)==int):
        f1 = 0
        f2 = 1
        if (n < 1): 
            return
        for x in range(0, n): 
            print(f2, end = " ") 
            next = f1 + f2 
            f1 = f2 
            f2 = next
    else :
        print("nombre invalide")
    
#6
def PPCM_PGCD(a,b):
    ppcm = a
    while (ppcm%a != 0 or ppcm%b !=0) :
        ppcm = ppcm + 1
    print('PPCM of ',a,'and',b,'is',ppcm)
        
    pgcd = a
    while (a%pgcd != 0 or b%pgcd !=0):
        pgcd = pgcd - 1
    print('PGCD of ',a,'and',b,'is',pgcd)
#7
def commun(ls1,ls2) :
    if (type(ls1)==list) & (type(ls2)==list) :
        ls_set = set(ls1)
        if len (ls_set.intersection(ls2))==0 :
            print(' pas de valeurs communes')
        else :    
            return ls_set.intersection(ls2)
    else :
        print('paramètres invalides')
        
#8
def Palindrome(s):
    if (type(s)==str) :
        isit = s[::-1]
        if isit==s:
            print(" la chaine est un palindrome ")
        else:
            print("le string n'est pas un palindrome ")
    else :
        print('Entrer a valid string')
    
    
#9
def remove_red(ls) :
    if type(ls)==list :    
        mylist = list(dict.fromkeys(ls))
        print('new unique list :',mylist)
    else :
        print('Entrer une liste Valide')
        
#10
def ip(string):
    if (type(string)==str) :
        try:
            ip=ipaddress.ip_address(str)
            print('IP address',string,'is valid',ip)
        except ValueError:
            print('IP address',string,'is not valid') 
        ipaddress.ip_address(string)
    else :
        print('Entrer une valeur valide ')
        
