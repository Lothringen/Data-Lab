#Strings

a = 'Today is Wednesday'    #single quote
b = "I begin the data lab"  #or double quotes

c = a + b
print(c)

c = a + ', ' + b
print(c)

a[6]            #a at index 4  'i'
a[6:8]          #a substring from index 4 to prev-8   'is'
a[6:]           #a substring from index 4 to end    'is Wednesday'
a[:5]           #a substring from start to index prev-5 'Today'
# a[1] = 'x'    Beware ERROR! Strings are immutable

print('Printing a string')

a = 'Hello' + 'World'   #concatenation of strings: 'HelloWorld'
b = 'Say ' + a          # 'Say HelloWorld'
s = 'Hello '            
l_s = len(s)            #length is 6, len(string) counts any leading or trailing whitespaces
print(l_s)
s2 = '  Hello'          #len is 7
l_s2 = len(s2)
print(l_s2)                 
print('e' in s)         #belongs? True
print('x' in s)         #False
print('hi' not in s)    #True
print(s*5)              #replication 'Hello  Hello  Hello  Hello  Hello  '
print(s.lower())        #'hello '
print(s.upper())        #'HELLO '
print(s.strip())        #'Hello' strip() removes any leading, and trailing whitespaces
