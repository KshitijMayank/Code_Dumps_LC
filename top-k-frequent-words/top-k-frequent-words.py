from collections import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        w_dict = Counter(words)
        
        res = sorted(w_dict, key=lambda x: (-w_dict[x], x))
        
        return res[:k]
        