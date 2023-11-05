from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        anagram_dict = defaultdict(list)

        for word in strs:

            count = [0] * 26

            for char in word:
                count[ord(char) - ord('a')] += 1
            
            anagram_dict[tuple(count)].append(word)
        
        for val in anagram_dict.values():
            res.append(val)
        
        return res