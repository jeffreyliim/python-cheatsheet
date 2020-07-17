############   CONDITIONS   ############
# array1 = [1,2,3]
#  '==' is just normal equals
#  'is' will consider memory locations. i.e. 2 lists, list1 and list2 are created in the same function, 
# list1 is not list2 because both are from seprate memory locations

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

# results = True
all(elem in array2 for elem in array1)

# check if ANY elements in array1 elements exist in array
array1=[1,2,3]
array2=[4,5,6]

# results = False
any(elem in array1 for elem in array2)	

array1=[1,2,3]
array2=[1,5,6]

# results = True
any(elem in array1 for elem in array2)  

# results = [[], [], []]
[[] for _ in range(3)]

# results = [1,2,3,5]
temp = False
array1.append(4) if temp == True else array1.append(5)

# results = [2,3]
[elem for elem in array1 if elem > 1]

# results = [true, true, false]
[elem <= 2 for elem in array1]

# find intersection between 2 lists
a = [1,2,3], b = [2,3,7]
# results = [2, 3]
[elem for elem in b if elem in a]

# results = [7]
[elem for elem in b if elem not in a]

# results = True
isinstance(1, int)
type(1) == int

# results = True
isinstance('a', str)
type('a') == str

# results = True
isinstance((), tuple)
type(()) == tuple

# results = True
isinstance({}, dict)
type({}) == dict

# results = True
isinstance([], list)
type([]) == list

# results = 3
array1[-1]

############   CLASSES    ############
# results = 10000
class Solution():
    def main(self):
        self.ans = 0
	self.changeAns()
	return self.ans

    def changeAns(self):
	self.ans = 10000

a = Solution()
a.main()


############   INTEGERS/FLOATS    ############
# num = -5

# results = 5
abs(num)

# num = 5

# results = 2
num//2

# results = 2
math.floor(2.5)

# results = 3
math.ceil(2.5)

# results = 25
num**2

# -inf 		negative infinity
float('-inf')

# inf		infinity
float('inf')

# results = -0000000000000000000000000000101			unsigned 32 int to binary
"{:032b}".format(n)



############   SETS    ############

# array = [3, 2, 1, 1]

# results = {1, 2, 3}     ******** TIP: sets will return always return unsorted/unordered and unindexed ******** 
myset = set(array)

# results = [1, 2, 3]
list(myset)

# results = 3
len(myset)

# results = {1, 2, 3, 4}
myset.add(4)

# results = ERROR
myset.remove(4)		# 4 doesnt exist in set. Can use try except for this

# results = {1, 3, 4} 		******** TIP: discard method does not panic if item not there *********
myset.discard(2)

# results = True		******** TIP: set insert/delete/add complexity is O(1) ******** very much like a map  ********
1 in myset


############	 MAPS/DICTIONARIES    ############
# mapp = {'a': 1,'b': 2,'c': 3}

# results = True
'a' in mapp or 'a' in mapp.keys()

# results = True,         **** NOTE: Does not work with array values ****
1 in mapp.values()

# results = a 1 , for loop    **** NOTE: the original map is MUTABLE in the forloop, means CAN change value while in the loop ****
#           b 2
#           c 3 
for key in mapp:
	print(key, mapp[key])

for i in mapp.items():
	key = i[0]
	val = i[1]
	print(key, val)

# results = c 3 , reverse for loop
#			      b 2
#			      a 1 
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

# array = ['word1', 'word2', 'word3'] 
# results = {'word1':'test', 'word2':'test', 'word3':'test'}
dict.fromkeys(array, 'test')

############   ARRAYS   ############
# array = [1,2,3,4]

# results = 1     ******** TIP: the original list is MUTABLE in the forloop, means CAN change value while in the loop, BUT DONT REMOVE OR ELSE INDEX OUT OR RANGE ********
#     2
#     3
#     4
for i in range(len(array)):

# results = 4
#	3
#	2
#	1

for i in range(len(array)-1, -1, -1):

# results = [1, 2, 3, 4, 1, 2, 3, 4]
array += array 

# results = [1, 2, 3, 4]
array.copy() == array[::1] == array[:] == array[::]

# results = [1, 3], start from first index, move to 2 index later
array[::2]

