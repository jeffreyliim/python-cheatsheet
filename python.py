############   CONDITIONS   ############
# array1 = [1,2,3]
is equals ==
is not equals !=

# results = True
3 in array1

# results = False
3 not in array1

# check if ALL elements in array1 elements exist in array
array1 = [1,2,3]
array2=[1,3,2] or array2=[2,2,2] or array2 = [2]

# results = True
all(elem in array1 for elem in array2) 	

array1=[2]
array2=[2,3]

# results = False
all(elem in array1 for elem in array2) 	

# check if ANY elements in array1 elements exist in array
array1=[1,2,3]
array2=[4,5,6]

# results = False
any(elem in array1 for elem in array2)	

array1=[1,2,3]
array2=[1,5,6]

# results = True
any(elem in array1 for elem in array2)  


############	MAPS/DICTIONARIES    ############
# mapp = {	'a':1,	'b':2, 	'c':3  }

# results = a 1 , for loop
#			b 2
#			c 3 
for key in mapp:
	print(key, mapp[key])

# results = c 3 , reverse for loop
#			b 2
#			a 1 
for key in reversed(mapp):
	print(key, mapp[key])

# results = { 'a': 1, 'b': 2, 'c': 3, 'd': 4}, add item to map
mapp['d'] = 4

# results = { b': 2, 'c': 4 }, remove item from map
mapp.pop('a')

# results = 3, length of map
len(mapp)

# mapp2 = {'c': 4, 'd': 5, 'e': 6}
# results = {'a': 1, 'b': 2, 'c': 4, 'd': 5, 'e': 6}, merge 2 dictionaries together 
mapp.update(mapp2)


############   ARRAYS   ############
# array = [1,2,3,4]

# results = [1, 2, 3, 4, 1, 2, 3, 4]
array += array 

# results = [1, 2, 3, 4]
array.copy() == array[::1] == array[:] == array[::]

# results = [1, 3], start from first index, move to 2 index later
array[::2]

# results = [4, 3, 2, 1], reverse array, start from first index, move to 1 index later
array[::-1] # DONT USE .REVERSE(), best just use slice.

# results = [3, 1], reverse array, skip first index, move to 2 index later
array[::-1][1::2]

# results =[4, 2], reverse array, start from first index, move to 2 index later
array[::-2]

# results = [1, 2, 3, 4]
array.sort()
array

# results = [4, 3, 2, 1]
array.sort(reverse=True)
array

# count elem == value in list
array.count('4') 	# returns 1

# length of array 
len(array)

# results = [1, 2, 5, 3, 4], insert item 5 in array at index 2
array.insert(2, 5)

# results = ['cat', 'rabbit', 'guinea pig'], removes value in array
array = ['cat', 'dog', 'rabbit', 'guinea pig']
array.remove('dog')
array

# results = ['cat', 'guinea pig', 'rabbit'], sorts array by first character
array.sort()
array



############   STRINGS   ############
# string = 'abcd'

#results = 'abcd'
string[::1] == string[:] == string[::]

# results = 'abcd'
string[::1] == string[:] == string[::]

# results = 'ac', start from first index, move to 2 index later
string[::2]

# results ='dcba', reverse array start from first index, move to 1 index later
string[::-1]

# results = 'ca', reverse array, skip first indedx, move to 2 index later
string[::-1][1::2]

# results ='db', reverse array start from first index, move to 2 index later
string[::-2]

# results = 4, length of string
len(string)

# string = 'a,b,c,d'
# results = ['a','b','c','d'], splits a string that MUST have a separator.
string.split(',')

# string = 'a,b,c,d'
# results = ['a','b','cd'], splits a string 
string.split(',', 2)

# results = ['a','b','c','d'], splits a string into individual characters
list(string)

# string = ['a','b','c','d']
# results = 'a-b-c-d'
'-'.join(string)

# results = 1, counts the number of occurence of a string in the string
string.count('a')

# results = 'abcd', gets lower case of string
string.lower()

# results = 'ABCD', gets upper case of string
string.upper()

# string = 'AbCd'
# results = 'aBcD', swaps case of letters
string.swapcase()

# results = False, checks if string is numeric
string.isnumeric()


########  LINKEDLIST  ###########
class LinkedList:
  def __init__(self, val):
    self.val = val
    self.next = None
  
  def insert(self, val):
    while self.next:
      self = self.next
    self.next = LinkedList(val)

ll = LinkedList(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)

# results = 1 -> 2 -> 3 -> 4

########  BINARY TREE  ###########
class BinaryTree:
  def __init__(self, val):
    self.left = None
    self.right = None
    self.val = val

  def add(self, root, val):
    if root.val < val:
      if root.right is None:
        root.right = BinaryTree(val)
      else:
        self.add(root.right,val)
    else:
      if root.left is None:
        root.left = BinaryTree(val)
      else:
        self.add(root.left, val)


t = BinaryTree(10)
t.add(t, 5)
t.add(t, 20)
t.add(t, 4)
t.add(t, 8)
t.add(t, 15)
t.add(t, 21)

# results = 
#		   10
#	   5        20
#   4	  8   15   21



