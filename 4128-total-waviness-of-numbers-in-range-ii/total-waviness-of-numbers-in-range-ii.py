from functools import lru_cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        def count(x):
            if x < 0:
                return 0

            s = str(x)

            @lru_cache(None)
            def dp(i, prev, prev2, leading, tight):
                if i == len(s):
                    return (1, 0)

                limit = int(s[i]) if tight else 9
                total_cnt = 0
                total_wave = 0

                for d in range(limit + 1):
                    ntight = tight and d == limit if tight else False
                    nleading = leading and d == 0

                    nprev2 = prev
                    nprev = -1 if nleading else d

                    cnt, wav = dp(
                        i + 1,
                        nprev,
                        nprev2,
                        nleading,
                        tight and d == int(s[i])
                    )

                    total_cnt += cnt

                    if (not leading and
                        prev2 != -1 and
                        ((prev2 < prev and prev > d) or
                         (prev2 > prev and prev < d))):
                        total_wave += cnt

                    total_wave += wav

                return (total_cnt, total_wave)

            return dp(0, -1, -1, True, True)[1]

        return count(num2) - count(num1 - 1)