from typing import List

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # Step 1: Define a helper function to check if a word starts and ends with a vowel
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        def is_vowel_word(word: str) -> bool:
            return word[0] in vowels and word[-1] in vowels
        
        # Step 2: Create an array where each entry is 1 if the word starts and ends with a vowel, otherwise 0
        is_vowel_start_end = [1 if is_vowel_word(word) else 0 for word in words]
        
        # Step 3: Build the prefix sum array
        prefix = [0] * len(words)
        prefix[0] = is_vowel_start_end[0]
        
        for i in range(1, len(words)):
            prefix[i] = prefix[i-1] + is_vowel_start_end[i]
        
        # Step 4: Answer each query using the prefix sum array
        result = []
        for li, ri in queries:
            if li > 0:
                result.append(prefix[ri] - prefix[li-1])
            else:
                result.append(prefix[ri])
        
        return result
