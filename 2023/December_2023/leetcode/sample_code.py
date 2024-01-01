class Solution:
    # calculate the int value of a binary string
    def calculate_binary(self, s : str) -> int:

        result = 0

        # loop through formula for each char in binary str respectively
        for i in range(len(s)):
            result += int(s[i]) * (2**(len(s)-i-1))

        return result

    # convert int value into binary string
    def convert_to_binary(self, n : int) -> str:

        im_done = True
        result = ''

        # continuously update and iterate through the given number until its value is less than 1 
        # meaning there are no more possible remainders
        while im_done:

            remainder = int(n) % 2
            
            # store the remainders as they will be the binary strings
            result += str(remainder)

            n = int(n) / 2

            if n < 1:
                im_done = False

        final_result = ''

        # the given result is the correct binary strings but in reversed order
        # so loop through it backwards and store into a final_result variable
        for i in range(len(result)-1, -1, -1):
            final_result += result[i]
        
        return final_result

    def add_binary(self, a : str, b : str) -> str:

        sum = self.calculate_binary(a) + self.calculate_binary(b)

        return self.convert_to_binary(sum)