#Matrix as list of lists

M = [[1,2],[3,4]]       # M[0] first row [1,2] - M[1] second row [3,4]
print(M[0][1])          # 2 - first row second column element   

N = [[1,0,3],[0,5,5],[8,-1,1],[10,3,1]]
print(N[1][2])          #5
print(N[2][1])          #-1

#Tuple - Associated to vector, constructor ()

a = (2, 4)
b = (-1, 2)
c = a + b
print(c)                #(2, 4, -1, 2) 
d = (1, 5, 10, 3, 7)
print(a[1])             #4
#print(d[9])            !out of range   
print(d[1:5])           #(5, 10, 3, 7)
#d[2] = 11              !BEWARE tuples are immutable such as strings, its elements cannot be replaced                   
d = (1, 5, 11, 3, 7)    #Must be constructed anew to "replace" an element
print(d)

#Set - constructor {}

a = {2, 4}
citrics = {'Orange', 'Lemon', 'Clementine'}         #constructor sets elements in random order
citrics = set(['Orange', 'Lemon', 'Clementine'])
print(citrics)                                      #{'Lemon', 'Orange', 'Clementine'}
print('Orange' in citrics)                          #True
citrics.add('Grapefruit')
print(citrics)                                      #{'Lemon', 'Orange', 'Grapefruit', 'Clementine'}
citrics.remove('Orange')
print(citrics)                                      #{'Lemon', 'Grapefruit', 'Clementine'}
print(len(a))                                       #2
