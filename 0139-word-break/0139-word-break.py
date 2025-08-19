class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        maxlen = max(map(len, wordDict))
        words = set(wordDict)

        @cache
        def dfs(i):
            if i==0:
                return True
            for j in range(i-1, i-maxlen-1, -1):
                if s[j:i] in words and dfs(j):
                    return True
            return False
        return dfs(len(s))