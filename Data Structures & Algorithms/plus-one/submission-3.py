class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            temp = digits[i]
            digits[i] = (digits[i] + carry)%10
            carry = (temp + carry)//10
            print(digits, carry)
            
        if carry:
            temp = [1]
            temp.extend(digits)
            return temp
        return digits