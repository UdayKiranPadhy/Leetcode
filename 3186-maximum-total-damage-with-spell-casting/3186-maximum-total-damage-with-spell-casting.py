class Solution:
    def maximumTotalDamage(self, power: List[int]) -> int:
        N = len(power)
        seen = set()
        freq = Counter(power)
        gg = []
        for spell in power:
            if spell in seen:
                continue
            seen.add(spell)
            gg.append([spell,spell * freq[spell]])
        gg.sort()
        N = len(gg)
        print(gg)

        @cache
        def dp(index):
            if index >= len(gg):
                return 0
            pick = not_pick = 0
            if index + 1 < N and abs(gg[index+1][0] - gg[index][0]) > 2:
                pick = gg[index][1] + dp(index+1)
            elif index + 2 < N and abs(gg[index + 2][0] - gg[index][0]) > 2:
                pick = gg[index][1] + dp(index+2)
            else:
                pick = gg[index][1] + dp(index+3)

            not_pick = dp(index+1)
            return max(pick,not_pick)

        return dp(0)