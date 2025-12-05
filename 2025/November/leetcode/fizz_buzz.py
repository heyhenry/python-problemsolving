class Solution:
    def fizz_buzz(self, n : int) -> list[str]:
        answer = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                answer.append("FizzBuzz")
            elif i % 3 == 0:
                answer.append("Fizz")
            elif i % 5 == 0:
                answer.append("Buzz")
            else:
                answer.append(str(i))
        return answer

solution = Solution()

test_case_1 = 3
test_case_2 = 5
test_case_3 = 15

print(solution.fizz_buzz(test_case_1))
print(solution.fizz_buzz(test_case_2))
print(solution.fizz_buzz(test_case_3))