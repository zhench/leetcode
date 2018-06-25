
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
        if len(s) != len(t):
            return False
        i = len(t) - 1
        while i >= 0:
            tchar = t[i]
            if tchar in s:
                s=s.replace(tchar, '', 1)
                i -= 1
            else:
                return False
        if len(s) == 0:
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
    s = "anagram"
    m = "nagaram"
    print(sol.isAnagram(s,m))
