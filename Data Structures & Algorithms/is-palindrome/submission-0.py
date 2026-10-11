import re
class Solution:

    def isPalindrome(self, s: str) -> bool:
        cleaned_s = re.sub(r'[^a-zA-Z0-9]', '', s)
        cleaned_s = cleaned_s.lower()
        reversed_s = reversed(cleaned_s)
        new_s = ''.join(reversed_s)

        return cleaned_s == new_s