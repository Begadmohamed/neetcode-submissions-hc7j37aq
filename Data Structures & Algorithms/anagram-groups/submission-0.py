class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        for str in strs:
            freq = [0] * 26
            for c in str:
                freq[ord(c)-ord('a')] += 1
            key=tuple(freq)
            mp[key].append(str)

        return list(mp.values())