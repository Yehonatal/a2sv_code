class Solution:
    def minDeletionSize(self, strs):
        count = 0

        m = len(strs)
        n = len(strs[0])

        for i in range(n):
            word = ''
            for s in strs:
                word += s[i]
            if word != "".join(sorted(word)):
                count += 1

        return count


sol = Solution()
strs = ["cba", "daf", "ghi"]
print(sol.minDeletionSize(strs))
