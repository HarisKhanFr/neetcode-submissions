class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        wMap = {}

        for word in strs:
            count = [0] * 26

            for letter in word:
                count[ord(letter) - ord("a")] = word.count(letter)
            
            count = tuple(count)

            if count in wMap.keys():
                temp = list(wMap.get(count))
                temp.append(word)
                wMap[count] = temp 

            else:
                wMap[count] = [word]

        final = []
        for array in wMap.values():
            final.append(array)

        return final