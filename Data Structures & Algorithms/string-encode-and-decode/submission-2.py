class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for s in strs:
            encoded_string += str(len(s)) + "#"
            encoded_string = encoded_string + s
        
        return encoded_string

    def decode(self, s: str) -> List[str]:
        i = 0
        result = []
        while i < len(s):
            j = s.index('#',i)
            length = int(s[i:j])
            word = s[j+1 : j+1+length]
            i = j+1+length
            result.append(word)
        
        return result
        
