class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
            l_groups, longest = zip(*strs), ""
            for letter_group in l_groups:
                if len(set(letter_group)) > 1: break
                longest += letter_group[0]
            return longest
