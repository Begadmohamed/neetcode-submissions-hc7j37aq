class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap1={}
        for char in s:
            hashMap1[char] = hashMap1.get(char, 0) + 1
        
        hashMap2={}
        for char in t:
            hashMap2[char] = hashMap2.get(char, 0) + 1
        
        for key,value in hashMap1.items():
            if hashMap1.get(key)!=hashMap2.get(key):
                return False
        
        for key,value in hashMap2.items():
            if hashMap2.get(key)!=hashMap1.get(key):
                return False
        return True

