class Solution:

    def hats(self, n, H, S):
        """ print YES if the receptionist can distribute the hats agreeing with the given rule, otherwise print NO """
        self.find_start_position = 0

        def can_distribute(position):
            for i in range(self.find_start_position, n):
                if H[i] == position:
                    self.find_start_position = i+1
                    return True
            return False
        
        for i in range(n):
            if S[i] == "1":
                if not can_distribute(i+1):
                    return print("NO")
        print("YES")



if __name__=="__main__":
    t = int(input("Enter testcase number: "))
    for _ in range(t):
        n = int(input("Enter n : "))
        H = list(map(int, input("Type H : ").split()))
        S = input("Type S : ")
        Solution().hats(n, H, S)