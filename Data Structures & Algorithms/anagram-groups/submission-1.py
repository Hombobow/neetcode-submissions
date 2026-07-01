class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_sorted = strs.copy()
        for i, word in enumerate(strs_sorted):
            strs_sorted[i] = "".join(sorted(word))
        
        str_indexes = defaultdict(list)
        for i, word in enumerate(strs_sorted):
            str_indexes[word].append(i)
        
        output = []
        for key, value in str_indexes.items():
            anagrams = []
            for v in value:
                anagrams.append(strs[v])
            output.append(anagrams)
        
        return output