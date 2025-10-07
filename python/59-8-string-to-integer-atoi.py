class Solution:
    # T: O(n)
    # S: O(1)
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()  # remove leading spaces
        # def my_lstrip(s: str, chars: str = " \t\n\r\f\v") -> str:
        #     i = 0
        #     while i < len(s) and s[i] in chars:
        #         i += 1
        #     return s[i:]

        if not s:
            return 0

        i = 0
        sign = 1

        # check sign
        if s[i] == "+":
            i += 1
        elif s[i] == "-":
            i += 1
            sign = -1

        parsed = 0

        # parse digits
        while i < len(s):
            cur = s[i]
            if not cur.isdigit():
                break
            parsed = parsed * 10 + int(cur)
            i += 1

        parsed *= sign

        # clamp to 32-bit signed integer range
        if parsed > 2**31 - 1:
            return 2**31 - 1
        elif parsed < -2**31:
            return -2**31
        else:
            return parsed