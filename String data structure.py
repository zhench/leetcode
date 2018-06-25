
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
        indx = len(s) // k
        for i in range(indx + 1):
            if i % 2 == 0:
                s = s[:i * k] + s[i * k:(i + 1) * k][::-1] + s[(i + 1) * k:]
        return s

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        lst = s.split()
        for l in lst:
            res.append(l[::-1])
        return ' '.join(res)

    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        for i in range(ord('a'),ord('z')+1):
            if s.count(chr(i))!=t.count(chr(i)):
                return False
        return True
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s=s.lower()
        s=[i for i in s if i.isalnum()]
        if s==s[::-1]:
            return True
        return False

if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseString('hello'))
    s = "hyzqyljrnigxvdtneasepfahmtyhlohwxmkqcdfehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqlimjkfnqcqnajmebeddqsgl"
    k = 39
    m = sol.reverseStr(s, k)
    # print(m)
    s = 'abc def ghi'
    # print(sol.reverseWords(s))
    s ="nl"
    m = "cx"
    print(sol.isAnagram(s,m))
    s="race a car"
    print(sol.isPalindrome(s))
