class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        ends = {c: i for i, c in enumerate(s)}
        curr = 0
        ans = [0]
        while curr < len(s):
            end = ends[s[curr]]
            while curr <= end:
                end = max(end, ends[s[curr]])
                curr += 1
            ans.append(curr)
        return [ans[i] - ans[i-1] for i in range(1, len(ans))]