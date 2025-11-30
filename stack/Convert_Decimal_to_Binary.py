class Solution(object):
    def decimal_to_binary(self,n):
        s = []
        if n == 0:
            return 0
        while n != 0:
            s.append(str(n % 2))
            n = n // 2
        return "".join(reversed(s))
    
s = Solution()    
print(s.decimal_to_binary(5)) # 101
print(s.decimal_to_binary(8)) # 1000
print(s.decimal_to_binary(0)) # 0