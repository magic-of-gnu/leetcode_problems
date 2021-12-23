from collections import Counter

class Solution:
    def numMatchingSubseq2(self, s: str, words):

        d = dict()
        words_counter = dict()
        for word in words:
            if word in words_counter:
                words_counter[word] = 0

            words_counter[word]['count'] += 1

            if word[0] not in d:
                d[word[0]] = set()
            d[word[0]].add((word,0))
        
        count_words = 0

        for ind, char in enumerate(s):
            st = d.get(char, None)

            if st is None:
                continue

            d[char] = set()
            
            for word, counter in st:
                if counter + 1 == len(word):
                    count_words += words_counter[word]
                else:
                    if word[counter+1] not in d:
                        d[word[counter+1]] = set()

                    d[word[counter+1]].add((word, counter+1))

        return count_words


if __name__ == "__main__":
    s = "aabbacedeqaz"
    words = ["ba", "abc", "cde", "aba"]
    output = 4

    sol = Solution()
    print(sol.numMatchingSubseq(s, words))
    
