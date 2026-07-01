class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_indexes = defaultdict(list)
        for i, word in enumerate(strs):
            freq = [0] * 26
            for c in word:
                freq[ord(c) - ord('a')] += 1
            str_indexes[tuple(freq)].append(word)

        output = []
        for k, v in str_indexes.items():
            anagram = []
            for word in v:
                anagram.append(word)
            output.append(anagram)
        
        return output
