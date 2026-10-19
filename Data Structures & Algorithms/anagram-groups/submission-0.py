class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strsAndIndices = {}
        toReturn = []

        for i, s in enumerate(strs) :
            ordered = "".join(sorted(s))
            if (ordered in strsAndIndices):
                strsAndIndices[ordered].append(i)
            else:
                strsAndIndices[ordered] = [i]
        
        for s, i in strsAndIndices.items():
            toAppend = []
            for index in i:
                if strs[index] != None:
                    toAppend.append(strs[index])
                else:
                    toAppend = [strs[index]]

            if toAppend != []:
                toReturn.append(toAppend)


        return toReturn