# results = [4, 3, 2, 1], reverse array, start from first index, move to 1 index later. **** DONT USE .reverse(), BEST TO JUST USE SLICE ****
array[::-1] 

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

# results = [4, 3, 2, 1]      ******** TIP: sorted() always returns type list ********
sorted(array, reverse=True)

# arrayOfTuples = [(1,4), (2,3), (3, 5)]
# results = [(3, 5), (1, 4), (2, 3)]
sorted(arrayOfTuples, key = lambda x: x[1], reverse=True)

# arrayOfStrings = ['a','abcd','ab','abc']
# results = ['a','ab','abc','abcd']
sorted(arrayOfStrings, key = len)
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

# results = [1, 3]							******** TIP: lambda is basically returning a function  ********
def filterOdd(a):
    if a % 2 == 1:
        return True
    else:
        return False
list(filter(filterOdd, array1)) or list(filter(lambda x : x % 2 ==1, array1))			

# results = 10
sum(array1)

# results = 1
min(array1)

# results 3
min(3, 4)

# results = 4
max(array1)

# results = 4
max(3, 4)

# results = 2.5
import statistics
statistics.mean(array1)

# results = 1 2 3 4	destructuring list
*array1

# combinations of all possible numbers in a list
# results = [1, 17, 71, 173, 137, 713, 731, 317, 371, 7, 73, 37, 3]
from itertools import permutations
nums = [1,7,3]
numbers = []
for i in range(len(nums)+1):
  for o in range(i+1, len(nums)+1):    
    print(nums[i:o])    
    if len(nums[i:o]) > 0:
      a = [int(''.join(map(str, elem))) for elem in list(permutations(nums[i:o]))]
      numbers += a
print(numbers)

############   STRINGS   ############
# string = 'abcd'

# ******** tip ******** expected result = 'azcd', actual result = cannot item assign to string
# cannot change char in string by doing string[1] = 'z'.

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

# results =  a
# 	     b
#   	     c
#	     d
for i in range(len(string)):    		******** TIP: cannot directly replace each element value while doing forloop because type string is not subscriptable. Instead do list(string) ********
	print(a[i])

# string = 'a,b,c,d'
# results = ['a','b','c','d'], splits a string that MUST have a separator.
string.split(',')

# string = 'a,b,c,d'
# results = ['a','b','cd'], splits a string 
string.split(',', 2)

# string = 'a b c d'
# results = ['a','b','c','d']
string.split(' ')

# string = 'abcd'
# results = ['a','b','c','d'], splits a string into individual characters
list(string)

# string = ['a','b','c','d']
# results = 'a-b-c-d'
'-'.join(string)

# results = 1, counts the number of occurence of a string in the string
string.count('a')

# results = 'abcd', gets lower case of string, if there is number it will ignore
string.lower()

# results = 'ABCD', gets upper case of string
string.upper()

# string = 'AbCd'
# results = 'aBcD', swaps case of letters
string.swapcase()

# results = False, checks if string is numeric
string.isnumeric()

# string = '1234'
# results = 1234
int(string)

# results = 1234.0
float(string)

# results = 0   results = -1
string.find('a'), string.find('z')

# results = 'cd'
string.replace('a','').replace('b','')

############   LINKEDLIST   ############
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

# traversing through linkedlist
while ll:
  ll = ll.next

# results = 1 -> 2 -> 3 -> 4

# traversing through copy of linkedlist and returning actual linkedlist OR traversing through actual linkedlist and return copy of linkedlist is the SAME
ll_cp = ll
while ll_cp:
  ll_cp = ll_cp.next

while ll:
  ll = ll.next

############   BINARY TREE   ############
# ********  tip ******** if you are doing traversals and want to add a value in a list, copy the value and add it in. Else, it might return the old value
# refer to https://leetcode.com/submissions/detail/314657078/

# results = 
#      10
#    5        20
#   4   8   15   21
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


# ********  tip ******** binary search trees have distinct keys hence duplicate keys are not allowed!!
# construct binary search tree with a preorder list given
# arr = [1, 2, 3]
def constructbinarytreefrompreorder(self, root, val)
root = None
for i in range(len(arr)):
  val = arr[i]
  # replacing the entire binary tree with the new value inside
  root = self.constructbtfrompreorderlist(root, val)
return root


