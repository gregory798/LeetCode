class Solution:
    def romanToInt(self, s: str) -> int:
        standard = {"M":1000, "CM":900, "D":500, "CD": 400,"C":100,"XC":90, "L":50, "XL":40,"X":10, "IX":9, "V":5, "IV":4, "I":1}
        n = 0
        special = ["CM","CD","XC","XL","IX","IV"]
        for i in special:
            if i in s:
                n = n + standard[i]
                s=s.replace(i,"")
        for i in s:
            n = n + standard[i]
        return(n)
        
