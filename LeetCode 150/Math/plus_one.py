# 66. Plus One - easy
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]: # O(n) time, O(1) space
        '''
            So add 1 to the last element in the list. If the last digit results to 10, the last digit becomes a 0 and creates a carry. Carry will be added to the next element. The carry can also continue leftward if the subsequent elements are 9. 

            Loop backwards
              - If there is a carry or we're at the last element (first iteration)
                - Add one to the element
                - Check again if result should continue on the carry
            Return [1] + digits if there is a carry
            Else just return digits
        '''
        carry = False
        for i in range(len(digits)-1, -1, -1):
            if carry or i == len(digits)-1:
                digits[i] += 1
                
                if digits[i] == 10:
                    digits[i] = 0
                    carry = True
                else:
                    carry = False
        
        return [1] + digits if carry else digits
