class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0  # If needle is empty, return 0
        return haystack.find(needle)
