import re

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        counter = 0
        first_c = word[0].isupper()
        w_len = len(word)
        for i in range(1,w_len):
            if word[i].isupper():
                counter+=1
        if first_c and (counter+1 == w_len or counter+1 == 1 ):
            return True
        elif not first_c and counter == 0:
            return True
        else:
            return False


class ExtendedSolution:
    def detectCapitalUse(self, word: str) -> bool:
        if(word.lower()==word):
            return True
        if(word.upper()==word):
            return True
        if(word[0].upper()==word[0] and word[1:].lower()==word[1:]):
            return True
        return False
        


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return re.fullmatch(r"[A-Z]*|.[a-z]*", word)
