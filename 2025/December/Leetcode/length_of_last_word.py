class Solution:
    def length_of_last_word(self, s : str) -> int:
        
        # split string into a list of words
        words = s.split()

        # return the length of the last word (element)
        return len(words[-1])

solution = Solution()

test_case_1 = "Hello World"
test_case_2 = "   fly me   to   the moon  "
test_case_3 = "luffy is still joyboy"

print(solution.length_of_last_word(test_case_1))
print(solution.length_of_last_word(test_case_2
print(solution.length_of_last_word(test_case_3))