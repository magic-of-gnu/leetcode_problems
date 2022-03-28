class Solution:
    def fullJustify(self, words, maxWidth):

        def can_fill_in(curr_nchars, curr_nwords, maxWidth):

            if curr_nchars + (curr_nwords-1) > maxWidth:
                return False

            return True

        def fill_line(idx_start, idx_end, words, curr_nchars, curr_nwords, maxWidth):

            if curr_nwords == 1:
                return words[idx_start] + ' ' * (maxWidth-len(words[idx_start]))

            rem_len = maxWidth - curr_nchars

            result = []

            while idx_start < idx_end: # 0 < 4

                if idx_start == idx_end - 1:
                    result.append(words[idx_start])
                    break

                # rem_len = rem_len - len(words[idx_start])  # 5 - 7 = 13

                result.append(words[idx_start])  # Science

                nspaces = rem_len // (curr_nwords - 1)  # 5 // 3 = 1
                rem_nspaces = rem_len % (curr_nwords - 1)  # 5 % 3 = 2

                if rem_nspaces != 0: 
                    nspaces += 1
                    
                result.append(' ' * nspaces) #[Science 
                rem_len -= nspaces
                curr_nwords -= 1
                idx_start += 1

            return ''.join(result)

        current_count = 0
        idx_start = 0
        idx = 0
        idx_end = 0
        n = len(words)

        curr_nchars = 0
        curr_nwords = 0

        result = []

        while idx < n:

            curr_nwords += 1
            curr_nchars += len(words[idx])

            can_fill = can_fill_in(curr_nchars, curr_nwords, maxWidth)

            if can_fill is False:

                curr_nwords -= 1
                curr_nchars -= len(words[idx])

                text_line = fill_line(idx_start, idx, words, curr_nchars, curr_nwords, maxWidth)

                result.append(text_line)

                curr_nwords = 0
                curr_nchars = 0
                idx_start = idx
                continue

            if idx == n - 1:
                break

            idx += 1

        result.append(' '.join(words[idx_start:]))
        result[-1] += ' ' * (maxWidth - len(result[-1]))

        return result


if __name__ == "__main__":
    words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"]
    maxWidth = 20

    words = ["What","must","be","acknowledgment","shall","be"]
    maxWidth = 16

    sol = Solution()
    print(sol.fullJustify(words, maxWidth))

    output = [
"Science  is  what we",
"understand      well",
"enough to explain to",
"a  computer.  Art is",
"everything  else  we",
"do                  "
]
