class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import Counter

        need = Counter(t)
        need_cnt = len(t)          # 还需要匹配的字符总数
        left = 0
        start, min_len = 0, float('inf')

        for right, ch in enumerate(s):
            if need[ch] > 0:       # ch 是 t 中需要的字符
                need_cnt -= 1
            need[ch] -= 1          # 无论是否需要，都减（多余的会变负）

            # 窗口已满足所有字符，尝试收缩左边界
            while need_cnt == 0:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    start = left

                # 移出 s[left]
                need[s[left]] += 1
                if need[s[left]] > 0:   # 移走了一个必需字符，窗口不再满足
                    need_cnt += 1
                left += 1

        return "" if min_len == float('inf') else s[start:start + min_len]
