class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleanString = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        start=0
        end=len(cleanString)-1
        size=len(cleanString)
        for _ in range(size//2):
            if cleanString[start]!=cleanString[end]:
                return False
            start+=1
            end-=1
        return True

