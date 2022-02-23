import function
#1

nom,prenoms=(input('Entrer votre nom \n'),input('Entrer votre prenom \n'))
print  ('Bonjour',prenoms,' ',str.upper(nom))

#2

age=int(input(" Entrer votre age "))
function.centenaire(age)


#3

rayon,hauteur=(int(input('Entrer le  rayon en cm \n')),int(input('Entrer la hauteur en cm \n')))
result=function.cone(rayon,hauteur)
print('le volume est de',result,'cm^3')

#4

nombre=int(input('Entrer le nombre  \n'))
function.pair(nombre)


#5

n_fibbo=int(input('Entrer le nombre de termes de la suite   \n'))
function.fibo(n_fibbo)

#6

function.PPCM_PGCD(25,5)


#7
print(function.commun([5,6,7],[6,7,8,9,10]))
print(function.commun([5,6,7],[8,9,10]))

#8

function.Palindrome('itopiNonavevanoNipoti')
function.Palindrome('itopiNonavevanoNiAi')

#9
function.remove_red([4,5,7,7,8,8,9,6,6,1,2,2])

#10
function.ip("192.0.1.246")




