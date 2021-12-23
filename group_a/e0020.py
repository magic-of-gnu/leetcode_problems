class Solution:
    def isValid(self, s: str) -> bool:
        _open, _close = set(["(", "[", "{"]), set([")", "]", "}"])
        match = {"(": ")", "[": "]", "{": "}"}
        arr = []

        for char in s:
            if char in _open:
                arr.append(char)
            elif char in _close:
                if len(arr) == 0:
                    return False
                if match[arr.pop()] != char:
                    return False

        if len(arr) > 0:
            return False

        return True
                
if __name__ == "__main__":
    s = "()[]{}"

    sol = Solution()
    print(sol.isValid(s))
