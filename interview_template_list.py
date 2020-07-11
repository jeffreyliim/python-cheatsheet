class Solution:
    def main(self, input):
        print(input)

n = int(input())
for i in range(n):
    input()
    s = Solution()
    print(s.main(input().split(' ')))


#################### matrix #################### 				sample input: 	3 1
												1 2 3
												4 5 6
												7 8 9
def solve(array, n, k):
    # Write your code here
    
    
    
n, k = map(int, raw_input().strip().split())
array = [n]
for i in range(n):
    array.append([int(i) for i in raw_input().strip().split()])
    

solve(array, n, k)


#################### array of numbers ####################					sample input: 	7
														1 0 1 1 1 0 1
def solve(array, n):
    result = -1
    # Write your code here
    # Return the result
    
    return result
    
n = int(raw_input())
array = [int(i) for i in raw_input().strip().split()]
print(solve(array, n))



#################### array of chars ####################                                      sample input:   7
                                                                                                                abcdadcdadc
def solve(array, n):
    result = -1
    # Write your code here
    # Return the result

    return result

n = int(raw_input())
array = [str(i) for i in raw_input().strip().split()]
print(solve(array, n))
