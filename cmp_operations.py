list_num = [1,2,3,4]
tup_num = (1,2,3,4)

print(list_num)
print(tup_num)

# printing the type 
type(list_num)
type(tup_num)
# modifying item between tuples and list 
#tuples does not support item assigement
list_num[2] = 5
print(list_num)

# tup_num[2] = 5 #it shows an error S

dir(list_num) 
dir(tup_num)

#srtings
str1 = 'Hello Python'  
print(str1)  
#Using double quotes  
str2 = "Hello Python"  
print(str2)  
  
#Using triple quotes  
str3 = '''''Triple quotes are generally used for  
    represent the multiline '''   
print(str3)
str = "HELLO"  
print(str[0])  
print(str[1])  
print(str[2])  
print(str[3])  
print(str[4])  
# It returns the IndexError because 6th index doesn't exist  
print(str[6]) 

s = "heLLo BuDdY"
s2 = s.capitalize()
print(s2)
s = 'Dread Thread Spread'
s.find('Thr')
s.find('rea')

s.find('rea', 4, 18)

s.find('x')

#Swaps case of all alphabetic characters.

s = "heLLo BuDdY"
s2 = s.swapcase()
print(s2)


s1 = input('Please enter the first string:\n')
s2 = input('Please enter the second string:\n')

print('Concatenated String =', s1 + s2)


# String Functions:

demo = "Aakash is a good boy" 
print(demo.endswith("boy"))
print(demo.count('o'))
print(demo.capitalize())
print(demo.upper())
print(demo.lower()) 
print(demo.find("good","nice"))

