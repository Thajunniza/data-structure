""" 
you have a 0 indexed array nums with both positive and negative numbers
get the next greater number and return a list
if there is no greatest element then mark as -1
## Example
num =[1,3,4,2]
resulut = [3,4,-1,-1]
"""

class Solution(object):
    def getNextGreatestNumber(self,num):
        n = len(num)
        result = [0] * n
        stack = []
        i = n - 1
        while i >=0:
            while stack and num[i] > stack[-1]:
                stack.pop()
            if stack:
                result[i] = stack[-1]    
            else:
                result[i] = -1
            
            stack.append(num[i])
            i -= 1
        return result

#----------------------
# Driver Test
#----------------------
if __name__ == "__main__":
    sol = Solution()
    print(sol.getNextGreatestNumber([1, 3, 4, 2]))  # Expected: [-3,4,-1,-1]
    print(sol.getNextGreatestNumber([2, 4 ,1, 2, 3, 4]))     # Expected: [4,4,2,3,4,-1]    