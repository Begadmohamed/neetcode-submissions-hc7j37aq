class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        
        i = 0
        j = 0
        hashTable = {}
        maxLen = 0
        
        while j < len(s):
            char = s[j]
            hashTable[char] = hashTable.get(char, 0) + 1
            
            while hashTable[char] > 1:
                left_char = s[i]
                hashTable[left_char] -= 1
                i += 1
            
            maxLen = max(maxLen, j - i + 1)
            j += 1
            
        return maxLen