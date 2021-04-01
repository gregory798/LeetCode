class Solution:
    def isValid(self, s: str) -> bool:
        tab = []
        p = {'(':')', '[':']', '{':'}'}
        
        for i in s:
            if i in p.keys():
                tab.append(i)
            elif len(tab) > 0 and p.get(tab[-1]) == i:
                tab.pop()
            else: 
                return False

        return len(tab) == 0
