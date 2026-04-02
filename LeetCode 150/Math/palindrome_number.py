# 9. Palindrome Number - easy
class Solution:
    def isPalindrome(self, x: int) -> bool: # O(n) time, O(n) space
        # if x < 0:
        #     return False

        # str_num = str(x)
        # i, j = 0, len(str_num)-1
        # for i in range(len(str_num)):
        #     if str_num[i] != str_num[j]:
        #         return False
            
        #     i += 1
        #     j -= 1
        
        # return True

        # return str(x) == str(x)[::-1]

        '''
            Math method to avoid strings and uses O(logn) time and O(1) space

            - Palindrom is symmetric -> so just reverse half
            - Repeatedly take the last digit of the number and build reversed_half with those digits
              - at the same time, remove those digits from the original number

              - do this until half the digits are processed

              - if the number has an even number of digits -> both halves should be equal
              - if the number has an odd number of digits -> ignore the middle digit (reversed_half // 10)
        '''
        if x < 0 or (x % 10 == 0 and x != 0): # negative numbers and numbers ending with 0 can't be palindromes
            return False
        
        reversed_half = 0

        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x = x // 10

        return x == reversed_half or x == reversed_half // 10

'''
x = 121

digit = 1
reversed_half = 0 * 10 + 1 = 1
x = 121 // 10 = 12

digit = 2
reversed_half = 1 * 10 + 2 = 12
x = 12 // 10 = 1

Check:
reversed_half = 12
x (1) == reversed_half//10 (1)
'''
