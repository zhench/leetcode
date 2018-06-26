
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
        for i in range(ord('a'), ord('z') + 1):
            if s.count(chr(i)) != t.count(chr(i)):
                return False
        return True

    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        s = [i for i in s if i.isalnum()]
        if s == s[::-1]:
            return True
        return False

    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        r = ''
        str = str.lstrip()
        if len(str)==0:
            return 0
        if str[0] not in "-+0987654321":
            return 0
        if str[0] in '-+':
            r+=str[0]
        start=len(r)
        for i in str[start:]:
            if i in '1234567890':
                r += i
            else:
                break
        try:
            r = int(r)
            if r < -2**31:
                return -2**31
            elif r > 2**31 - 1:
                return 2**31 - 1
            return r
        except ValueError:
            return 0
    def countAndSay(self, n):  
        """ 
        :type n: int 
        :rtype: str 
        """  
        if n==1:#类似于斐波拉契数，后面的数跟前面的数有关  
            return '1'  
        if n==2:  
            return '11'  
        pre='11'  
        for i in range(3,n+1):  
            res=''#结果，每次报数都要初始化  
            cnt=1#计数  
            length=len(pre)  
            for j in range(1,length):  
                if pre[j-1]==pre[j]:#相等则加一  
                    cnt+=1  
                else:  
                    res+=str(cnt)+pre[j-1]  
                    cnt=1#重置为1  
            res+=str(cnt)+pre[j]  
            pre=res#保存上一次的结果  
        return res
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0:
            return ''
        res=""
        flag=True
        first_str=strs[0]
        length=len(strs[0])
        for substr in strs:
            if len(substr)<length:
                length=len(substr)
                first_str=substr
        
        for i in range(length):
            for substr in strs:
                if first_str[i] == substr[i]:
                    flag=True
                else:
                    flag=False
                    return res
            if flag:
                res+=first_str[i]
        return res
                    


if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseString('hello'))
    s = "hyzqyljrnigxvdtneasepfahmtyhlohwxmkqcdfehybknvdmfrfvtbsovjbdhevlfxpdaovjgunjqlimjkfnqcqnajmebeddqsgl"
    k = 39
    m = sol.reverseStr(s, k)
    # print(m)
    s = 'abc def ghi'
    # print(sol.reverseWords(s))
    s = "nl"
    m = "cx"
    print(sol.isAnagram(s, m))
    s = "race a car"
    # print(sol.isPalindrome(s))
    s = "42"
    print(sol.myAtoi(s))
    print(sol.countAndSay(5))
    print(sol.longestCommonPrefix(['a']))
