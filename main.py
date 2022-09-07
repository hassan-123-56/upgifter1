#Uppgift 1#

print(10 + 3)
print(6 * 3)
print(7 % 2)
print(3 + 4 * 5)
print((5 * 2) % 3)
a = 10
print(5 + 6)
b= 5
print(a > b)
print(a * b < a)
print(a == b)
print(b == a or b == 3)
print(8 + 12)
print(6 - 8)
print(3 - 10)



#Uppgift 2#
A = int (10)

b = str("Python")

C = float (12.43)

print (A,b,C)
#uppgift 3#
state = 1

while state == 1:
    num = int(input("Skirv en siffra: "))

    if num > 0:
        print("positivt")

    elif num < 0:
        print ("negativt")

    state = int(input("Fortsätta? 1. Ja, 2. Nej: "))
