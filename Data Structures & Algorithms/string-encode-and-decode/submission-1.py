class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string=""
        for string in strs:
            encoded_string += string
            encoded_string += '.'

        return encoded_string

    def decode(self, s: str) -> List[str]:
        strs=[]
        string=""
        for char in s:
            if char != '.':
                string += char
            else:
                strs.append(string)
                string=""
        return strs