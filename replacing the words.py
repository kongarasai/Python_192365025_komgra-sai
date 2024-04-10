def minDistance(word1, word2):
    dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
    for i in range(len(word1) + 1):
        dp[i][0] = i
    for j in range(len(word2) + 1):
        dp[0][j] = j
    for i in range(1, len(word1) + 1):
        for j in range(1, len(word2) + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
    return dp[len(word1)][len(word2)]
test_cases = [
    ("horse", "ros"),          
    ("intention", "execution"),
    ("sunday", "saturday"),    
    ("cat", "cut"),            
    ("girl", "grill")          ]
for word1, word2 in test_cases:
    print("Input: word1 =", word1, ", word2 =", word2)
    print("Output:", minDistance(word1, word2))
    print()
