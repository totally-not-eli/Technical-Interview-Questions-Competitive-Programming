class Solution:
    def reverseInteger(self,bint):
        #naive way
        bstr = str(bint)
        new_s = ""
        if bstr[0] == "-":
            val = -1
            new_s = bstr[1:]
            new_s = new_s[::-1]
            nint = int(new_s)*val
        else:
            val = 1
            new_s = bstr[:]
            new_s = new_s[::-1]
            nint = int(new_s)*val
        try:
            if nint >= 2**31 - 1 or nint <= -2**31:
                return 0
            else:
                return nint
        except:
            return 0

if __name__ == '__main__':
    x = Solution()
    i = int(input("Please enter a valid integer: "))
    print(x.reverseInteger(i))
