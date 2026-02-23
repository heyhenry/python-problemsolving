"""
Returns the celsius equivalent of the farhenheit `temp`
Examples:
in_celsius(32.0) ~> 0.0
in_celsius(212.0) ~> 100.0
in_celsius(-40.0) ~> -40.0
"""
class Problem:
    def in_celsius(self, farhenheit : float) -> float:
        return (farhenheit - 32) * 5/9

test_01 = 32.0
test_02 = 212.0
test_03 = -40.0

p = Problem()

print(p.in_celsius(test_01))
print(p.in_celsius(test_02))
print(p.in_celsius(test_03))