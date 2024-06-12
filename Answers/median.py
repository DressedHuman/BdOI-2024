class Solution:
    def median(self, n, bit_array):
        zero_count = 0
        for bit in bit_array:
            if bit == 0:
                zero_count += 1
        
        if zero_count < (n/2):
            print(1)
        else:
            print(0)



if __name__=="__main__":
    n = int(input("Enter n: "))
    bit_array = list(map(int, input("Type the bit array: ").split()))
    Solution().median(n, bit_array)