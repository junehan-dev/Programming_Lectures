class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0;
        end = len(s) - 1;
        result = True;

        while (result and start <= end):
            # while still Palindrom and comparing pair is left.
            while (start <= end and not (s[start].isalnum() and s[end].isalnum())):
                # move cursor to next alnum character
                start = start if s[start].isalnum() else start + 1;
                end = end if s[end].isalnum() else end - 1;
            if (start > end):
                return result
                # if comparable?
            result = s[start].lower() == s[end].lower();
            start += 1;
            end -= 1;
        return (result);


if __name__ == "__main__":
    phrases = [
            "A man, a plan, a canal: Panama", "race a car", " ", ".,"
            ];
    expects = [
            True, False, True, True];

    aSol = Solution();
    for i, p in enumerate(phrases):
        assert(aSol.isPalindrome(p) == expects[i]);

