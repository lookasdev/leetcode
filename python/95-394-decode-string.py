class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()

                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k

                stack.append(int(k) * substr)

        return "".join(stack)

        # result = ""
        # for part in stack:
        #     result += part
        # return result
        # 🔹 This works the same as "".join(stack) but is slower for large strings, because += creates a new string each time (strings are immutable in Python).
        # 🔹 "".join(stack) is faster and more memory-efficient, since it builds the final string in one go. ✅