def constructbtfrompreorderlist(self, root, val):
  # here is when we construct by adding a node
  if not root:
    return BinaryTree(val)
  if val <= root.val:
    root.left = self.construct(root.left, val)
  else:
    root.right = self.construct(root.right, val)
  # this root is returned as the first root node when the above calls are finished.
  return root


# construct binary search tree from sorted array
def sortedArrayToBST(self, nums):
    def constructbst(nums, l, r):
	if l <= r:
            mid = (l+r)//2
            return TreeNode(nums[mid], constructbst(nums, l, mid-1), constructbst(nums, mid+1, r))
    return constructbst(nums, 0, len(nums)-1)


# search for a node val in binary search tree and return the node and its children
def searchBST(self, root: TreeNode, val: int) -> TreeNode:
  res = None
  res = self.search(root, val)
  return res
    
def search(self, root:TreeNode, val: int):
  if not root:
    return None
  elif root and root.val == val:
    return root
  else:
    if val <= root.val:
      return self.searchBST(root.left, val)
    else:
      return self.searchBST(root.right, val)


# checks if its a valid binary tree. 1. Do an in order traversal, put it in temp array. Sort the array and do a comparison, remove duplicate (not allowed in binary tree)
# by using set. if same, its a binary tree.
def isValidBST(self, root: TreeNode) -> bool:
  temp = []
  self.inorder(root, temp)
  if(len(set(temp)) != len(temp)):
    return False
  copy_temp = sorted(temp[:])
  return copy_temp == temp
    
def inorder(self, root: TreeNode, temp: List[int]):
	return self.inorder(root.left) + [root.val] + self.inorder(root.right) if root else []

############   MIN HEAP   ############
# heap = []           
# results = heap = [1, 2, 3, 4]
heapq.heappush(heap, 1)
heapq.heappush(heap, 2)
heapq.heappush(heap, 3)
heapq.heappush(heap, 4)

# results = heap = [2, 4, 3]
heapq.heappop(heap)


############   COLLECTIONS   ############   <- high performance container datatypes
# list = [1, 1, 1, 1, 2, 2, 2, 3, 3]

# results = Counter({1: 4, 2: 3, 3: 2})   <- type of 'collections.Counter' == map
c = collections.Counter(list)

# results = dict_items([(1, 4), (2, 3), (3, 2)])  <- a dic_items are like maps. Foreach using "for item in results".
#                          Access the tuple by item[0] and item[1]
c.items()

# results = dict_values([1, 2, 3])      <- type of 'dict_keys' == map
c.keys()

# results = dict_values([4, 3, 2])      <- type of 'dict_values' == map
c.values()

# results = 6  ,  9
sum(c.keys()) or sum(c.values())

# results Counter({0: 3})
c = collections.Counter()
c[0] += 1
c[0] += 2

# results = Counter({1: 4, 2: 3, 3: 2})
	    3					<- max value of KEY	returns key
	    1					<- max value of VALUE   returns key

print(c)
print(max(c))
print(max(c, key=c.get))

# results [(1, 4), (2, 3)]
c.most_common(2)

# results = 4
c.get(1)

# results = Counter({1: 2, 2: 2, 5: 2, 4: 1})		***** TIP: Counter intersection takes the key and the max value of intersection *****
	    Counter({2: 3, 1: 1, 6: 1, 5: 1})
	    Counter({2: 2, 1: 1, 5: 1})
	    
d = Counter([1,1,2,2,4,5])
a = Counter([1,1,2,2,6,5])
print(d)
print(a)
print(d & a)

# results = Counter({1: 2, 2: 2, 5: 2, 4: 1})		***** TIP: Counter intersection takes the key and the MAX value of intersection AND the union of items not in intersection *****
	    Counter({2: 3, 1: 1, 6: 1, 5: 1})
	    Counter({2: 3, 1: 2, 5: 2, 4: 1, 6: 1})

d = Counter([1,1,2,2,4,5,5])
a = Counter([2,1,2,2,6,5])

print(d)
print(a)
print(d | a)


############   DEQUEUE   ############   <- high performance container datatypes
from collections import deque
queue = deque([1,2,3,4,5])

# results = deque([1, 2, 3, 4])
queue.pop()

# results = deque([2, 3, 4, 5])
queue.popleft()

# results = [1, 2, 3, 4, 5]
list(queue)

