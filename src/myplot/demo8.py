class Solution(object):
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 字符串为空则返回零
        if not s:
            return 0

        window = []  # 滑动窗口数组
        max_length = 0  # 最长串长度

        # 遍历字符串
        for c in s:
            # 如果字符不在滑动窗口中，则直接扩展窗口
            if c not in window:
                # 使用当前字符扩展窗口
                window.append(c)
            # 如果字符在滑动窗口中，则
            # 1. 从窗口中移除重复字符及之前的字符串部分
            # 2. 再扩展窗口
            else:
                # 从窗口中移除重复字符及之前的字符串部分，新字符串即为无重复字符的字符串
                window = window[window.index(c) + 1:]
                # 扩展窗口
                window.append(c)

            # 更新最大长度
            max_length = max(len(window), max_length)

        return max_length if max_length != 0 else len(s)


class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num1) == 0 or len(num2) == 0:
            return "error"

        int1 = int(num1)
        count = 0
        sum_ = 0
        for c in num2[::-1]:
            temp = int(c)
            muti = int1 * temp * pow(10, count)
            sum_ = sum_ + muti
            count += 1

        return str(sum_)


if __name__ == "__main__":
    solution = Solution()
    # str_ = "abcabcbb"
    # i = solution.lengthOfLongestSubstring(str_)
    # print(i)
    res = solution.multiply("123", "111")
    print(res)
    # 28 ms	11.8 MB	Python
