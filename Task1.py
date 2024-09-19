
#This task involves understanding the basic data types in Python such as lists, dictionaries, and sets.

#list : ordered ,mutable and allow duplicate 

l=[1,2,"A","B"] #list creation
print(l)

# aading element

l.insert(0,0)
print(l)

l.append(3)
print(l)

#removing element

l.remove(0)
print(l)

l.pop()
print(l)

#updating list 
l[2]="P"
print(l)

#accessing elements using loop

for i in l:
    print(i)



#dictionary : stores data values in key value pairs. ordered,mutable and not allow duplicate

flowers=dict({1:"Rose",2:"Mogra",3:"Lotus"}) #dictionary creation 
print(flowers)   #Display dictionary

flowers.update({4:"Marigold"}) # adding item
print("Dictionary after adding item: ",flowers)   

del flowers[1]  #deleting item
print("Dictionary after deleting item: ",flowers)   

# another way for printing dictionary 
flowers[2]="Rose"
print(flowers.items())

#set : unordered, immutable and not allow duplicate value

set={1,2,3,4,5,6,7} #creating set 

print(set) 

#adding elements
set.add(8)
print(set) 

set.add(0)
print(set) 

#removing element
set.remove(0)
print(set) 

#accessing elements using loop

for i in set:
    print(i)


#Tuple :ordered ,immutable and allow duplicate

