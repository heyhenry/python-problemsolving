"""
Returns the string `s` in reverse order
Examples:
reverse_string('abc') -> 'cba'
reverse_string('') -> ''
reverse_string('abab') -> 'baba'
"""
class Problem:
    def reverse_string(self, s : str) -> str:
        return s[::-1]

test_01 = "abc"
test_02 = ""
test_03 = "abab"

p = Problem()

print(p.reverse_string(test_01))
print(p.reverse_string(test_02))
print(p.reverse_string(test_03))
