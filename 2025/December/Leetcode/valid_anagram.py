class Solution:
    def is_anagram(self, s : str, t : str) -> bool:

        # immediately return False if strings are not the same length
        if len(s) != len(t):
            return False
        
        # re-sort strings alphabetically
        s_sorted = "".join(sorted(s))
        t_sorted = "".join(sorted(t))

        # compare each character in both string for consistency, else return False
        # note: this is an appropriate means to determine validity, as there should be equal amount of characters per string
        for i in range(len(s_sorted)):
            if s_sorted[i] != t_sorted[i]:
                return False
        
        # if no False flags are triggered, t is deemed a valid anagram of s
        return True

solution = Solution()

test_case_1 = ("anagram", "nagaram")
test_case_2 = ("rat", "car")

print(solution.is_anagram(test_case_1[0], test_case_1[1])) # true
print(solution.is_anagram(test_case_2[0], test_case_2[1])) # false


