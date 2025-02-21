#Lists
#index starts at 0, built with [], can contain any type of variable

num_list = [10, 43, 22, 5, 63, 101, -5, 3]
print(num_list) 

name_list = ['Julia', 'Luciano', 'Peter', 'Sara']
print(name_list)

num_list[0]                 #first element --> 10 , index starts at 0
name_list[1]                #Luciano

empty_list = []
print(len(empty_list))      #lenght of list is 0

mix_list = [10, 'fruit']    #supports mixed data type lists, sort() is not possible in this case
print(mix_list)

print(num_list[1:5])        #slice returns: [43, 22, 5, 63]
print(len(num_list))        # return: 8. Slice does not modify list size

print(28 not in num_list)   #True
num_list.append(28)         #adds an element at the back of the list
print(num_list)
print(28 in num_list)       #True
num_list.sort()             #returns None - list.sort() sorts list in-place 
print(num_list)


name_list[0] = 'Leia'               #changes first element
print(name_list)                    #['Leia', 'Luciano', 'Peter', 'Sara']
print('Leia' in name_list)          #True
name_list.remove('Luciano')     
print(len(name_list))               #3
print('Luciano' not in name_list)   #True                   
print(name_list[1])                 # 'Peter'
print(name_list)                    #['Leia', 'Peter', 'Sara']


fruits = 'Strawberry,Apple,Orange,Clementine,Banana,Watermelon,Pear'
fruit_list = fruits.split(',')          #takes ',' as string splitter to create a list
print(fruit_list)                       #['Strawberry', 'Apple', 'Orange', 'Clementine', 'Banana', 'Watermelon', 'Pear']
print(fruit_list[0])                    #Strawberry
print(fruit_list[1])                    #Apple
print(fruit_list[-1])                   #Last element - Pear
print(fruit_list[-2])                   #Watermelon
fruit_list.append('Lemon')              #adds Lemon to the end of the list
print(fruit_list)
fruit_list.insert(0,'Lemon')            #adds Lemon to the beginning of the list
print(fruit_list)
fruit_list.insert(2,'Grape')            #insert can be done in any index of the list, if index>len it is inserted in the back
print(fruit_list)
fruit_list += ['Kiwi', 'Cherry']        #joins elements to the back of the list
print(fruit_list)

fruits = 'Apple,Orange,Banana'
fruit_list = fruits.split(',')
shopping = ['Coffee', fruit_list, 'Eggs']       #the list carries a list within
#accessing
print(shopping[1])                              #['Apple','Orange','Banana']
print(shopping[1][1])                           # Orange
print(shopping[1][1][1])                        # r - index 1 of the string Orange

errands = [shopping, 'Bank', 'Walk the dog']    #[['Coffee', fruit_list, 'Eggs'], 'Bank', 'Walk the dog']
print(errands)                                  #[['Coffee', ['Apple', 'Orange', 'Banana'], 'Eggs'], 'Bank', 'Walk the dog']
print(shopping in errands)                      #True
print(fruit_list in errands)                    #False
print('Orange' in errands)                      #False
print('Orange' in errands[0][1])                #True
print(len(errands))                             #3
