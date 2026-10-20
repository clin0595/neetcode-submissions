class Solution:

    def encode(self, strs: List[str]) -> str:
        toReturn = ""
        for string in strs:
            toReturn = toReturn + str(len(string)) + "#" + string
        
        return toReturn

    def decode(self, s: str) -> List[str]:
        toReturn = []
        i = 0
        while i < len(s) :
            j = i
            
            while s[j] != '#':
                j += 1;
            
            num = s[i:j]
            num = int(num)
            toReturn.append(s[j+1 : j+1+num])
            i = j + 1 + num

        return toReturn