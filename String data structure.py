
class Solution(object):
    def reverseString(self, s):
        """
        type s:str
        rtype: str
        """
        return s[::-1]

    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        indx=len(s)//k
        for i in range(indx+1):
            if i%2==0:
                s=s[:i*k]+s[i*k:(i+1)*k][::-1]+s[(i+1)*k:]
        return s
        


if __name__=="__main__":
    sol=Solution()
    print(sol.reverseString('hello'))
    s="hyzqyljrnigxvdtneasepfahmtyhlohwxmkqcdfehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqlimjkfnqcqnajmebeddqsgl"
    k=39
    m=sol.reverseStr(s,k)
    print(m)