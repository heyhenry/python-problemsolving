# Leetcode No.567: Permutation in String
# More Info: https://leetcode.com/problems/permutation-in-string/description/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # count frequency of s1's characters
        s1_dict = {}
        for c in s1:
            if c not in s1_dict:
                s1_dict[c] = 1
            else:
                s1_dict[c] += 1
        
        s1_len = len(s1)
        for i in range(len(s2)):
            s2_window = s2[i:s1_len+i]
            # counter frequency of s2's window of characters
            s2_counter = {}
            # get count of all the character's counts per window (s2_window)
            for c in s2_window:
                if c not in s2_counter:
                    s2_counter[c] = 1
                else:
                    s2_counter[c] += 1

            # compare the 2 dicts, if frequency matches - we found a permutation of s1 in s2
            if s1_dict == s2_counter:
                print("True")
                return True
            
        print("False")
        return False
                    

            

        
        

test_case_01 = ("ab", "eidbaooo")
test_case_02 = ("ab", "eidboaoo")

s = Solution()

s.checkInclusion(test_case_01[0], test_case_01[1])
s.checkInclusion(test_case_02[0], test_case_02[1])