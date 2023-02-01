#https://leetcode.com/problems/isomorphic-strings/?envType=study-plan&id=level-1
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_hashmap = {}
        t_hashmap = {}
        for idx, letter in enumerate(s):
            if letter not in s_hashmap and t[idx] not in t_hashmap:
                s_hashmap[letter] = t[idx]
                t_hashmap[t[idx]] = letter
            else:
                if s_hashmap.get(letter) != t[idx] or t_hashmap.get(t[idx]) != letter:
                    return False
        return True