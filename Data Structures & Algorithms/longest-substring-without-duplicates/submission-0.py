class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        i=0
        j=0
        hashTable={}
        maxLen = 0
        while j<len(s):
            hashTable[s[j]] = hashTable.get(s[j],0) + 1
            while hashTable[s[j]] > 1:
                hashTable[s[i]] -= 1
                i+=1
            maxLen=max(maxLen,j-i+1)
            j+=1
        return maxLen
