class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = []
        for word in strs:
            encoded.append(word)
        
        if len(strs) == 0:
            return "<n>."
        
        return ":;".join(encoded)

    def decode(self, s):
        if len(s) == 0:
            return [""]
        
        if s ==  "<n>.":
            return []
        return s.split(":;")