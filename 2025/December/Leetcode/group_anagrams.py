class Solution:
    def group_anagrams(self, strs : list[str]) -> list[list[str]]:
        # create a dictionary that will contain all the groups of anagrams found in strs
        anagrams = {}

        # loop through strs and use a sorted i as the key for each group of anagrams in the dictionary
        for i in strs:
            # create the sorted i for comparison and reference use
            sorted_i = "".join(sorted(i))
            # create a new key in the anagrams dictionary with the sorted i 
            # and store the original i value within
            if sorted_i not in anagrams:
                anagrams[sorted_i] = [i]
            # store original i values into the respective sorted i key
            else:
                anagrams[sorted_i].append(i)

        results = []
        # loop through the values in the dictionary and store into the results list as per output request
        for i in anagrams.values():
            results.append(i)

        return results

solution = Solution()

test_case_1 = ["eat","tea","tan","ate","nat","bat"]
test_case_2 = [""]
test_case_3 = ["a"]

print(solution.group_anagrams(test_case_1))
print(solution.group_anagrams(test_case_2))
print(solution.group_anagrams(test_case_3))