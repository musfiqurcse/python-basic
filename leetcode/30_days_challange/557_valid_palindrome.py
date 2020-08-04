class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = -1
        result = ''.join(c.lower() if c.isalpha() else c for c in s if c.isalpha() or c.isdigit())
        leno = len(result)
        if leno == 0:
            return True
        for i in range(0,int(len(result)/2)):
            if result[i]!=result[res-i]:
                return False
        return True
        
    def isExtendedPalindrome(self, s: str) -> bool:
        new_s = re.sub('[^a-zA-Z0-9]', '', s).lower()
        return new_s  ==  new_s[::-1]
