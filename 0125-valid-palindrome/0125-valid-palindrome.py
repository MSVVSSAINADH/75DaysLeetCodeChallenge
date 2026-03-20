class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            if not s[i].isalnum():
                i += 1
            elif not s[j].isalnum(): #ignores if it is not alphanumeric
                j -= 1
            elif s[i].lower() != s[j].lower(): #checks characters irrespective of the casing
                return False
            else:
                i += 1
                j -= 1
            
        return True