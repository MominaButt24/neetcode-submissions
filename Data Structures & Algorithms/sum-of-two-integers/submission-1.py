class Solution:
    def getSum(self, a: int, b: int) -> int:
        # return (~(a & b)) & 15
        # return (a&b) ^ 15
        res = 0
        carry = 0

        for i in range(32):
            cur_bit1 = a & 1
            cur_bit2 = b & 1
            # XOR the two individual bits together along carry
            xor_bit = (cur_bit1 ^ cur_bit2) ^ carry
            # Shift the result bit back to its proper position and add to total
            res |= (xor_bit << i)

            # Full-Adder Carry Logic
            # A carry is generated if at least two of these are 1: cur_bit1, cur_bit2, or the old carry
            carry = (cur_bit1 & cur_bit2) | (cur_bit1 & carry) | (cur_bit2 & carry)
            # if carry:
            #     carry -=1
            # if cur_bit1 & cur_bit2 == 1:
            #     carry +=1
            # shift both source numbers right to move to the next bit
            a = a >> 1
            b = b >> 1
            
         # Handle 32-bit signed negative integers (Python specific)
        if res >= 0x80000000:
            res = ~(res ^ 0xFFFFFFFF)

        return res