class Solution: 
    def is_anagram(self, s : str, t : str) -> bool:

        # check if both have the same length
        if len(s) != len(t):
            return False

        # initialise dictionary
        s_dict = {}
        t_dict = {}

        # create lists of unique characters found for each string
        s_unqiue_chars = list(set(s))
        t_unique_chars = list(set(t))

        # order it so it can be compared 1:1
        s_unqiue_chars.sort()
        t_unique_chars.sort()
        
        # check if both strings have the same characters
        for i in range(len(s_unqiue_chars)):
            if s_unqiue_chars != t_unique_chars:
                return False
            
        # create a dictionary for each string that counts each unique character count
        for i in range(len(s_unqiue_chars)):
            s_dict[s_unqiue_chars[i]] = s.count(s_unqiue_chars[i])
        
        for i in range(len(t_unique_chars)):
            t_dict[t_unique_chars[i]] = t.count(t_unique_chars[i])

        # check if both have the same amount for each character
        for key, val in s_dict.items():
            if val != t_dict[key]:
                return False
            
        # if none of the above checkers get triggered, then both strings are considered anagrams of each other
        return True

solution = Solution()

test_case_1 = ("anagram", "nagaram")
test_case_2 = ("rat", "car")

print(solution.is_anagram(test_case_1[0], test_case_1[1]))
print(solution.is_anagram(test_case_2[0], test_case_2[1]))