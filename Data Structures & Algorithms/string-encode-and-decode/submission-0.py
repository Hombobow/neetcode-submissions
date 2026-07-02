class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word))
            res += "#"
            res += word
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        n = len(s)
        while i < n:
            length = ""
            while s[i] != "#":
                length += s[i]
                i += 1
            i += 1
            
            t = int(length)

            res.append(s[i:i+t])
            i += t
        
        return res