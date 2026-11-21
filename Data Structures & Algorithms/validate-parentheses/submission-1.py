class Solution:
    def isValid(self, s: str) -> bool:
        hashS = {
            '(' : 0, 
            ')' : 0, 
            '{' : 0, 
            '}' : 0, 
            '[' : 0, 
            ']' : 0, 
            }

        for i in range(len(s)) :
            hashS[s[i]] = hashS.get(s[i], 0) + 1

        if hashS.get('(') != hashS.get(')') or hashS.get('{') != hashS.get('}') or hashS.get('[') != hashS.get(']')  :
            return False

        last = []
        
        print(len(s))
        
        for elem in s :
            print(elem)
            if elem == '(' or elem == '{' or elem == '[':
                last.append(elem)
            else :
                if last == [] or last == None :
                    print(last)
                    return False
                
                if elem == ')':
                    if last[-1] != '(' :
                        return False
                elif elem == '}':
                    if last[-1] != '{' :
                        return False
                elif elem == ']' :
                    if last[-1] != '[' :
                        return False
                
                last.pop()

        return True

            

        
